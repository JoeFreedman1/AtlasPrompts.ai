"""Build the sellable Well Listed Kit from the markdown source files.

Run from anywhere:  python3 launch-kit/product/build.py
Makes, in launch-kit/product/dist/:
  Well-Listed-Kit.html      the full guide as one web page (print-ready)
  Well-Listed-Kit.pdf       the full guide as a PDF (needs Chromium + Playwright)
  prompt-library.html       searchable prompt library with copy buttons (works offline)
  all-prompts.txt           every prompt as plain text
  Well-Listed-Kit.zip       everything the buyer downloads, in one file
"""
import datetime
import html
import json
import os
import re
import subprocess
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "tools"))
import mdlite  # noqa: E402

SRC = os.path.join(HERE, "source")
TPL = os.path.join(HERE, "templates")
DIST = os.path.join(HERE, "dist")
VERSION = "1.0"
TODAY = datetime.date.today().strftime("%B %Y")

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@700;800&family=Inter:wght@400;600&family=JetBrains+Mono&display=swap" rel="stylesheet">')

BASE_CSS = """
:root{--ink:#1F2A44;--cream:#FAF6EF;--kraft:#C9A27E;--green:#1E7F55;--yellow:#F2C84B;--red:#C4453B;--card:#fff;--muted:#5b6478;--line:#e6dccd}
*{box-sizing:border-box}
body{margin:0;background:var(--cream);color:var(--ink);font:16px/1.6 Inter,system-ui,sans-serif}
h1,h2,h3,h4{font-family:Archivo,Inter,sans-serif;line-height:1.2;color:var(--ink)}
h1{font-weight:800;font-size:2rem}h2{font-weight:800;font-size:1.5rem;margin-top:2.2rem;padding-bottom:.3rem;border-bottom:3px solid var(--kraft)}
h3{font-weight:700;font-size:1.15rem;margin-top:1.8rem}
a{color:var(--green)}
code{font-family:'JetBrains Mono',monospace;font-size:.88em;background:#f1eadf;padding:.1em .3em;border-radius:4px}
pre{background:#fff;border:1px solid var(--line);border-left:5px solid var(--green);border-radius:8px;padding:14px;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word}
pre code{background:none;padding:0;font-size:.85rem;line-height:1.5}
blockquote{margin:1rem 0;padding:.6rem 1rem;background:#fff8e1;border-left:5px solid var(--yellow);border-radius:6px}
.table-wrap{overflow-x:auto}
table{border-collapse:collapse;width:100%;margin:1rem 0;background:#fff;font-size:.9rem}
th,td{border:1px solid var(--line);padding:6px 8px;text-align:left;vertical-align:top}
th{background:var(--ink);color:var(--cream)}
hr{border:none;border-top:2px dashed var(--kraft);margin:2rem 0}
"""


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def modules():
    files = sorted(f for f in os.listdir(SRC) if re.match(r"^\d\d-.*\.md$", f))
    return [(f, read(os.path.join(SRC, f))) for f in files]


PROMPT_HEAD = re.compile(r"^#{3,4}\s+\[?([A-Z]{1,2})[- ]?(\d{1,3})\]?[.:)]?\s+(.*)$")


def extract_prompts(mods):
    prompts = []
    for fname, text in mods:
        title_m = re.search(r"^#\s+(.*)$", text, re.M)
        module_title = title_m.group(1).strip() if title_m else fname
        lines = text.split("\n")
        i = 0
        while i < len(lines):
            m = PROMPT_HEAD.match(lines[i].strip())
            if not m:
                i += 1
                continue
            pid = "%s%s" % (m.group(1), m.group(2).zfill(2))
            name = re.sub(r"[*_`]", "", m.group(3)).strip()
            j = i + 1
            use = ""
            body = None
            while j < len(lines) and not re.match(r"^#{1,4}\s", lines[j]):
                ln = lines[j]
                um = re.match(r"^\*\*Use it when:?\*\*:?\s*(.*)$", ln.strip())
                if um and not use:
                    use = um.group(1).strip()
                    use = use[:1].upper() + use[1:]
                if body is None and re.match(r"^\s*```", ln):
                    k = j + 1
                    buf = []
                    while k < len(lines) and not re.match(r"^\s*```", lines[k]):
                        buf.append(lines[k])
                        k += 1
                    body = "\n".join(buf).strip("\n")
                    j = k
                j += 1
            if body:
                prompts.append({"id": pid, "name": name, "use": use, "prompt": body,
                                "module": module_title, "file": fname})
            i = j
    return prompts


