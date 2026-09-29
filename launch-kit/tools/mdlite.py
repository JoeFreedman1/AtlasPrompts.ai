"""mdlite: a tiny, dependency-free Markdown to HTML converter.

Handles what the Well Listed files use: headings, paragraphs, bold, italic,
inline code, links, bullet and numbered lists (one level of nesting),
blockquotes, fenced code blocks, horizontal rules and pipe tables.
No internet or pip packages needed.
"""
import html
import re


def slugify(text):
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[^a-zA-Z0-9\s-]", "", text).strip().lower()
    return re.sub(r"[\s-]+", "-", text)


def inline(text):
    codes = []

    def keep_code(m):
        codes.append("<code>" + html.escape(m.group(1)) + "</code>")
        return "\x00%d\x00" % (len(codes) - 1)

    text = re.sub(r"`([^`]+)`", keep_code, text)
    text = html.escape(text, quote=False)
    text = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+|[^)\s]+\.(?:html|md|pdf|csv|txt)[^)\s]*)\)",
                  r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", text)
    text = re.sub(r"(?<![\w\"=/])(https?://[^\s<)]+)", r'<a href="\1">\1</a>', text)
    text = re.sub(r"\x00(\d+)\x00", lambda m: codes[int(m.group(1))], text)
    return text


def _table(lines):
    rows = []
    for ln in lines:
        ln = ln.strip()
        if ln.startswith("|"):
            ln = ln[1:]
        if ln.endswith("|"):
            ln = ln[:-1]
        rows.append([c.strip() for c in ln.split("|")])
    out = ['<div class="table-wrap"><table>']
    head, body = rows[0], rows[2:] if len(rows) > 1 and re.match(r"^[\s:|-]+$", lines[1]) else rows[1:]
    out.append("<thead><tr>" + "".join("<th>%s</th>" % inline(c) for c in head) + "</tr></thead><tbody>")
    for r in body:
        out.append("<tr>" + "".join("<td>%s</td>" % inline(c) for c in r) + "</tr>")
    out.append("</tbody></table></div>")
    return "\n".join(out)


def convert(md, heading_ids=True):
    lines = md.replace("\r\n", "\n").split("\n")
    out = []
    i = 0
    para = []

    def flush_para():
        if para:
            out.append("<p>" + inline(" ".join(p.strip() for p in para)) + "</p>")
            para.clear()

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        fence = re.match(r"^(\s*)(```+|~~~+)\s*([\w-]*)\s*$", line)
        if fence:
            flush_para()
            marker = fence.group(2)
            lang = fence.group(3)
            i += 1
            buf = []
            while i < len(lines) and not lines[i].strip().startswith(marker[:3]):
                buf.append(lines[i])
                i += 1
            i += 1
            cls = ' class="lang-%s"' % lang if lang else ""
            out.append("<pre%s><code>%s</code></pre>" % (cls, html.escape("\n".join(buf))))
            continue
        if not stripped:
            flush_para()
            i += 1
            continue
        h = re.match(r"^(#{1,6})\s+(.*?)\s*#*$", stripped)
        if h:
            flush_para()
            lvl = len(h.group(1))
            content = inline(h.group(2))
            hid = ' id="%s"' % slugify(h.group(2)) if heading_ids else ""
            out.append("<h%d%s>%s</h%d>" % (lvl, hid, content, lvl))
            i += 1
            continue
        if re.match(r"^(-{3,}|\*{3,}|_{3,})$", stripped):
            flush_para()
            out.append("<hr>")
            i += 1
            continue
        if stripped.startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|?[\s:|-]+\|[\s:|-]*$", lines[i + 1]):
            flush_para()
            buf = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                buf.append(lines[i])
                i += 1
            out.append(_table(buf))
            continue
        if stripped.startswith(">"):
            flush_para()
            buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                buf.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            out.append("<blockquote>" + convert("\n".join(buf), heading_ids) + "</blockquote>")
            continue
        lm = re.match(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$", line)
        if lm:
            flush_para()
            ordered = lm.group(2)[0].isdigit()
            tag = "ol" if ordered else "ul"
            items = []
            while i < len(lines):
                m = re.match(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$", lines[i])
                if m and len(m.group(1)) < 2:
                    items.append([m.group(3)])
                    i += 1
                elif m and items:
                    items[-1].append(lines[i])
                    i += 1
                elif lines[i].strip() and items and (lines[i].startswith("  ") or lines[i].startswith("\t")):
                    items[-1].append(lines[i])
                    i += 1
                else:
                    break
            out.append("<%s>" % tag)
            for it in items:
                first = it[0]
                rest = [r for r in it[1:]]
                sub = ""
                sub_lines = [r for r in rest if re.match(r"^\s+([-*+]|\d+[.)])\s+", r)]
                cont = [r.strip() for r in rest if r not in sub_lines]
                if cont:
                    first = first + " " + " ".join(cont)
                if sub_lines:
                    sub = convert("\n".join(r.strip() for r in sub_lines), heading_ids)
                box = re.match(r"^\[( |x|X)\]\s+(.*)$", first)
                if box:
                    checked = " checked" if box.group(1) != " " else ""
                    first_html = '<label><input type="checkbox"%s> %s</label>' % (checked, inline(box.group(2)))
                else:
                    first_html = inline(first)
                out.append("<li>%s%s</li>" % (first_html, sub))
            out.append("</%s>" % tag)
            continue
        para.append(line)
        i += 1
    flush_para()
    return "\n".join(out)


if __name__ == "__main__":
    import sys
    print(convert(open(sys.argv[1], encoding="utf-8").read()))
