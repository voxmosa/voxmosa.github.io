#!/usr/bin/env python3
"""Regenerate sitemap.xml -- python3 tools/build-sitemap.py

<lastmod> is the only field Google reads besides <loc>. Its docs say the value is
used "if it's consistently and verifiably accurate", so a hand-typed date is worse
than useless once it drifts: an inaccurate lastmod makes Google distrust the
field entirely. Every date is therefore derived, never written by hand.

A file with uncommitted changes gets today's date, because it is about to be
committed today. Everything else gets the date of the commit that last touched
it. test/link-check.js asserts the file still matches, so it cannot rot quietly.

<changefreq> and <priority> are deliberately absent: "Google ignores <priority>
and <changefreq> values."

Each Chinese page and its English counterpart under en/ are listed with
<xhtml:link rel="alternate" hreflang> entries. This is Google's documented way of
declaring language versions in a sitemap, and it mirrors the <link rel="alternate">
tags already in each page's <head>.

Pages are discovered, not listed by hand: every *.html in the root and in en/,
except 404.html and the Search Console verification file.
"""
import datetime, pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "https://voxmosa.com/"
VERIFY = re.compile(r"^google[0-9a-f]+\.html$")


def pages():
    # 404.html 與 Google Search Console 的驗證檔（google<亂碼>.html）不是頁面
    names = [p.name for p in sorted(ROOT.glob("*.html")) if p.name != "404.html" and not VERIFY.match(p.name)]
    names += ["en/" + p.name for p in sorted((ROOT / "en").glob("*.html"))]
    return names


def loc(name):
    # 網址不帶 .html：GitHub Pages 會把 /mosatalk 對應到 mosatalk.html，
    # 這也是每頁 canonical 寫的網址，兩邊要一致。
    if name.endswith("index.html"):
        return BASE + name[: -len("index.html")]
    return BASE + name[: -len(".html")]


def last_modified(name):
    dirty = subprocess.run(["git", "status", "--porcelain", "--", name],
                           cwd=ROOT, capture_output=True, text=True).stdout.strip()
    if dirty:
        return datetime.date.today().isoformat()
    out = subprocess.run(["git", "log", "-1", "--format=%cs", "--", name],
                         cwd=ROOT, capture_output=True, text=True).stdout.strip()
    if not out:
        sys.exit(f"{name} 還沒有任何 commit，無法推導 lastmod")
    return out


def alternates(name, all_pages):
    zh = name[3:] if name.startswith("en/") else name
    en = "en/" + zh
    if zh not in all_pages or en not in all_pages:
        return []
    return [f'    <xhtml:link rel="alternate" hreflang="zh-Hant-TW" href="{loc(zh)}"/>',
            f'    <xhtml:link rel="alternate" hreflang="en" href="{loc(en)}"/>',
            f'    <xhtml:link rel="alternate" hreflang="x-default" href="{loc(zh)}"/>']


def build():
    all_pages = pages()
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
             'xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for name in all_pages:
        lines += ["  <url>", f"    <loc>{loc(name)}</loc>",
                  f"    <lastmod>{last_modified(name)}</lastmod>",
                  *alternates(name, all_pages), "  </url>"]
    lines.append("</urlset>")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    (ROOT / "sitemap.xml").write_text(build(), encoding="utf-8")
    for name in pages():
        print(f"  {name:<24} {last_modified(name)}")
    print(f"共 {len(pages())} 個網址 → sitemap.xml")
