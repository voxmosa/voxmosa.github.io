#!/usr/bin/env python3
"""同步各頁共用的區塊 —— python3 tools/sync-views.py

每個頁面檔都包含全站所有畫面（<section class="view" id="v-…">），差別只在
哪一個畫面預設是 on。站內切換因此不必重新載入，關掉 JavaScript 時每個網址也
照樣顯示自己的內容。代價是同一段文案在同語言的 7 個檔案裡各有一份。

所以改文案的流程是：
    1. 只改 index.html（英文改 en/index.html）
    2. 跑這支腳本，把共用區塊複製到同語言的其他頁
    3. 照常重跑 tools/build-fonts.py 與 tools/build-sitemap.py

複製的範圍：
    - <head> 裡的 <style>（整站共用的樣式）
    - <main> 裡所有畫面，並把 on 換到該頁自己的畫面
    - 頁尾 <footer>（語言切換連結的目標會換成該頁的對應頁）
    - 頁尾的主程式 <script>
不複製的：<head> 的標題、描述、正式網址、結構化資料，以及頁首導覽列——這些每頁不同。

哪個檔案對應哪個畫面，是從導覽列連結的 data-route 讀出來的，不必在這裡維護清單。
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def block(s, start_pat, end, name, last=False):
    ms = list(re.finditer(start_pat, s))
    if not ms:
        sys.exit(f"找不到 {name}")
    a = (ms[-1] if last else ms[0]).start()
    b = s.index(end, a) + len(end)
    return a, b


STYLE = (r"<style>", "</style>")
MAIN = (r'<section class="view[^"]*" id="v-', None)
FOOT = (r"<footer>", "</footer>")
SCRIPT = (r"<script>\n\(function\(\)\{\n  'use strict';", "</script>")


def main_span(s):
    a = re.search(MAIN[0], s).start()
    b = s.rindex("</section>", a, s.index("</main>")) + len("</section>")
    return a, b


def routes(src):
    """href → route，從首頁導覽列讀出來"""
    head = src[src.index("<header"):src.index("</header>")]
    return dict(re.findall(r'<a href="([\w-]+\.html)" data-route="(\w+)"', head)) | {"index.html": "home"}


def sync_dir(d, lang_link):
    src = (d / "index.html").read_text(encoding="utf-8")
    route_of = routes(src)
    parts = {
        "style": src[slice(*block(src, *STYLE, "<style>"))],
        "main": src[slice(*main_span(src))],
        "foot": src[slice(*block(src, *FOOT, "<footer>"))],
        "script": src[slice(*block(src, *SCRIPT, "主程式", last=True))],
    }
    changed = 0
    for p in sorted(d.glob("*.html")):
        if p.name in ("index.html", "404.html"):
            continue
        r = route_of.get(p.name)
        if not r:
            print(f"  略過 {p.name}（導覽列沒有對應的 data-route）")
            continue
        s = old = p.read_text(encoding="utf-8")
        a, b = block(s, *STYLE, "<style>"); s = s[:a] + parts["style"] + s[b:]
        a, b = main_span(s)
        views = parts["main"].replace('<section class="view on"', '<section class="view"')
        views = views.replace(f'<section class="view" id="v-{r}"', f'<section class="view on" id="v-{r}"', 1)
        s = s[:a] + views + s[b:]
        a, b = block(s, *FOOT, "<footer>")
        s = s[:a] + lang_link(parts["foot"], p.name) + s[b:]
        a, b = block(s, *SCRIPT, "主程式", last=True); s = s[:a] + parts["script"] + s[b:]
        if s != old:
            p.write_text(s, encoding="utf-8")
            changed += 1
            print(f"  已同步 {p.relative_to(ROOT)}")
    return changed


def zh_link(foot, name):
    return re.sub(r'<a href="en/[^"]*"( lang="en" hreflang="en">English</a>)', rf'<a href="en/{name}"\1', foot)


def en_link(foot, name):
    return re.sub(r'<a href="\.\./[^"]*"( lang="zh-Hant-TW" hreflang="zh-Hant-TW">中文</a>)', rf'<a href="../{name}"\1', foot)


if __name__ == "__main__":
    n = sync_dir(ROOT, zh_link) + sync_dir(ROOT / "en", en_link)
    print(f"共更新 {n} 個檔案" if n else "所有頁面都已同步，沒有需要更新的檔案")
