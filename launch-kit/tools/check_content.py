"""Automatic quality check for everything in the Well Listed launch kit.

Run:  python3 launch-kit/tools/check_content.py
       python3 launch-kit/tools/check_content.py path/to/file.md   (check one file or folder)

It reports (and exits with an error if it finds any):
  * em dashes or en dashes (never allowed)
  * anything that could identify the owner (worked out from the git remote, so no
    personal name is stored in this repo)
  * email addresses that are not obvious placeholders
  * income claims, hype words and fake-review signals in customer-facing files
  * common American spellings (warnings only)
"""
import os
import re
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
KIT = os.path.join(ROOT, "launch-kit")
SCAN_EXT = (".md", ".html", ".txt", ".csv", ".json")
SKIP_DIRS = {"dist", ".git", "node_modules"}

# Files that talk to customers (strict marketing checks apply)
CUSTOMER_FACING = ("launch-kit/marketing/", "launch-kit/sales-site/", "launch-kit/product/source/",
                   "launch-kit/product/templates/", "launch-kit/product/READ-ME-FIRST.txt")

INCOME = [
    r"passive income", r"make money (fast|online|from home)", r"\bsix[- ]figure", r"\b6[- ]figure",
    r"quit your (day )?job", r"financial freedom", r"\bget rich\b", r"guaranteed (sales|income|profit)",
    r"£\s?\d[\d,]*\s?(a|per|/)\s?(day|week|month)", r"\bearn(ed|ing|s)? (up to )?£", r"sell (\d+x|twice|double) (as )?(fast|more)",
    r"more sales guaranteed", r"\bincrease (your )?sales by \d+",
]
HYPE = [r"\bhustle\b", r"\bgrind\b", r"\bguru\b", r"game[- ]changer", r"\bunlock\b", r"revolutionary",
        r"\bskyrocket", r"\binsane\b", r"crush it", r"\bexplode\b", r"secret (trick|formula|method)"]
FAKE = [r"★★★★★", r"\"[^\"]{10,120}\"\s*(\n|\s)*[-~]\s*[A-Z][a-z]+ [A-Z]\.", r"\b\d+[,\d]* (happy )?(customers|sellers) (love|trust|use)",
        r"as seen (on|in)\b", r"rated \d(\.\d)? out of 5"]
US = {r"\bcolor": "colour", r"\borganiz": "organis", r"\bfavorite": "favourite", r"\bzip code": "postcode",
      r"\bsweater": "jumper", r"\bcenter\b": "centre", r"\bcheck out the cart": "basket", r"\bmailman": "postie",
      r"\bshipping label": "postage label (fine if quoting a platform)", r"\bmom\b": "mum"}


def owner_terms():
    terms = set()
    try:
        url = subprocess.run(["git", "-C", ROOT, "remote", "get-url", "origin"], capture_output=True, text=True).stdout
        m = re.search(r"[:/]([^/:]+)/[^/]+?(\.git)?\s*$", url)
        if m:
            user = re.sub(r"\d+$", "", m.group(1))
            terms.add(user)
            parts = re.findall(r"[A-Z][a-z]+", user)
            for p in parts:
                if len(p) >= 3:
                    terms.add(p)
            if len(parts) >= 2:
                terms.add(" ".join(parts))
    except Exception:
        pass
    try:
        for key in ("user.name", "user.email"):
            v = subprocess.run(["git", "-C", ROOT, "config", key], capture_output=True, text=True).stdout.strip()
            if v and v.lower() not in ("claude", "noreply@anthropic.com"):
                terms.add(v)
    except Exception:
        pass
    return {t for t in terms if t}


EMAIL_OK = re.compile(r"(example\.|\[|placeholder|yourbrand|hello@well|support@well|@welllisted|welllisted@|@well-listed|noreply@anthropic)", re.I)


def files(targets):
    for t in targets:
        if os.path.isfile(t):
            yield t
            continue
        for dp, dn, fn in os.walk(t):
            dn[:] = [d for d in dn if d not in SKIP_DIRS]
            for f in fn:
                if f.endswith(SCAN_EXT):
                    yield os.path.join(dp, f)


def main():
    targets = sys.argv[1:] or [KIT, os.path.join(ROOT, "CLAUDE.md"), os.path.join(ROOT, "STATE.md"),
                                os.path.join(ROOT, "OPERATOR.md")]
    targets = [t for t in targets if os.path.exists(t)]
    ident = owner_terms()
    errors, warnings = [], []
    for path in files(targets):
        rel = os.path.relpath(path, ROOT)
        if rel.endswith("check_content.py"):
            continue
        try:
            text = open(path, encoding="utf-8").read()
        except UnicodeDecodeError:
            continue
        cust = rel.startswith(CUSTOMER_FACING)
        for n, line in enumerate(text.split("\n"), 1):
            where = "%s:%d" % (rel, n)
            if "—" in line or "–" in line:
                errors.append("%s  dash (em or en) found" % where)
            for t in ident:
                if re.search(r"\b%s\b" % re.escape(t), line, re.I):
                    errors.append("%s  possible owner identifier: %s" % (where, t))
            for em in re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", line):
                if not EMAIL_OK.search(em) and not EMAIL_OK.search(line):
                    errors.append("%s  real-looking email address: %s" % (where, em))
            if cust:
                low = line.lower()
                for pat in INCOME:
                    if re.search(pat, low):
                        errors.append("%s  possible income claim: /%s/" % (where, pat))
                for pat in HYPE:
                    if re.search(pat, low) and "banned" not in low and "avoid" not in low:
                        warnings.append("%s  hype word: /%s/" % (where, pat))
                for pat in FAKE:
                    if re.search(pat, line):
                        errors.append("%s  possible fake review or invented social proof: /%s/" % (where, pat))
                for pat, uk in US.items():
                    if re.search(pat, low) and "americanism" not in low and "us " not in low:
                        warnings.append("%s  American spelling? use '%s'" % (where, uk))
    for w in warnings:
        print("WARNING ", w)
    for e in errors:
        print("PROBLEM ", e)
    print("\n%d problem(s), %d warning(s)." % (len(errors), len(warnings)))
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
