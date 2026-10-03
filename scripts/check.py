#!/usr/bin/env python3
"""Self-review checks for a rendered resume PDF.

Usage:
  python3 check.py "First Last Resume.pdf" [--max-pages 1] [--ats]

  --ats  also fail on multi-column extraction order (use for the ATS version)

Exits 1 when a hard check fails, so it can gate a render step.
"""

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

BANNED = [
    "responsible for", "helped", "worked on", "assisted", "involved in", "participated in",
    "tasked with", "leveraged", "leveraging", "spearheaded", "orchestrated", "utilized",
    "synergy", "cutting-edge", "results-driven", "passionate", "team player",
    "detail-oriented", "hard-working", "go-getter", "unasked", "was allowed to",
]


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True).stdout


def has(tool):
    return shutil.which(tool) is not None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("--max-pages", type=int, default=1)
    ap.add_argument("--ats", action="store_true")
    a = ap.parse_args()
    pdf = Path(a.pdf)
    if not pdf.exists():
        sys.exit(f"Not found: {pdf}")

    fails, warns = [], []
    poppler = has("pdftotext") and has("pdfinfo")
    raw = pdf.read_bytes()

    # Pages
    if poppler:
        pages = int(re.search(r"Pages:\s+(\d+)", run(["pdfinfo", str(pdf)])).group(1))
    else:
        pages = raw.count(b"/Type /Page") - raw.count(b"/Type /Pages")
    if pages > a.max_pages:
        fails.append(f"{pages} pages, limit is {a.max_pages}")

    # Text
    text = run(["pdftotext", str(pdf), "-"]) if poppler else ""
    layout = run(["pdftotext", "-layout", str(pdf), "-"]) if poppler else ""
    words = len(text.split())

    # Banned words
    low = text.lower()
    hits = [w for w in BANNED if re.search(r"\b" + re.escape(w) + r"\b", low)]
    if hits:
        fails.append("banned words: " + ", ".join(hits))

    # Fonts
    if has("pdffonts"):
        fonts = run(["pdffonts", str(pdf)]).splitlines()[2:]
        type3 = [f.split()[0] for f in fonts if "Type 3" in f]
        if type3:
            fails.append("Type 3 fonts (use static font instances): " + ", ".join(sorted(set(type3))))
        unembedded = []
        for f in fonts:
            m = re.search(r"\s(yes|no)\s+(yes|no)\s+(yes|no)\s+\d+\s+\d+\s*$", f)
            if m and m.group(1) == "no":
                unembedded.append(f.split()[0])
        if unembedded:
            warns.append("fonts not embedded: " + ", ".join(unembedded))
    elif b"/Type3" in raw:
        fails.append("Type 3 fonts found (use static font instances)")

    # Links
    links = sorted(set(u.decode("latin-1") for u in re.findall(rb"/URI \((.*?)\)", raw)))

    # Orphans: a wrapped continuation line holding one or two words
    orphans = []
    lines = layout.splitlines()
    for prev, line in zip(lines, lines[1:]):
        s_ = line.strip()
        if s_ and prev.strip() and line[:1].isspace() and len(s_.split()) <= 2:
            orphans.append(s_)
    orphans = sorted(set(orphans))
    if orphans:
        warns.append("possible orphan lines: " + " | ".join(orphans[:8]))

    # Duty-shaped bullet openers
    DUTY = {"coordinate", "manage", "support", "handle", "maintain", "oversee", "ensure", "provide",
            "serve", "cared", "served", "assist", "own", "work", "responsible"}
    duty = []
    for line in layout.splitlines():
        st = line.strip()
        if st.startswith("•"):
            tok = (st[1:].split() or [""])[0].strip(",.")
            first = tok.lower()
            gerund = len(tok) > 5 and tok[1:].islower() and first.endswith("ing")
            if first in DUTY or gerund:
                duty.append(st[1:].strip()[:50])
    if duty:
        warns.append("duty-shaped openers (lead with a result or scope): " + " | ".join(duty[:6]))

    # Empty space below the last line of text
    if poppler:
        bbox = run(["pdftotext", "-bbox", "-f", str(pages), "-l", str(pages), str(pdf), "-"])
        height = re.search(r'<page width="[\d.]+" height="([\d.]+)"', bbox)
        bottoms = [float(y) for y in re.findall(r'yMax="([\d.]+)"', bbox)]
        if height and bottoms:
            empty = 1 - max(bottoms) / float(height.group(1))
            if empty > 0.25:
                warns.append(f"bottom {empty:.0%} of the last page is empty. Ask more interview questions; "
                             "don't enlarge the type")

    # ATS reading order: sidebar words landing mid-sentence
    if a.ats and poppler:
        for line in text.splitlines():
            if re.search(r"[a-z]\s{2,}[A-Z][a-z]+\s{2,}[a-z]", line):
                warns.append("text order may interleave columns: " + line.strip()[:80])
                break

    if not poppler:
        warns.append("poppler not installed, so text, banned-word and orphan checks were skipped")

    print(f"File      {pdf.name}")
    print(f"Pages     {pages}")
    print(f"Words     {words}")
    print(f"Links     {', '.join(links) if links else 'none'}")
    for f in fails:
        print(f"FAIL      {f}")
    for w in warns:
        print(f"WARN      {w}")
    if text:
        head = " / ".join(l.strip() for l in text.splitlines() if l.strip())[:220]
        print(f"Starts    {head}")
    print("RESULT    " + ("FAIL" if fails else "PASS"))
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
