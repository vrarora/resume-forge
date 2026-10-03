#!/usr/bin/env python3
"""Render resume HTML to PDF with headless Chrome, Chromium or Edge.

Usage:
  python3 render.py resume.html "First Last Resume.pdf"
  python3 render.py resume.html            # writes resume.pdf next to the HTML
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    "google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "microsoft-edge",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
]


def find_browser():
    override = os.environ.get("RESUME_BROWSER")
    if override:
        return override
    for c in CANDIDATES:
        if os.path.isabs(c) and os.path.exists(c):
            return c
        found = shutil.which(c)
        if found:
            return found
    return None


def page_count(pdf):
    if shutil.which("pdfinfo"):
        out = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
        for line in out.splitlines():
            if line.startswith("Pages:"):
                return int(line.split()[1])
    # Fallback: count page objects in the raw file.
    data = Path(pdf).read_bytes()
    return data.count(b"/Type /Page") - data.count(b"/Type /Pages")


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    html = Path(sys.argv[1]).resolve()
    pdf = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else html.with_suffix(".pdf")

    browser = find_browser()
    if not browser:
        sys.exit("No Chrome, Chromium or Edge found. Install one, or set RESUME_BROWSER to its path.")

    subprocess.run(
        [browser, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
         f"--print-to-pdf={pdf}", html.as_uri()],
        capture_output=True,
    )
    if not pdf.exists():
        sys.exit(f"Render failed: {pdf} was not created.")
    print(f"{pdf.name}: {page_count(pdf)} page(s)")


if __name__ == "__main__":
    main()