def build_guide(mods, prompts):
    toc = []
    parts = []
    for fname, text in mods:
        t = re.search(r"^#\s+(.*)$", text, re.M)
        title = t.group(1).strip() if t else fname
        anchor = "m-" + fname[:2]
        toc.append('<li><a href="#%s">%s</a></li>' % (anchor, html.escape(title)))
        body = mdlite.convert(text)
        parts.append('<section class="module" id="%s">%s</section>' % (anchor, body))
    cover = f"""
<section class="cover">
  <div class="label">
    <div class="brand">Well Listed<span class="tick">&#10003;</span></div>
    <h1>The Well Listed Kit</h1>
    <p class="sub">AI prompts, templates and checklists for UK sellers on eBay, Vinted, Depop, Etsy, Amazon and TikTok Shop</p>
    <p class="meta">{len(prompts)} prompts with worked examples &middot; Version {VERSION} &middot; {TODAY}</p>
  </div>
  <p class="small">Works with the free versions of ChatGPT, Claude, Gemini and Microsoft Copilot. Not affiliated with or endorsed by eBay, Vinted, Depop, Etsy, Amazon or TikTok. Platform rules change: always check the platform's own help pages. Nothing in this kit is legal, tax or financial advice. For your own use; please do not resell or share the files.</p>
</section>
<section class="toc"><h2>Contents</h2><ol>{''.join(toc)}</ol>
<p>Prefer copying prompts on your phone? Open <strong>prompt-library.html</strong> from your download: every prompt has a copy button and a search box.</p></section>
"""
    css = BASE_CSS + """
.wrap{max-width:820px;margin:0 auto;padding:24px 18px 60px}
.cover{min-height:92vh;display:flex;flex-direction:column;justify-content:center}
.label{background:#fff;border:3px solid var(--kraft);border-radius:14px;padding:36px 28px;outline:2px dashed var(--kraft);outline-offset:8px}
.brand{font-family:Archivo;font-weight:800;font-size:1.2rem}.tick{color:var(--green);margin-left:4px}
.cover h1{font-size:2.6rem;margin:.6rem 0}
.sub{font-size:1.15rem}.meta{color:var(--muted)}.small{font-size:.8rem;color:var(--muted);margin-top:2rem}
.module{page-break-before:always}
@media print{body{background:#fff}.wrap{padding:0}pre{page-break-inside:avoid}h2,h3{page-break-after:avoid}a{color:var(--ink)}}
"""
    page = f"""<!doctype html><html lang="en-GB"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>The Well Listed Kit</title>{FONTS}<style>{css}</style></head>
<body><div class="wrap">{cover}{''.join(parts)}</div></body></html>"""
    out = os.path.join(DIST, "Well-Listed-Kit.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(page)
    return out


def build_library(prompts):
    data = json.dumps(prompts, ensure_ascii=False).replace("</", "<\\/")
    modules_list = []
    for p in prompts:
        if p["module"] not in modules_list:
            modules_list.append(p["module"])
    css = BASE_CSS + """
header{position:sticky;top:0;background:var(--ink);color:var(--cream);padding:12px 16px;z-index:5}
header h1{color:var(--cream);font-size:1.15rem;margin:0 0 8px}
header .tick{color:var(--yellow)}
#q{width:100%;padding:10px 12px;border-radius:8px;border:none;font-size:16px}
#mods{display:flex;gap:6px;overflow-x:auto;padding:10px 16px;background:#efe6d8}
#mods button{flex:none;border:1px solid var(--kraft);background:#fff;border-radius:20px;padding:6px 12px;font:600 .8rem Inter;color:var(--ink)}
#mods button.on{background:var(--green);color:#fff;border-color:var(--green)}
main{max-width:820px;margin:0 auto;padding:12px 16px 60px}
.card{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px;margin:12px 0}
.card h3{margin:0 0 4px;font-size:1.02rem}.id{display:inline-block;background:var(--yellow);border-radius:5px;padding:0 6px;margin-right:6px;font:700 .8rem 'JetBrains Mono'}
.use{color:var(--muted);font-size:.9rem;margin:0 0 8px}.mod{font-size:.75rem;color:var(--muted)}
.copy{background:var(--green);color:#fff;border:none;border-radius:8px;padding:9px 14px;font:600 .9rem Inter;cursor:pointer}
.copy.done{background:var(--ink)}
.count{font-size:.85rem;color:var(--muted)}
.card pre{max-height:9.5em;overflow:hidden;position:relative;margin-bottom:8px}
.card.open pre{max-height:none}
.more{background:none;border:1px solid var(--kraft);border-radius:8px;padding:8px 12px;font:600 .85rem Inter;color:var(--ink);margin-left:6px;cursor:pointer}
"""
    buttons = '<button class="on" data-m="">All</button>' + "".join(
        '<button data-m="%s">%s</button>' % (html.escape(m, quote=True), html.escape(re.sub(r"^(Module\s+)?\d+[.:]?\s*", "", m))) for m in modules_list)
    js = """
const P=%s;let mod="";const q=document.getElementById('q'),list=document.getElementById('list'),cnt=document.getElementById('cnt');
function esc(s){return s.replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]))}
function render(){const t=q.value.toLowerCase().trim();const f=P.filter(p=>(!mod||p.module===mod)&&(!t||(p.id+' '+p.name+' '+p.use+' '+p.prompt).toLowerCase().includes(t)));
cnt.textContent=f.length+' prompt'+(f.length==1?'':'s');
list.innerHTML=f.map((p,i)=>`<div class="card"><div class="mod">${esc(p.module)}</div><h3><span class="id">${p.id}</span>${esc(p.name)}</h3>${p.use?`<p class="use">${esc(p.use)}</p>`:''}<pre><code>${esc(p.prompt)}</code></pre><button class="copy" data-i="${P.indexOf(p)}">Copy prompt</button><button class="more">Show full prompt</button></div>`).join('');}
list.addEventListener('click',e=>{const m=e.target.closest('.more');if(m){const c=m.closest('.card');c.classList.toggle('open');m.textContent=c.classList.contains('open')?'Show less':'Show full prompt';return}const b=e.target.closest('.copy');if(!b)return;const txt=P[+b.dataset.i].prompt;
const ok=()=>{b.textContent='Copied';b.classList.add('done');setTimeout(()=>{b.textContent='Copy prompt';b.classList.remove('done')},1500)};
if(navigator.clipboard&&window.isSecureContext){navigator.clipboard.writeText(txt).then(ok,()=>fallback(txt,ok))}else fallback(txt,ok)});
function fallback(txt,ok){const a=document.createElement('textarea');a.value=txt;document.body.appendChild(a);a.select();try{document.execCommand('copy');ok()}catch(e){alert('Press and hold the prompt text to copy it.')}a.remove()}
document.getElementById('mods').addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;mod=b.dataset.m;document.querySelectorAll('#mods button').forEach(x=>x.classList.toggle('on',x===b));render()});
q.addEventListener('input',render);render();
""" % data
    page = f"""<!doctype html><html lang="en-GB"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Well Listed Prompt Library</title>{FONTS}<style>{css}</style></head>
<body><header><h1>Well Listed<span class="tick"> &#10003;</span> Prompt Library</h1>
<input id="q" type="search" placeholder="Search prompts, e.g. lowball, eBay title, bundle" aria-label="Search prompts"></header>
<nav id="mods">{buttons}</nav>
<main><p class="count" id="cnt"></p><div id="list"></div>
<p class="use">Tip: fill in the [SQUARE BRACKETS] before you send a prompt. Never paste a buyer's name, address or order details into an AI tool. Not affiliated with or endorsed by any marketplace. Version {VERSION}.</p></main>
<script>{js}</script></body></html>"""
    out = os.path.join(DIST, "prompt-library.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(page)
    return out


def build_txt(prompts):
    out = os.path.join(DIST, "all-prompts.txt")
    with open(out, "w", encoding="utf-8") as f:
        f.write("THE WELL LISTED KIT: ALL PROMPTS (version %s)\n" % VERSION)
        f.write("Fill in the [SQUARE BRACKETS] before sending. Never paste buyers' personal details into AI tools.\n\n")
        cur = None
        for p in prompts:
            if p["module"] != cur:
                cur = p["module"]
                f.write("\n" + "=" * 60 + "\n" + cur.upper() + "\n" + "=" * 60 + "\n\n")
            f.write("[%s] %s\n" % (p["id"], p["name"]))
            if p["use"]:
                f.write("Use it when: %s\n" % p["use"])
            f.write("-" * 40 + "\n" + p["prompt"] + "\n\n")
    return out


def build_pdf(html_path):
    pdf = os.path.join(DIST, "Well-Listed-Kit.pdf")
    script = r"""
const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+process.argv[1],{waitUntil:'load'});
try{await p.waitForLoadState('networkidle',{timeout:8000})}catch(e){}
await p.pdf({path:process.argv[2],format:'A4',printBackground:true,margin:{top:'16mm',bottom:'18mm',left:'14mm',right:'14mm'},
displayHeaderFooter:true,headerTemplate:'<span></span>',
footerTemplate:'<div style="font-size:8px;width:100%;text-align:center;color:#5b6478">The Well Listed Kit &middot; page <span class="pageNumber"></span> of <span class="totalPages"></span></div>'});
await b.close();})();
"""
    env = dict(os.environ, NODE_PATH="/opt/node22/lib/node_modules")
    try:
        subprocess.run(["node", "-e", script, html_path, pdf], check=True, env=env, timeout=180)
        return pdf
    except Exception as e:  # PDF is optional if Chromium is missing
        print("PDF step skipped:", e)
        return None


def build_zip(files):
    z = os.path.join(DIST, "Well-Listed-Kit.zip")
    with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in files:
            if path and os.path.exists(path):
                zf.write(path, "Well-Listed-Kit/" + os.path.basename(path))
        for t in sorted(os.listdir(TPL)):
            zf.write(os.path.join(TPL, t), "Well-Listed-Kit/templates/" + t)
        readme = os.path.join(HERE, "READ-ME-FIRST.txt")
        if os.path.exists(readme):
            zf.write(readme, "Well-Listed-Kit/READ-ME-FIRST.txt")
    return z


def main():
    os.makedirs(DIST, exist_ok=True)
    mods = modules()
    prompts = extract_prompts(mods)
    ids = [p["id"] for p in prompts]
    dupes = sorted({i for i in ids if ids.count(i) > 1})
    guide = build_guide(mods, prompts)
    lib = build_library(prompts)
    txt = build_txt(prompts)
    pdf = build_pdf(guide) if "--no-pdf" not in sys.argv else None
    z = build_zip([pdf, lib, txt])
    print("Modules:", len(mods), "| Prompts:", len(prompts), "| Duplicate IDs:", dupes or "none")
    for p in (guide, lib, txt, pdf, z):
        if p:
            print(" ", os.path.relpath(p, os.path.join(HERE, "..", "..")))


if __name__ == "__main__":
    main()
