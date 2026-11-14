#!/usr/bin/env python3
"""把字型子集化後自架 —— python3 tools/build-fonts.py

產出 vendor/fonts/*.woff2 與 vendor/fonts/fonts.css，頁面只要 link 那支 CSS。

為什麼要子集化：Noto Sans TC 與 Noto Serif TC 完整檔都是十幾 MB，直接自架反而
比 Google Fonts 慢。這裡只保留站上實際用到的字元，再把字重軸砍到實際用到的範圍。

⚠️  改過任何頁面文案之後要重跑這支腳本，否則新字會變成豆腐格。
    字元集是從所有 HTML 的原始碼取聯集（根目錄、en/ 與 404.html），所以連只在
    JavaScript 執行後才出現的字串（例如動畫裡的文字）也會被涵蓋。
    頁面是自動找的，新增頁面不必改這支腳本。

需要 fonttools 與 brotli：
    python3 -m venv .venv && .venv/bin/pip install fonttools brotli
    .venv/bin/python tools/build-fonts.py
"""
import pathlib, re, subprocess, sys, urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "vendor" / "fonts"

# 所有字型都從 google/fonts 上游取得未分割的完整檔。
# 以前靜態字重走 Google Fonts 的 CSS API，但那支 API 送的是照 unicode-range
# 切好的分片，而且在部分受限網路裡連不到；上游 repo 的檔案兩個問題都沒有。
UPSTREAM = "https://raw.githubusercontent.com/google/fonts/main/ofl/"

# 靜態字重：IBM Plex Mono 沒有可變字型版本，兩個字重合計不到 15KB。
STATIC = [
    {"family": "IBM Plex Mono", "weight": 400, "url": UPSTREAM + "ibmplexmono/IBMPlexMono-Regular.ttf"},
    {"family": "IBM Plex Mono", "weight": 500, "url": UPSTREAM + "ibmplexmono/IBMPlexMono-Medium.ttf"},
]

# 可變字型：一個檔涵蓋一段字重，比多個靜態檔小得多。範圍要對齊頁面 CSS 實際用到的字重：
#   Space Grotesk  400 內文、500 標籤、700 按鈕與欄位名
#   Noto Sans TC   同上（中文內文跟著 Space Grotesk 的字重走）
#   Noto Serif TC  700 小標題、900 大標題
VARIABLE = [
    {"family": "Space Grotesk", "url": UPSTREAM + "spacegrotesk/SpaceGrotesk%5Bwght%5D.ttf", "lo": 400, "hi": 700},
    {"family": "Noto Sans TC", "url": UPSTREAM + "notosanstc/NotoSansTC%5Bwght%5D.ttf", "lo": 400, "hi": 700},
    {"family": "Noto Serif TC", "url": UPSTREAM + "notoseriftc/NotoSerifTC%5Bwght%5D.ttf", "lo": 700, "hi": 900},
]


def pages():
    # Search Console 的驗證檔（google<亂碼>.html）不是頁面，略過
    return [p for p in sorted(ROOT.glob("*.html")) if not re.match(r"google[0-9a-f]+\.html$", p.name)] + sorted((ROOT / "en").glob("*.html"))


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as r:
        return r.read()


def charset():
    chars = set()
    for p in pages():
        chars |= set(p.read_text(encoding="utf-8"))
    chars |= {chr(c) for c in range(0x20, 0x7F)}   # 完整可列印 ASCII，留餘裕
    return "".join(sorted(c for c in chars if c.isprintable() or c == " "))


def slug(family, weight):
    return re.sub(r"[^a-z0-9]+", "-", family.lower()).strip("-") + f"-{weight}"


def subset(src, dest, text_file):
    subprocess.run([
        "pyftsubset", str(src),
        f"--text-file={text_file}",
        "--flavor=woff2",
        f"--output-file={dest}",
        "--layout-features=*",       # keep kerning and friends
        "--no-hinting",
        "--desubroutinize",
    ], check=True)


def face(family, weight, name):
    # format('woff2'), not 'woff2-variations'. The latter is a transitional
    # spelling some browsers do not recognise; they skip the whole @font-face
    # rule and the font silently never loads.
    return (f"@font-face{{font-family:'{family}';font-style:normal;"
            f"font-weight:{weight};font-display:swap;"
            f"src:url('./{name}.woff2') format('woff2')}}")


def main():
    try:
        subprocess.run(["pyftsubset", "--help"], capture_output=True, check=True)
    except (FileNotFoundError, subprocess.CalledProcessError):
        sys.exit("找不到 pyftsubset。請先安裝 fonttools 與 brotli（見檔頭說明）。")

    OUT.mkdir(parents=True, exist_ok=True)
    text = charset()
    text_file = OUT / ".charset.txt"
    text_file.write_text(text, encoding="utf-8")
    cjk = sum(1 for c in text if ord(c) > 0x2E80)
    print(f"字元集：{len(text)} 個，其中 {cjk} 個中日韓與全形符號（來自 {len(pages())} 個頁面）")

    out_css = ["/* 由 tools/build-fonts.py 產生 —— 不要手動編輯。",
               "   改過頁面文案後請重跑，否則新字會缺字。 */"]
    total = 0
    for st in STATIC:
        name = slug(st["family"], st["weight"])
        ttf = OUT / f".{name}.ttf"
        ttf.write_bytes(fetch(st["url"]))
        woff2 = OUT / f"{name}.woff2"
        subset(ttf, woff2, text_file)
        ttf.unlink()
        size = woff2.stat().st_size
        total += size
        print(f"  {st['family']} {st['weight']}: {size // 1024}KB")
        out_css.append(face(st["family"], st["weight"], name))

    for vf in VARIABLE:
        family, lo, hi = vf["family"], vf["lo"], vf["hi"]
        name = slug(family, f"{lo}-{hi}-var")
        raw = OUT / f".{name}.ttf"
        raw.write_bytes(fetch(vf["url"]))
        # Clamp the axis to the range the site actually uses before subsetting
        # the characters: dropping the unused weight ends drops their
        # interpolation data with them.
        limited = OUT / f".{name}.limited.ttf"
        subprocess.run(["fonttools", "varLib.instancer", str(raw),
                        f"wght={lo}:{hi}", "-o", str(limited)],
                       check=True, capture_output=True)
        woff2 = OUT / f"{name}.woff2"
        subset(limited, woff2, text_file)
        raw.unlink(); limited.unlink()
        size = woff2.stat().st_size
        total += size
        print(f"  {family} {lo}–{hi}（可變字型）: {size // 1024}KB")
        out_css.append(face(family, f"{lo} {hi}", name))   # 範圍寫法，瀏覽器自行內插

    text_file.unlink()
    (OUT / "fonts.css").write_text("\n".join(out_css) + "\n", encoding="utf-8")

    # Drop leftovers that fonts.css no longer references, so files from a
    # previous weight list do not sit in version control while nothing loads them.
    css_text = (OUT / "fonts.css").read_text(encoding="utf-8")
    for stale in sorted(OUT.glob("*.woff2")):
        if stale.name not in css_text:
            print(f"  移除孤兒檔 {stale.name}（{stale.stat().st_size // 1024}KB）")
            stale.unlink()
    print(f"共 {len(STATIC)} 個靜態字重 + {len(VARIABLE)} 個可變字型，"
          f"{total // 1024}KB → {OUT.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
