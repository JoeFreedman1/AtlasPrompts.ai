"""Assemble the ready-to-deploy Netlify folder for the Well Listed sales site.

Run:  python3 launch-kit/tools/build_site.py

Reads:
  launch-kit/sales-site/version-a.html, version-b.html, privacy.html, terms.html
  launch-kit/sales-site/placeholders.json      the values that replace [PLACEHOLDERS]
  launch-kit/sales-site/lead-magnet/uk-listing-cheat-sheet.md
  launch-kit/marketing/d-blog/B*.md           the blog articles
Writes launch-kit/sales-site/netlify-site/ :
  index.html            the live version (A or B, set "live_version" in placeholders.json)
  b/index.html          the other version, for testing (or a/index.html)
  privacy.html, terms.html
  blog/index.html and blog/<slug>.html
  free/uk-listing-cheat-sheet.pdf and .html (the lead magnet)
  og-image.png, robots.txt, sitemap.xml (sitemap only once site_url is set)
Placeholders still unfilled are listed at the end so nothing goes live half-done.
"""
import datetime
import html
import json
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
KIT = os.path.abspath(os.path.join(HERE, ".."))
ROOT = os.path.abspath(os.path.join(KIT, ".."))
SITE = os.path.join(KIT, "sales-site")
OUT = os.path.join(SITE, "netlify-site")
sys.path.insert(0, HERE)
import mdlite  # noqa: E402

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@700;800&family=Inter:wght@400;600&family=JetBrains+Mono&display=swap" rel="stylesheet">')
FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='12' fill='%23FAF6EF'/%3E"
           "%3Ctext x='8' y='42' font-family='Arial' font-weight='900' font-size='28' fill='%231F2A44'%3EWL%3C/text%3E"
           "%3Cpath d='M46 40l5 5 9-12' stroke='%231E7F55' stroke-width='5' fill='none'/%3E%3C/svg%3E")
CSS = """
:root{--ink:#1F2A44;--cream:#FAF6EF;--kraft:#C9A27E;--green:#1E7F55;--yellow:#F2C84B;--muted:#5b6478;--line:#e6dccd}
*{box-sizing:border-box}body{margin:0;background:var(--cream);color:var(--ink);font:17px/1.65 Inter,system-ui,sans-serif}
a{color:var(--green)}header,footer{background:var(--ink);color:var(--cream)}
header .in,footer .in{max-width:760px;margin:0 auto;padding:14px 18px;display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap}
header a{color:var(--cream);text-decoration:none;font:800 1.1rem Archivo,sans-serif}header a b{color:var(--yellow)}
header nav a{font:600 .9rem Inter,sans-serif;margin-left:14px;opacity:.9}
main{max-width:760px;margin:0 auto;padding:22px 18px 50px}
h1,h2,h3{font-family:Archivo,Inter,sans-serif;line-height:1.2}h1{font-size:2rem;font-weight:800}h2{margin-top:2rem;font-size:1.4rem}
code{font-family:'JetBrains Mono',monospace;background:#f1eadf;padding:.1em .3em;border-radius:4px;font-size:.88em}
pre{background:#fff;border:1px solid var(--line);border-left:5px solid var(--green);border-radius:8px;padding:14px;white-space:pre-wrap;word-wrap:break-word}
pre code{background:none;padding:0}
blockquote{margin:1rem 0;padding:.6rem 1rem;background:#fff8e1;border-left:5px solid var(--yellow);border-radius:6px}
.table-wrap{overflow-x:auto}table{border-collapse:collapse;width:100%;background:#fff;font-size:.92rem}th,td{border:1px solid var(--line);padding:6px 8px;text-align:left;vertical-align:top}th{background:var(--ink);color:var(--cream)}
.cta{background:#fff;border:3px solid var(--kraft);outline:2px dashed var(--kraft);outline-offset:6px;border-radius:14px;padding:20px;margin:36px 0}
.btn{display:inline-block;background:var(--green);color:#fff;text-decoration:none;font-weight:600;padding:12px 18px;border-radius:10px;margin:6px 6px 0 0}
.btn.alt{background:none;color:var(--ink);border:2px solid var(--kraft)}
.list a{display:block;background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px;margin:10px 0;text-decoration:none;color:var(--ink)}
.list a span{display:block;color:var(--muted);font-size:.9rem}
footer{font-size:.85rem}footer a{color:var(--cream)}
@media print{header,footer,.cta{display:none}body{background:#fff}}
"""


