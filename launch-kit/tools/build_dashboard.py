"""Build launch-kit/dashboard.html: the Well Listed mission control page.

Run:  python3 launch-kit/tools/build_dashboard.py

It reads (all optional except the calendar):
  STATE.md                                   launch date, price, links
  launch-kit/marketing/a-content-calendar/calendar.csv
  launch-kit/marketing/b-short-form-posts/*.md   (P01 to P60 and any new posts)
  launch-kit/marketing/c-pinterest/pins.md
  launch-kit/marketing/d-blog/*.md
  launch-kit/marketing/e-email/*.md
  launch-kit/LAUNCH.md                       the launch checklist
  launch-kit/metrics/YYYY-MM.csv             the latest numbers
  launch-kit/daily/YYYY-MM-DD.md             the latest daily plan from OPERATOR.md
and writes one self-contained HTML file that works offline on a phone.
"""
import csv
import datetime
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
KIT = os.path.abspath(os.path.join(HERE, ".."))
ROOT = os.path.abspath(os.path.join(KIT, ".."))
sys.path.insert(0, HERE)
import mdlite  # noqa: E402


def read(path, default=""):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except OSError:
        return default


def code_block_after(text, heading):
    m = re.search(r"^###\s+%s\s*\n(.*?)(?=^###\s|^##\s|\Z)" % re.escape(heading), text, re.S | re.M)
    if not m:
        return ""
    body = m.group(1).strip()
    cb = re.search(r"```[\w-]*\n(.*?)\n```", body, re.S)
    return (cb.group(1) if cb else body).strip()


def field(text, name):
    m = re.search(r"^- \*\*%s:\*\*\s*(.*)$" % re.escape(name), text, re.M)
    return m.group(1).strip() if m else ""


def parse_posts():
    posts = {}
    for path in sorted(glob.glob(os.path.join(KIT, "marketing", "b-short-form-posts", "*.md"))):
        text = read(path)
        for m in re.finditer(r"^## (P\d+):\s*(.+?)\n(.*?)(?=^## P\d+:|\Z)", text, re.S | re.M):
            pid, title, body = m.group(1), m.group(2).strip(), m.group(3)
            hook = re.search(r"^\*\*Hook \(first 2 seconds\):\*\*\s*(.*)$", body, re.M)
            posts[pid] = {
                "id": pid, "title": title,
                "format": field(body, "Format"), "best": field(body, "Best on"),
                "length": field(body, "Length"), "cta": field(body, "Call to action"),
                "hook": hook.group(1).strip() if hook else "",
                "script": code_block_after(body, "Script"),
                "onscreen": code_block_after(body, "On-screen text"),
                "caption": code_block_after(body, "Caption"),
                "hashtags": code_block_after(body, "Hashtags"),
                "visuals": code_block_after(body, "Visuals"),
                "file": os.path.relpath(path, ROOT),
            }
    return posts


def parse_pins():
    pins = {}
    text = read(os.path.join(KIT, "marketing", "c-pinterest", "pins.md"))
    for m in re.finditer(r"^## (PIN\d+):\s*(.+?)\n(.*?)(?=^## PIN\d+:|\Z)", text, re.S | re.M):
        body = m.group(3)
        pins[m.group(1)] = {"id": m.group(1), "title": field(body, "Title") or m.group(2).strip(),
                            "description": field(body, "Description"), "board": field(body, "Board"),
                            "link": field(body, "Link"), "design": field(body, "Design")}
    return pins


def parse_blog():
    posts = {}
    for path in sorted(glob.glob(os.path.join(KIT, "marketing", "d-blog", "B*.md"))):
        text = read(path)
        bid = os.path.basename(path)[:3]
        t = re.search(r"^title:\s*(.+)$", text, re.M)
        s = re.search(r"^slug:\s*(.+)$", text, re.M)
        posts[bid] = {"id": bid, "title": t.group(1).strip() if t else bid,
                      "slug": s.group(1).strip() if s else "", "file": os.path.relpath(path, ROOT)}
    return posts


