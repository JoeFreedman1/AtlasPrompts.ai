"""Render ready-to-upload images for every post and pin.

Run:  python3 launch-kit/tools/build_post_images.py

Makes launch-kit/marketing/ready-to-post/:
  P01/ ... P60/    slide-01.png ... (1080 x 1350, one per slide) + caption.txt
  PIN01/ ... PIN30/ pin.png (1000 x 1500) + caption.txt
  slide-text.txt   every word that appears on an image (for spelling checks)
  first-14-days.zip  the posts and pins for calendar days 1 to 14
Carousel posts use their slide-by-slide script. Video posts use their
on-screen text, one slide per line, so they can be posted as a slideshow
or dropped into CapCut under the voiceover.
Text is auto-fitted: if any slide still overflows at the smallest size,
the script reports it and exits with an error.
"""
import csv
import html
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
KIT = os.path.abspath(os.path.join(HERE, ".."))
OUT = os.path.join(KIT, "marketing", "ready-to-post")
sys.path.insert(0, HERE)
import build_dashboard as bd  # noqa: E402

SITE = "well-listed.netlify.app"


def clean(t):
    t = t.strip().strip('"').strip()
    t = t.replace("’", "'").replace("‘", "'")
    return re.sub(r"\s+", " ", t)


def carousel_slides(script):
    slides = []
    for line in script.split("\n"):
        m = re.match(r'^\s*\d+\.\s*Slide \d+[^:]*:\s*(.*)$', line)
        if not m:
            continue
        rest = m.group(1)
        small = ""
        sm = re.search(r'Small text:\s*"(.*?)"', rest)
        if sm:
            small = sm.group(1)
            rest = rest[:sm.start()]
        quotes = re.findall(r'"(.*?)"', rest)
        main = " ".join(quotes) if quotes else re.sub(r"\([^)]*\)", "", rest)
        slides.append({"text": clean(main), "small": clean(small)})
    return slides


def onscreen_slides(onscreen):
    return [{"text": clean(l), "small": ""} for l in onscreen.split("\n") if l.strip()]


def post_slides(p):
    s = carousel_slides(p["script"])
    return s if len(s) >= 3 else onscreen_slides(p["onscreen"])


CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{width:W;height:H;overflow:hidden;font-family:'Liberation Sans',Arial,sans-serif;font-stretch:normal;background:#FAF6EF;color:#1F2A44}
.page{position:relative;width:W;height:H;padding:90px 80px 120px;display:flex;flex-direction:column}
.brand{font-weight:700;font-size:42px;letter-spacing:.5px;display:flex;align-items:center;gap:10px}
.brand i{color:#1E7F55;font-style:normal}
.box{flex:1;display:flex;flex-direction:column;justify-content:center;overflow:hidden;margin-top:40px}
.t{font-weight:700;line-height:1.18;overflow-wrap:break-word}
.s{margin-top:34px;color:#5b6478;line-height:1.3}
.label{background:#fff;border:6px solid #C9A27E;outline:4px dashed #C9A27E;outline-offset:14px;border-radius:28px;padding:64px 56px}
.chip{display:inline-block;font-weight:700;font-size:40px;padding:8px 22px;border-radius:12px;margin-bottom:26px;color:#fff}
.before .chip{background:#C4453B}.before .t{color:#6b7280}
.after .chip{background:#1E7F55}
.num{color:#1E7F55}
.foot{position:absolute;left:80px;right:80px;bottom:56px;display:flex;justify-content:space-between;font-size:32px;color:#5b6478}
.dark{background:#1F2A44;color:#FAF6EF}.dark .brand,.dark .t{color:#FAF6EF}.dark .foot{color:#C9A27E}.dark .s{color:#F2C84B}
.hl{background:#F2C84B;padding:0 8px;border-radius:6px;color:#1F2A44}
.swipe{color:#1E7F55;font-weight:700}
.pin .t{font-size:0}
"""


def mark(text):
    """Escape, highlight [CHECK...] tags and a leading list number."""
    t = html.escape(text)
    t = re.sub(r"(\[CHECK[^\]]*\])", r'<span class="hl">\1</span>', t)
    t = re.sub(r"^(\d+\.)\s", r'<span class="num">\1</span> ', t)
    return t


def slide_html(slide, i, n, w, h, kind="post"):
    text = slide["text"]
    cls, chip = "", ""
    m = re.match(r"^(Before|After)\s*:\s*(.*)$", text, re.I)
    if m:
        cls = m.group(1).lower()
        chip = '<span class="chip">%s</span>' % m.group(1).capitalize()
        text = m.group(2)
    first, last = i == 0, i == n - 1
    page_cls = "dark" if (last and n > 1) else ""
    body = '<div class="t" data-fit>%s</div>' % mark(text)
    if slide["small"]:
        body += '<div class="s" data-small>%s</div>' % html.escape(slide["small"])
    inner = '<div class="%s">%s%s</div>' % (cls, chip, body)
    if first:
        inner = '<div class="label">%s%s</div>' % (chip, body) if not cls else '<div class="label %s">%s%s</div>' % (cls, chip, body)
    foot_right = "%d / %d" % (i + 1, n) if n > 1 else ""
    if first and n > 1:
        foot_right = '<span class="swipe">Swipe &rarr;</span> &nbsp; ' + foot_right
    foot_left = SITE if last else "Well Listed"
    css = CSS.replace("W", "%dpx" % w).replace("H", "%dpx" % h)
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>
<div class="page {page_cls}"><div class="brand">Well Listed <i>&#10003;</i></div>
<div class="box">{inner}</div>
<div class="foot"><span>{foot_left}</span><span>{foot_right}</span></div></div></body></html>"""


def pin_html(pin, w=1000, h=1500):
    sub = re.split(r"(?<=[.!?])\s", pin["description"])[0]
    css = CSS.replace("W", "%dpx" % w).replace("H", "%dpx" % h)
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{css}
.page{{padding:90px 70px 130px}}</style></head><body>
<div class="page"><div class="brand">Well Listed <i>&#10003;</i></div>
<div class="box"><div class="label"><div class="t" data-fit>{mark(pin["title"])}</div>
<div class="s" data-small>{html.escape(sub)}</div></div></div>
<div class="foot"><span>{SITE}</span><span class="swipe">Free UK Listing Cheat Sheet</span></div></div></body></html>"""


FIT_JS = r"""
() => {
  const box = document.querySelector('.box');
  const t = document.querySelector('[data-fit]');
  const s = document.querySelector('[data-small]');
  const first = !!document.querySelector('.label');
  let size = first ? 96 : 88, min = 34;
  const fits = () => box.scrollHeight <= box.clientHeight + 1 && t.scrollWidth <= t.clientWidth + 1
      && [...document.querySelectorAll('.t,.s,.label')].every(e => e.scrollWidth <= e.clientWidth + 1);
  while (size >= min) {
    t.style.fontSize = size + 'px';
    if (s) s.style.fontSize = Math.max(28, Math.round(size * 0.5)) + 'px';
    if (fits()) return {ok: true, size};
    size -= 2;
  }
  return {ok: false, size};
}
"""

NODE = r"""
const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const jobs=JSON.parse(fs.readFileSync(process.argv[1],'utf8'));const b=await chromium.launch();
const results=[];const pages={};
for(const j of jobs){const key=j.w+'x'+j.h;if(!pages[key]){pages[key]=await b.newPage({viewport:{width:j.w,height:j.h}})}
const p=pages[key];await p.setContent(j.html,{waitUntil:'load'});
const r=await p.evaluate(eval(process.argv[2]));await p.screenshot({path:j.out});results.push({out:j.out,...r});}
await b.close();fs.writeFileSync(process.argv[3],JSON.stringify(results));})();
"""


def render(jobs):
    tmp = os.path.join(OUT, "_jobs.json")
    res = os.path.join(OUT, "_results.json")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(jobs, f)
    env = dict(os.environ, NODE_PATH="/opt/node22/lib/node_modules")
    subprocess.run(["node", "-e", NODE, tmp, FIT_JS, res], check=True, env=env, timeout=1800)
    with open(res, encoding="utf-8") as f:
        results = json.load(f)
    os.remove(tmp)
    os.remove(res)
    return results


def main():
    posts = bd.parse_posts()
    pins = bd.parse_pins()
    if os.path.isdir(OUT):
        for d in os.listdir(OUT):
            if re.match(r"^(P|PIN)\d+$", d):
                shutil.rmtree(os.path.join(OUT, d))
    os.makedirs(OUT, exist_ok=True)
    jobs, texts = [], []
    for pid in sorted(posts, key=lambda x: int(x[1:])):
        p = posts[pid]
        d = os.path.join(OUT, pid)
        os.makedirs(d, exist_ok=True)
        slides = post_slides(p)
        with open(os.path.join(d, "caption.txt"), "w", encoding="utf-8") as f:
            f.write(p["caption"].strip() + "\n\n" + p["hashtags"].strip() + "\n")
        for i, s in enumerate(slides):
            out = os.path.join(d, "slide-%02d.png" % (i + 1))
            jobs.append({"html": slide_html(s, i, len(slides), 1080, 1350), "out": out, "w": 1080, "h": 1350})
            texts.append("%s slide %d: %s%s" % (pid, i + 1, s["text"], (" | " + s["small"]) if s["small"] else ""))
    for pid in sorted(pins, key=lambda x: int(x[3:])):
        pin = pins[pid]
        d = os.path.join(OUT, pid)
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "caption.txt"), "w", encoding="utf-8") as f:
            f.write("TITLE:\n%s\n\nDESCRIPTION:\n%s\n\nLINK:\nhttps://%s%s\n\nBOARD:\n%s\n" % (
                pin["title"], pin["description"], SITE, pin["link"], pin["board"]))
        jobs.append({"html": pin_html(pin), "out": os.path.join(d, "pin.png"), "w": 1000, "h": 1500})
        texts.append("%s: %s | %s" % (pid, pin["title"], re.split(r"(?<=[.!?])\s", pin["description"])[0]))
    results = render(jobs)
    bad = [r for r in results if not r["ok"]]
    with open(os.path.join(OUT, "slide-text.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(texts) + "\n")
    # zip of calendar days 1 to 14
    ids = []
    with open(os.path.join(KIT, "marketing", "a-content-calendar", "calendar.csv"), encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if int(r["day"]) <= 14 and re.match(r"^(P|PIN)\d+$", r["item"] or ""):
                ids.append((int(r["day"]), r["slot"], r["item"]))
    z = os.path.join(OUT, "first-14-days.zip")
    with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
        for day, slot, item in ids:
            folder = os.path.join(OUT, item)
            for fn in sorted(os.listdir(folder)):
                zf.write(os.path.join(folder, fn), "day-%02d-%s-%s/%s" % (day, slot, item, fn))
    print("Images:", len(results), "| overflow failures:", len(bad), "| zip items:", len(ids))
    for r in bad:
        print("  OVERFLOW:", os.path.relpath(r["out"], KIT))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