def read(p, d=""):
    try:
        with open(p, encoding="utf-8") as f:
            return f.read()
    except OSError:
        return d


def write(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(s)


def load_placeholders():
    path = os.path.join(SITE, "placeholders.json")
    data = json.loads(read(path, "{}") or "{}")
    return data


def fill(text, ph):
    for k, v in ph.items():
        if k.startswith("_") or k in ("live_version", "site_url") or not isinstance(v, str) or not v.strip():
            continue
        text = text.replace("[%s]" % k, v)
    return text


def front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    meta = {}
    if m:
        for line in m.group(1).split("\n"):
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
        text = text[m.end():]
    return meta, text


def page(title, desc, body, canonical=""):
    canon = '<link rel="canonical" href="%s">' % html.escape(canonical) if canonical else ""
    return f"""<!doctype html><html lang="en-GB"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc, quote=True)}">
<meta property="og:title" content="{html.escape(title, quote=True)}"><meta property="og:description" content="{html.escape(desc, quote=True)}">
<meta property="og:type" content="article"><meta property="og:image" content="/og-image.png">{canon}
<link rel="icon" href="{FAVICON}">{FONTS}<style>{CSS}</style>
<!-- ANALYTICS SNIPPET -->
</head><body>
<header><div class="in"><a href="/">Well Listed <b>&#10003;</b></a><nav><a href="/blog/">Blog</a><a href="/#free-cheat-sheet">Free cheat sheet</a><a href="/#buy">The kit</a></nav></div></header>
<main>{body}</main>
<footer><div class="in"><span>Well Listed. Not affiliated with or endorsed by eBay, Vinted, Depop, Etsy, Amazon or TikTok.</span><span><a href="/privacy.html">Privacy</a> &middot; <a href="/terms.html">Terms</a></span></div></footer>
</body></html>"""


CTA = """<div class="cta"><h2 style="margin-top:0">Get the free UK Listing Cheat Sheet</h2>
<p>10 free prompts, a character-limit table for each platform and a 7-point check to run before you post.</p>
<a class="btn" href="/#free-cheat-sheet">Get the free cheat sheet</a><a class="btn alt" href="/#buy">See the full kit</a></div>"""


def build_blog(ph, site_url):
    items = []
    for fn in sorted(os.listdir(os.path.join(KIT, "marketing", "d-blog"))):
        if not re.match(r"^B\d\d-.*\.md$", fn):
            continue
        meta, body = front_matter(read(os.path.join(KIT, "marketing", "d-blog", fn)))
        slug = meta.get("slug") or fn[4:-3]
        title = meta.get("title", slug)
        desc = meta.get("meta_description", "")
        content = mdlite.convert(fill(body, ph))
        canonical = "%s/blog/%s.html" % (site_url.rstrip("/"), slug) if site_url else ""
        write(os.path.join(OUT, "blog", slug + ".html"), page(title + " | Well Listed", desc, content + CTA, canonical))
        items.append((slug, title, desc))
    lst = "".join('<a href="/blog/%s.html"><b>%s</b><span>%s</span></a>' % (s, html.escape(t), html.escape(d)) for s, t, d in items)
    body = "<h1>The Well Listed blog</h1><p>Practical, UK-specific guides to writing listings, pricing and dealing with buyers.</p><div class=\"list\">%s</div>%s" % (lst, CTA)
    write(os.path.join(OUT, "blog", "index.html"), page("Blog | Well Listed", "Practical guides for UK sellers on eBay, Vinted, Depop, Etsy, Amazon and TikTok Shop.", body))
    return items


def chromium(script, *args):
    env = dict(os.environ, NODE_PATH="/opt/node22/lib/node_modules")
    try:
        subprocess.run(["node", "-e", script] + list(args), check=True, env=env, timeout=180)
        return True
    except Exception as e:
        print("Chromium step skipped:", e)
        return False


def build_lead_magnet(ph):
    src = os.path.join(SITE, "lead-magnet", "uk-listing-cheat-sheet.md")
    if not os.path.exists(src):
        print("Lead magnet source missing:", src)
        return
    body = mdlite.convert(fill(read(src), ph))
    doc = page("The UK Listing Cheat Sheet | Well Listed", "Free prompts and checklists for UK sellers.", body)
    doc = doc.replace("<header>", "<header style=\"display:none\">")
    h = os.path.join(OUT, "free", "uk-listing-cheat-sheet.html")
    write(h, doc)
    pdf = os.path.join(OUT, "free", "uk-listing-cheat-sheet.pdf")
    chromium(r"""const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+process.argv[1]);try{await p.waitForLoadState('networkidle',{timeout:8000})}catch(e){}
await p.pdf({path:process.argv[2],format:'A4',printBackground:true,margin:{top:'14mm',bottom:'14mm',left:'14mm',right:'14mm'}});await b.close()})();""", h, pdf)


def build_og_image():
    card = f"""<html><head>{FONTS}<style>body{{margin:0;width:1200px;height:630px;background:#FAF6EF;display:flex;align-items:center;justify-content:center;font-family:Archivo,Arial,sans-serif}}
.l{{background:#fff;border:6px solid #C9A27E;outline:4px dashed #C9A27E;outline-offset:14px;border-radius:24px;padding:56px 64px;width:1000px}}
.b{{font-weight:800;font-size:34px;color:#1F2A44}}.b i{{color:#1E7F55;font-style:normal}}h1{{font-size:64px;line-height:1.08;margin:18px 0;color:#1F2A44}}
h1 span{{background:#F2C84B;padding:0 8px}}p{{font:28px Inter,Arial,sans-serif;color:#5b6478;margin:0}}</style></head>
<body><div class="l"><div class="b">Well Listed <i>&#10003;</i></div><h1>UK listings that stick to <span>your facts</span></h1><p>AI prompts and templates for eBay, Vinted, Depop, Etsy, Amazon and TikTok Shop sellers</p></div></body></html>"""
    tmp = os.path.join(OUT, "_og.html")
    write(tmp, card)
    chromium(r"""const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1200,height:630}});
await p.goto('file://'+process.argv[1]);try{await p.waitForLoadState('networkidle',{timeout:6000})}catch(e){}
await p.screenshot({path:process.argv[2]});await b.close()})();""", tmp, os.path.join(OUT, "og-image.png"))
    os.remove(tmp)


def build_brand_assets():
    """Logo and Gumroad cover images, so the owner does not have to design them (not deployed)."""
    outdir = os.path.join(SITE, "brand-assets")
    os.makedirs(outdir, exist_ok=True)
    logo = f"""<html><head>{FONTS}<style>body{{margin:0;width:1080px;height:1080px;background:#FAF6EF;display:flex;align-items:center;justify-content:center;font-family:Archivo,Arial,sans-serif}}
.l{{font-weight:800;font-size:420px;color:#1F2A44;letter-spacing:-12px}}.l i{{color:#1E7F55;font-style:normal;font-size:300px;margin-left:10px}}</style></head>
<body><div class="l">WL<i>&#10003;</i></div></body></html>"""
    cover = f"""<html><head>{FONTS}<style>body{{margin:0;width:1280px;height:720px;background:#1F2A44;display:flex;align-items:center;justify-content:center;font-family:Archivo,Arial,sans-serif}}
.c{{background:#FAF6EF;border:6px solid #C9A27E;outline:4px dashed #C9A27E;outline-offset:14px;border-radius:24px;padding:56px 64px;width:1060px}}
.b{{font-weight:800;font-size:34px;color:#1F2A44}}.b i{{color:#1E7F55;font-style:normal}}h1{{font-size:78px;line-height:1.05;margin:16px 0;color:#1F2A44}}
p{{font:30px Inter,Arial,sans-serif;color:#5b6478;margin:0}}</style></head>
<body><div class="c"><div class="b">Well Listed <i>&#10003;</i></div><h1>The Well Listed Kit</h1><p>AI prompts, templates and checklists for UK sellers on eBay, Vinted, Depop, Etsy, Amazon and TikTok Shop</p></div></body></html>"""
    for name, htmltext, w, h in (("logo-1080.png", logo, 1080, 1080), ("gumroad-cover-1280x720.png", cover, 1280, 720)):
        tmp = os.path.join(outdir, "_tmp.html")
        write(tmp, htmltext)
        chromium(r"""const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:+process.argv[3],height:+process.argv[4]}});
await p.goto('file://'+process.argv[1]);try{await p.waitForLoadState('networkidle',{timeout:6000})}catch(e){}
await p.screenshot({path:process.argv[2]});await b.close()})();""", tmp, os.path.join(outdir, name), str(w), str(h))
        os.remove(tmp)


BLOG_MARKER = "<!-- BLOG LINKS: filled in by tools/build_site.py from the blog articles -->"


def blog_links_html():
    items = []
    for fn in sorted(os.listdir(os.path.join(KIT, "marketing", "d-blog"))):
        if re.match(r"^B\d\d-.*\.md$", fn):
            meta, _ = front_matter(read(os.path.join(KIT, "marketing", "d-blog", fn)))
            items.append((meta.get("slug") or fn[4:-3], meta.get("title", ""), meta.get("meta_description", "")))
    lis = "".join('<li><a href="/blog/%s.html">%s<span>%s</span></a></li>' % (sl, html.escape(t), html.escape(d)) for sl, t, d in items)
    return ('<section class="section guides" id="guides"><div class="wrap narrow"><h2>Free guides for UK sellers</h2>'
            '<p>Practical how-tos you can use today, no sign-up needed.</p><ul>%s</ul>'
            '<p><a href="/blog/">All guides</a></p></div></section>' % lis)


def main():
    ph = load_placeholders()
    su = (ph.get("site_url") or "").strip().rstrip("/")
    if su:
        ph.setdefault("SALES_PAGE_URL", "")
        ph.setdefault("CHEAT_SHEET_LINK", "")
        if not ph["SALES_PAGE_URL"]:
            ph["SALES_PAGE_URL"] = su + "/"
        if not ph["CHEAT_SHEET_LINK"]:
            ph["CHEAT_SHEET_LINK"] = su + "/free/uk-listing-cheat-sheet.pdf"
    # Launch dates: day 1 is launch_date (Claude sets it on deploy day; if empty, today).
    try:
        ld = datetime.date.fromisoformat((ph.get("launch_date") or "").strip())
    except ValueError:
        ld = datetime.date.today()
    fmt = lambda d: "%s %d %s" % (d.strftime("%A"), d.day, d.strftime("%B %Y"))
    if not (ph.get("LAUNCH END DATE") or "").strip():
        ph["LAUNCH END DATE"] = fmt(ld + datetime.timedelta(days=13))
    if not (ph.get("DATE") or "").strip():
        ph["DATE"] = "%d %s" % (ld.day, ld.strftime("%B %Y"))
    live = (ph.get("live_version") or "A").upper()
    site_url = (ph.get("site_url") or "").strip()
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    guides = blog_links_html()
    a = fill(read(os.path.join(SITE, "version-a.html")), ph).replace(BLOG_MARKER, guides)
    b = fill(read(os.path.join(SITE, "version-b.html")), ph).replace(BLOG_MARKER, guides)
    main_html, other_html, other_dir = (a, b, "b") if live == "A" else (b, a, "a")
    write(os.path.join(OUT, "index.html"), main_html)
    other_html = other_html.replace("<head>", '<head><meta name="robots" content="noindex">', 1)
    write(os.path.join(OUT, other_dir, "index.html"), other_html)
    for name in ("privacy.html", "terms.html"):
        if os.path.exists(os.path.join(SITE, name)):
            write(os.path.join(OUT, name), fill(read(os.path.join(SITE, name)), ph))
    items = build_blog(ph, site_url)
    build_lead_magnet(ph)
    thanks = """<h1>Thank you</h1><p>Your free UK Listing Cheat Sheet is ready.</p>
<p><a class="btn" href="/free/uk-listing-cheat-sheet.pdf">Download the cheat sheet (PDF)</a></p>
<p>Prefer to read it on screen? <a href="/free/uk-listing-cheat-sheet.html">Open the web version</a>.</p>
<p>When you want every prompt, template and checklist in one place, <a href="/#buy">see The Well Listed Kit</a>. Or browse our <a href="/blog/">free guides</a>.</p>"""
    write(os.path.join(OUT, "free", "thanks.html"), page("Your cheat sheet | Well Listed", "Download the free UK Listing Cheat Sheet.", thanks).replace("<head>", '<head><meta name="robots" content="noindex">', 1))
    build_og_image()
    write(os.path.join(OUT, "robots.txt"), "User-agent: *\nAllow: /\n" + ("Sitemap: %s/sitemap.xml\n" % site_url.rstrip("/") if site_url else ""))
    if site_url:
        today = datetime.date.today().isoformat()
        urls = ["/", "/blog/"] + ["/blog/%s.html" % s for s, _, _ in items]
        xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
            "<url><loc>%s%s</loc><lastmod>%s</lastmod></url>\n" % (site_url.rstrip("/"), u, today) for u in urls) + "</urlset>\n"
        write(os.path.join(OUT, "sitemap.xml"), xml)
    build_brand_assets()
    # the owner's legal name and address may appear ONLY on terms.html and privacy.html
    for key in ("LEGAL NAME", "ADDRESS"):
        val = (ph.get(key) or "").strip()
        if not val:
            continue
        for dp, _, fns in os.walk(OUT):
            for fn in fns:
                if fn.endswith((".html", ".txt", ".xml")) and fn not in ("terms.html", "privacy.html"):
                    if val in read(os.path.join(dp, fn)):
                        print("WARNING: your %s appears in %s. It must only be on terms and privacy." % (key.lower(), os.path.relpath(os.path.join(dp, fn), OUT)))
    # report unfilled placeholders
    left = {}
    for dp, _, fns in os.walk(OUT):
        for fn in fns:
            if fn.endswith(".html"):
                for m in re.findall(r"\[([A-Z][A-Z0-9 _]{3,})\]", read(os.path.join(dp, fn))):
                    if m not in ph:
                        continue  # fill-in text inside prompts, not a site placeholder
                    left.setdefault(m, set()).add(os.path.relpath(os.path.join(dp, fn), OUT))
    print("Built", os.path.relpath(OUT, ROOT), "| live version:", live, "| blog articles:", len(items))
    if left:
        print("Placeholders still to fill in (edit launch-kit/sales-site/placeholders.json, then rebuild):")
        for k, v in sorted(left.items()):
            print("  [%s]  in %s" % (k, ", ".join(sorted(v))[:120]))
    else:
        print("All placeholders filled.")


if __name__ == "__main__":
    main()