def parse_calendar():
    rows = []
    with open(os.path.join(KIT, "marketing", "a-content-calendar", "calendar.csv"), encoding="utf-8") as f:
        for r in csv.DictReader(f):
            r["day"] = int(r["day"])
            rows.append(r)
    return rows


def parse_launch():
    steps = []
    part = ""
    cur = None
    for line in read(os.path.join(KIT, "LAUNCH.md")).split("\n"):
        h = re.match(r"^###\s+(.*)$", line)
        if h or re.match(r"^---", line):
            cur = None
            if h:
                part = h.group(1).strip()
            continue
        m = re.match(r"^(\d+)\.\s+\*\*(.+?)\s*\((\d+)\s*min\)\.?\*\*\s*(.*)$", line)
        if m:
            cur = {"n": int(m.group(1)), "title": m.group(2).strip(), "mins": int(m.group(3)),
                   "md": [m.group(4).strip()], "part": part}
            steps.append(cur)
        elif cur is not None and line.startswith("   "):
            cur["md"].append(line[3:])
        elif cur is not None and line.strip() == "":
            continue
        else:
            cur = None
    for st in steps:
        st["detail"] = mdlite.convert("\n".join(st.pop("md")), heading_ids=False)
    return steps


def parse_state():
    text = read(os.path.join(ROOT, "STATE.md"))

    def cell(name):
        m = re.search(r"^\|\s*%s\s*\|\s*(.*?)\s*\|" % re.escape(name), text, re.M | re.I)
        v = m.group(1).strip() if m else ""
        return "" if v.lower() in ("", "-", "blank", "not set", "(blank)") or v.startswith("_") else v

    return {"launch_date": cell("Launch date"), "price": cell("Current price"),
            "site": cell("Sales page address"), "gumroad": cell("Gumroad link")}


def parse_metrics():
    files = sorted(f for f in glob.glob(os.path.join(KIT, "metrics", "[0-9][0-9][0-9][0-9]-[0-9][0-9].csv")))
    rows = []
    for path in files:
        with open(path, encoding="utf-8") as f:
            for r in csv.DictReader(f):
                if r.get("date"):
                    rows.append(r)
    rows.sort(key=lambda r: r["date"])
    return rows[-28:]


def latest_plan():
    plans = sorted(glob.glob(os.path.join(KIT, "daily", "[0-9]*.md")))
    if not plans:
        return None
    path = plans[-1]
    text = read(path)
    todo = []
    m = re.search(r"^## Owner's to-do.*?\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    if m:
        for line in m.group(1).split("\n"):
            lm = re.match(r"^\s*(?:[-*]|\d+[.)])\s+(?:\[[ xX]\]\s+)?(.*)$", line)
            if lm and lm.group(1).strip():
                todo.append(lm.group(1).strip())
    return {"date": os.path.basename(path)[:10], "html": mdlite.convert(text), "todo": todo}


DEFAULT_TASKS = [
    "Add yesterday's numbers to metrics (5 min)",
    "Type \"Run OPERATOR.md\" in Claude Code and read the plan (3 min)",
    "Make and post Slot A to TikTok, Reels and Shorts (10 min)",
    "Schedule Slot B for 19:30 and today's pin for 12:00 (5 min)",
    "Reply to every comment and message on the brand accounts (5 min)",
    "Tick off today and note any good questions for future posts (2 min)",
]


def main():
    data = {
        "built": datetime.datetime.now().strftime("%d %B %Y, %H:%M"),
        "state": parse_state(), "calendar": parse_calendar(), "posts": parse_posts(),
        "pins": parse_pins(), "blog": parse_blog(), "launch": parse_launch(),
        "metrics": parse_metrics(), "plan": latest_plan(), "default_tasks": DEFAULT_TASKS,
    }
    js_data = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    html = TEMPLATE.replace("/*DATA*/", js_data)
    out = os.path.join(KIT, "dashboard.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print("Wrote", os.path.relpath(out, ROOT), "| posts:", len(data["posts"]), "| pins:", len(data["pins"]),
          "| blog:", len(data["blog"]), "| launch steps:", len(data["launch"]), "| metric rows:", len(data["metrics"]),
          "| plan:", data["plan"]["date"] if data["plan"] else "none")


TEMPLATE = r"""<!doctype html>
<html lang="en-GB"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex">
<title>Well Listed Mission Control</title>
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='12' fill='%23FAF6EF'/%3E%3Ctext x='8' y='42' font-family='Arial' font-weight='900' font-size='28' fill='%231F2A44'%3EWL%3C/text%3E%3Cpath d='M46 40l5 5 9-12' stroke='%231E7F55' stroke-width='5' fill='none'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@700;800&family=Inter:wght@400;600&family=JetBrains+Mono&display=swap" rel="stylesheet">
<style>
:root{--ink:#1F2A44;--cream:#FAF6EF;--kraft:#C9A27E;--green:#1E7F55;--yellow:#F2C84B;--red:#C4453B;--card:#fff;--muted:#5b6478;--line:#e6dccd;--bg:#FAF6EF}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--ink:#F3EEE6;--cream:#1F2A44;--card:#27334f;--muted:#b7bfd1;--line:#3a4764;--bg:#172036;--kraft:#b08a66}}
:root[data-theme="dark"]{--ink:#F3EEE6;--cream:#1F2A44;--card:#27334f;--muted:#b7bfd1;--line:#3a4764;--bg:#172036;--kraft:#b08a66}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 Inter,system-ui,sans-serif}
h1,h2,h3{font-family:Archivo,Inter,sans-serif;margin:0}
header{background:#1F2A44;color:#FAF6EF;padding:14px 16px 0;position:sticky;top:0;z-index:10}
.brand{font:800 1.1rem Archivo,sans-serif}.brand b{color:#F2C84B}
.sub{font-size:.85rem;opacity:.85;margin:2px 0 10px}
nav{display:flex;gap:4px;overflow-x:auto}
nav button{flex:none;background:none;border:none;color:#FAF6EF;opacity:.7;font:600 .9rem Inter,sans-serif;padding:10px 12px;border-bottom:3px solid transparent;cursor:pointer}
nav button.on{opacity:1;border-color:#F2C84B}
main{max-width:760px;margin:0 auto;padding:14px 16px 80px}
section{display:none}section.on{display:block}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px;margin:12px 0}
.label{border:2px solid var(--kraft);outline:1px dashed var(--kraft);outline-offset:3px}
.row{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
.pill{display:inline-block;background:var(--yellow);color:#1F2A44;border-radius:6px;padding:0 7px;font:700 .78rem 'JetBrains Mono',monospace}
.muted{color:var(--muted);font-size:.85rem}
.btn{background:var(--green);color:#fff;border:none;border-radius:8px;padding:9px 12px;font:600 .85rem Inter,sans-serif;cursor:pointer;min-height:40px}
.btn.alt{background:none;color:var(--ink);border:1px solid var(--kraft)}
.btn.done{background:#1F2A44;color:#fff}
.copies{display:flex;flex-wrap:wrap;gap:6px;margin-top:10px}
details{margin-top:8px}summary{cursor:pointer;font-weight:600;padding:6px 0}
pre{white-space:pre-wrap;word-wrap:break-word;background:var(--bg);border:1px solid var(--line);border-radius:8px;padding:10px;font:13px/1.5 'JetBrains Mono',monospace;margin:6px 0}
.task{display:flex;gap:10px;align-items:flex-start;padding:9px 0;border-bottom:1px solid var(--line)}
.task:last-child{border:none}.task input{width:22px;height:22px;flex:none;margin-top:1px;accent-color:#1E7F55}
.task.ticked span{text-decoration:line-through;opacity:.6}
.daynav{display:flex;justify-content:space-between;align-items:center;gap:8px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:8px}
.day{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px;cursor:pointer;font-size:.82rem}
.day.today{border:2px solid var(--green)}.day h3{font-size:.95rem;margin-bottom:4px}
.kpis{display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:8px}
.kpi{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px}
.kpi .v{font:800 1.5rem Archivo,sans-serif}.kpi .k{font-size:.8rem;color:var(--muted)}
table{border-collapse:collapse;width:100%;font-size:.8rem}th,td{border-bottom:1px solid var(--line);padding:6px 4px;text-align:right}th:first-child,td:first-child{text-align:left}
.tw{overflow-x:auto}
.det p{margin:4px 0}.det ul{margin:4px 0;padding-left:18px}.det code{font-size:.8em}
.plan h1{font-size:1.2rem}.plan h2{font-size:1rem;margin-top:14px}.plan ul{padding-left:18px}
.bar{height:10px;background:var(--line);border-radius:6px;overflow:hidden}.bar i{display:block;height:100%;background:var(--green)}
input[type=date]{font:inherit;padding:6px;border-radius:6px;border:1px solid var(--line);background:var(--card);color:var(--ink)}
#toast{position:fixed;bottom:18px;left:50%;transform:translateX(-50%);background:#1E7F55;color:#fff;padding:10px 16px;border-radius:20px;font-weight:600;opacity:0;transition:opacity .2s;pointer-events:none}
#toast.show{opacity:1}
</style></head>
<body>
<header>
  <div class="brand">Well Listed <b>&#10003;</b> Mission Control</div>
  <div class="sub" id="sub"></div>
  <nav id="tabs">
    <button data-t="today" class="on">Today</button>
    <button data-t="calendar">Calendar</button>
    <button data-t="launch">Launch</button>
    <button data-t="numbers">Numbers</button>
  </nav>
</header>
<main>
<section id="today" class="on"></section>
<section id="calendar"></section>
<section id="launch"></section>
<section id="numbers"></section>
<p class="muted" id="built"></p>
</main>
<div id="toast">Copied</div>
<script>
const D=/*DATA*/;
const store={get(k,d){try{const v=localStorage.getItem('wl:'+k);return v===null?d:JSON.parse(v)}catch(e){return d}},set(k,v){try{localStorage.setItem('wl:'+k,JSON.stringify(v))}catch(e){}}};
const esc=s=>String(s||'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const $=id=>document.getElementById(id);
const COPY=[];
function copyBtn(label,text){if(!text)return'';COPY.push(text);return `<button class="btn alt" data-copy="${COPY.length-1}">Copy ${esc(label)}</button>`}
function toast(t){const e=$('toast');e.textContent=t;e.classList.add('show');setTimeout(()=>e.classList.remove('show'),1300)}
document.addEventListener('click',e=>{const b=e.target.closest('[data-copy]');if(!b)return;const t=COPY[+b.dataset.copy];
 const ok=()=>{toast('Copied');b.classList.add('done');setTimeout(()=>b.classList.remove('done'),1200)};
 if(navigator.clipboard&&window.isSecureContext){navigator.clipboard.writeText(t).then(ok,()=>fb(t,ok))}else fb(t,ok)});
function fb(t,ok){const a=document.createElement('textarea');a.value=t;a.style.position='fixed';a.style.opacity='0';document.body.appendChild(a);a.focus();a.select();try{document.execCommand('copy');ok()}catch(e){alert('Could not copy. Press and hold the text to copy it.')}a.remove()}
document.getElementById('tabs').addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;
 document.querySelectorAll('nav button').forEach(x=>x.classList.toggle('on',x===b));
 document.querySelectorAll('section').forEach(s=>s.classList.toggle('on',s.id===b.dataset.t));store.set('tab',b.dataset.t);window.scrollTo(0,0)});

function launchDate(){return D.state.launch_date||store.get('launch_date','')}
function todayISO(){const d=new Date();return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0')}
function dayNumber(){const L=launchDate();if(!L)return 0;const a=new Date(L+'T00:00:00'),b=new Date(todayISO()+'T00:00:00');return Math.floor((b-a)/864e5)+1}
function dateForDay(n){const L=launchDate();if(!L)return'';const a=new Date(L+'T00:00:00');a.setDate(a.getDate()+n-1);return a.toLocaleDateString('en-GB',{weekday:'short',day:'numeric',month:'short'})}
const maxDay=Math.max(...D.calendar.map(r=>r.day));
let viewDay=null;

function postCard(slot,r){
 const p=D.posts[r.item];
 if(!p)return `<div class="card"><b>${esc(slot)}</b> ${esc(r.item)} <span class="muted">(script not found)</span></div>`;
 const both=(p.caption||'')+(p.hashtags?'\n\n'+p.hashtags:'');
 return `<div class="card label"><div class="row"><span class="pill">${esc(p.id)}</span><span class="muted">${esc(slot)} &middot; ${esc(r.time)} &middot; ${esc(r.platforms)}</span></div>
 <h3 style="margin:6px 0">${esc(p.title)}</h3><div class="muted">${esc(p.format)} &middot; ${esc(p.length)}</div>
 <p><b>Hook:</b> ${esc(p.hook)}</p>
 <div class="copies">${copyBtn('caption + hashtags',both)}${copyBtn('caption',p.caption)}${copyBtn('hashtags',p.hashtags)}${copyBtn('script',p.script)}${copyBtn('on-screen text',p.onscreen)}</div>
 <details><summary>Script</summary><pre>${esc(p.script)}</pre></details>
 <details><summary>On-screen text</summary><pre>${esc(p.onscreen)}</pre></details>
 <details><summary>Caption</summary><pre>${esc(p.caption)}</pre><pre>${esc(p.hashtags)}</pre></details>
 <details><summary>Visuals</summary><pre>${esc(p.visuals)}</pre></details>
 <p class="muted">${esc(r.notes)}</p></div>`}

function pinCard(r){const p=D.pins[r.item];if(!p)return `<div class="card"><b>Pin</b> ${esc(r.item)} <span class="muted">(not found)</span></div>`;
 return `<div class="card"><div class="row"><span class="pill">${esc(p.id)}</span><span class="muted">Pinterest &middot; ${esc(r.time)} &middot; board: ${esc(p.board)}</span></div>
 <h3 style="margin:6px 0">${esc(p.title)}</h3><p>${esc(p.description)}</p><p class="muted">Link: ${esc(p.link)}</p>
 <div class="copies">${copyBtn('title',p.title)}${copyBtn('description',p.description)}${copyBtn('link',p.link)}</div>
 <details><summary>Design</summary><pre>${esc(p.design)}</pre></details></div>`}

function otherCard(r){let t=r.notes;if(r.slot==='Blog'){const b=D.blog[r.item];t=`Publish ${esc(r.item)}: <b>${esc(b?b.title:'')}</b><br><span class="muted">${esc(b?b.file:'')}</span><br>${esc(r.notes)}`}else t=esc(t);
 return `<div class="card"><div class="row"><span class="pill">${esc(r.slot)}</span><span class="muted">${esc(r.time)} &middot; ${esc(r.platforms)}</span></div><p>${t}</p></div>`}

function renderToday(){
 COPY.length=0;
 const real=dayNumber();let d=viewDay??(real>=1?Math.min(real,maxDay):1);viewDay=d;
 const L=launchDate();
 let h='';
 if(!L){h+=`<div class="card label"><h2>Not launched yet</h2><p>Work through the <b>Launch</b> tab first. Below is a preview of Day 1. When you launch, set the date here (or tell Claude, and it goes in STATE.md).</p>
  <div class="row"><input type="date" id="ld"><button class="btn" id="setld">Set launch date</button></div></div>`}
 else if(real>maxDay){h+=`<div class="card"><p>Day ${real}: the first 30-day calendar is finished. Run OPERATOR.md so Claude builds the next month from what worked.</p></div>`}
 const key='tasks:'+todayISO();const ticked=store.get(key,{});
 const plan=D.plan&&D.plan.date===todayISO()?D.plan:null;
 const tasks=plan&&plan.todo.length?plan.todo:D.default_tasks;
 h+=`<div class="card"><h2>Today's tasks</h2><p class="muted">${plan?'From today\'s operator plan.':'Standard daily routine. Run OPERATOR.md for a plan based on your numbers.'}</p>`+
  tasks.map((t,i)=>`<label class="task ${ticked[i]?'ticked':''}"><input type="checkbox" data-task="${i}" ${ticked[i]?'checked':''}><span>${esc(t)}</span></label>`).join('')+`</div>`;
 if(plan)h+=`<details class="card"><summary>Today's full plan (${esc(plan.date)})</summary><div class="plan">${plan.html}</div></details>`;
 else if(D.plan)h+=`<p class="muted">Latest operator plan is from ${esc(D.plan.date)}. Run OPERATOR.md for today's.</p>`;
 h+=`<div class="daynav"><button class="btn alt" id="prev">&larr; Day ${d-1}</button><div style="text-align:center"><b>Day ${d}</b><br><span class="muted">${esc(dateForDay(d))}${d===real?' (today)':''}</span></div><button class="btn alt" id="next">Day ${d+1} &rarr;</button></div>`;
 const rows=D.calendar.filter(r=>r.day===d);
 rows.forEach(r=>{if(r.slot==='A'||r.slot==='B')h+=postCard('Slot '+r.slot,r);else if(r.slot==='Pin')h+=pinCard(r);else h+=otherCard(r)});
 $('today').innerHTML=h;
 $('prev').disabled=d<=1;$('next').disabled=d>=maxDay;
 $('prev').onclick=()=>{viewDay=Math.max(1,d-1);renderToday()};$('next').onclick=()=>{viewDay=Math.min(maxDay,d+1);renderToday()};
 const sl=$('setld');if(sl)sl.onclick=()=>{const v=$('ld').value;if(v){store.set('launch_date',v);viewDay=null;renderAll()}};
 $('today').querySelectorAll('[data-task]').forEach(cb=>cb.onchange=()=>{const t=store.get(key,{});t[cb.dataset.task]=cb.checked;store.set(key,t);cb.parentElement.classList.toggle('ticked',cb.checked)});
}

function renderCalendar(){
 const real=dayNumber();let h='<p class="muted">Tap a day to open its posts.</p><div class="grid">';
 for(let d=1;d<=maxDay;d++){const rows=D.calendar.filter(r=>r.day===d);
  const items=rows.map(r=>{if(r.slot==='A'||r.slot==='B'){const p=D.posts[r.item];return `<div><span class="pill">${esc(r.item)}</span> ${esc(p?p.title:'')}</div>`}
   if(r.slot==='Pin')return `<div class="muted">${esc(r.item)}</div>`;if(r.slot==='Blog')return `<div class="muted">Blog ${esc(r.item)}</div>`;return `<div class="muted">${esc(r.slot)}</div>`}).join('');
  h+=`<div class="day ${d===real?'today':''}" data-day="${d}"><h3>Day ${d}</h3><div class="muted">${esc(dateForDay(d))}</div>${items}</div>`}
 h+='</div>';$('calendar').innerHTML=h;
 $('calendar').querySelectorAll('[data-day]').forEach(el=>el.onclick=()=>{viewDay=+el.dataset.day;renderToday();document.querySelector('nav button[data-t=today]').click()});
}

function renderLaunch(){
 const t=store.get('launch',{});const total=D.launch.reduce((a,s)=>a+s.mins,0);const left=D.launch.filter(s=>!t[s.n]).reduce((a,s)=>a+s.mins,0);
 const done=D.launch.filter(s=>t[s.n]).length;
 let h=`<div class="card"><h2>Launch checklist</h2><p class="muted">${done} of ${D.launch.length} done &middot; about ${left} of ${total} minutes left. Full instructions: launch-kit/LAUNCH.md</p><div class="bar"><i style="width:${D.launch.length?Math.round(done*100/D.launch.length):0}%"></i></div>`;
 let part='';D.launch.forEach(s=>{if(s.part!==part){part=s.part;h+=`<h3 style="margin:14px 0 4px;font-size:.95rem">${esc(part)}</h3>`}
  h+=`<label class="task ${t[s.n]?'ticked':''}"><input type="checkbox" data-step="${s.n}" ${t[s.n]?'checked':''}><span><b>${s.n}. ${esc(s.title)}</b> <span class="muted">(${s.mins} min)</span><div class="muted det">${s.detail}</div></span></label>`});
 h+='</div>';$('launch').innerHTML=h;
 $('launch').querySelectorAll('[data-step]').forEach(cb=>cb.onchange=()=>{const t=store.get('launch',{});t[cb.dataset.step]=cb.checked;store.set('launch',t);renderLaunch()});
}

function num(v){const n=parseFloat(String(v||'').replace(/[£,]/g,''));return isNaN(n)?0:n}
function renderNumbers(){
 const M=D.metrics;if(!M.length){$('numbers').innerHTML=`<div class="card"><h2>No numbers yet</h2><p>After launch, add one row a day to <b>launch-kit/metrics/YYYY-MM.csv</b> (guide: metrics/HOW-TO-FILL-IN.md), then run OPERATOR.md. This page updates when Claude rebuilds it.</p></div>`;return}
 const last=M[M.length-1];const lastDate=last.date;const w=M.filter(r=>(new Date(lastDate)-new Date(r.date))/864e5<7);
 const sum=k=>w.reduce((a,r)=>a+num(r[k]),0);
 const views=r=>num(r.tiktok_views)+num(r.instagram_views)+num(r.youtube_shorts_views);
 const conv=sum('checkout_page_views')?(sum('sales_count')*100/sum('checkout_page_views')).toFixed(1)+'%':'n/a';
 const k=[['Sales yesterday',num(last.sales_count)],['Sales last 7 days',sum('sales_count')],['Revenue 7 days','£'+sum('revenue_gbp').toFixed(2)],['Checkout conversion (7d)',conv],
  ['Email sign-ups yesterday',num(last.email_signups_today)],['Subscribers',num(last.email_subscribers_total)||'n/a'],['Bio link clicks (7d)',sum('link_in_bio_clicks')],['Video views yesterday',views(last)],['Ad spend 7 days','£'+sum('ad_spend_gbp').toFixed(2)]];
 let h=`<div class="card"><h2>Key numbers</h2><p class="muted">Latest row: ${esc(lastDate)}</p><div class="kpis">`+k.map(x=>`<div class="kpi"><div class="v">${esc(x[1])}</div><div class="k">${esc(x[0])}</div></div>`).join('')+`</div></div>`;
 const cols=[['date','Date'],['sales_count','Sales'],['revenue_gbp','£'],['checkout_page_views','Checkout views'],['email_signups_today','Sign-ups'],['tiktok_views','TikTok'],['instagram_views','Insta'],['youtube_shorts_views','Shorts'],['pinterest_impressions','Pin impr.'],['ad_spend_gbp','Ad £']];
 h+=`<div class="card"><h2>Last ${M.length} days</h2><div class="tw"><table><tr>${cols.map(c=>`<th>${c[1]}</th>`).join('')}</tr>`+M.slice().reverse().map(r=>`<tr>${cols.map(c=>`<td>${esc(r[c[0]])}</td>`).join('')}</tr>`).join('')+`</table></div></div>`;
 $('numbers').innerHTML=h;
}

function renderAll(){
 const d=dayNumber();const L=launchDate();
 $('sub').textContent=L?(d>=1?`Day ${d}`+(d<=maxDay?` of ${maxDay}`:'')+` · launched ${L}`:`Launch day is ${L}`):'Pre-launch · start with the Launch tab';
 renderToday();renderCalendar();renderLaunch();renderNumbers();
 $('built').textContent='Page built '+D.built+'. Ticks are saved on this device only.';
}
renderAll();
const t0=store.get('tab','today');if(t0!=='today'){const b=document.querySelector(`nav button[data-t=${t0}]`);if(b)b.click()}
</script>
</body></html>
"""

if __name__ == "__main__":
    main()
