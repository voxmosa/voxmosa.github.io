# voxmosa.github.io

Voxmosa 官方網站，中英雙語。**純靜態 HTML，沒有建置流程** —— 改完直接 push 就上線。
渲染所需的一切都在 repo 內，唯一的外部請求是 GA4；關掉 JavaScript 內容也照樣完整。

| 路徑 | 內容 |
| --- | --- |
| `index.html` | 首頁（直排標題、逐字稿示意、聲波、三項產品、資料邊界、自己跑過的數字）|
| `mosatalk.html` | MosaTalk：地端 AI 語音客服 |
| `mosaminutes.html` | MosaMinutes：地端 AI 會議記錄平台 |
| `mosascore.html` | MosaScore：地端通話品質分析（效度驗證中）|
| `on-premise.html` | 為什麼地端：資料邊界、雲地比較、主機配置、產業與合規、部署之後的事 |
| `languages.html` | 臺灣本土語言：台語、客語六腔、原住民族語的能力與可查證的依據 |
| `research.html` | 團隊與研究：獎項、41 篇發表（可篩選）、媒體報導、研究筆記 |
| `en/` | 英文版，檔名與中文版一一對應（`en/mosatalk.html` ↔ `mosatalk.html`）|
| `404.html` | 找不到頁面。中英並列，從 `/en/` 底下進來時英文排在前面。GitHub Pages 自動使用 |
| `vendor/fonts/` | 子集化後自架的字型（含授權說明）|
| `test/` | 回歸測試，`test/baseline/` 為版面基準 |
| `tools/sync-views.py` | **改文案後先跑這支**：把 `index.html` 的共用區塊同步到同語言的其他頁 |
| `tools/build-fonts.py` | 重新產生字型子集 |
| `tools/build-sitemap.py` | 重新產生 `sitemap.xml`，`lastmod` 由 git 推導 |
| `tools/bake.js` | 第一代頁面的烘焙工具（已無頁面需要，保留備查）|
| `og.png` / `og-en.png` | 社群分享縮圖，中文頁 / 英文頁 |
| `favicon.svg` / `favicon.png` | 分頁圖示。Google 不吃 SVG，所以兩種都要 |
| `logo.png` | `Organization.logo` 用的方形識別標誌 |
| `robots.txt` / `sitemap.xml` | 爬蟲規則與網站地圖；兩者都刻意極簡，理由見 [SEO 與 AEO](#seo-與-aeo) |
| `CNAME` / `.nojekyll` | GitHub Pages 的自訂網域與停用 Jekyll |

## 各產品實際支援的語言

寫文案前先看這張表。**三個產品的語言涵蓋範圍不一樣**，把其中一個的能力
講到另一個身上，是這個網站踩過的錯（FAQ 曾經寫「MosaTalk 支援五種語言」，
那是 MosaMinutes 的範圍）。

| 產品 | 語言 |
| --- | --- |
| MosaMinutes（會議轉錄）| 國語、台語、客語、原住民族語、英語 |
| MosaTalk（語音客服）| 國語、台語、英語 —— 台語**只聽得懂、以國語回答**，台語合成仍在開發規劃中 |
| MosaScore（通話分析）| 語言不是這個產品的訴求重點，不要在文案裡強調；台語辨識列在開發規劃中 |

公司層級的宣稱（例如首頁 hero 與 `Organization` 的 description）涵蓋五種語言是
成立的，因為 MosaMinutes 做得到 —— 但只要句子的主詞變成單一產品，就要回來查這張表。

客語為六腔全覆蓋（四縣、海陸、大埔、饒平、詔安、南四縣），可以明講，
市面上多數同業只做三腔或兩腔。原住民族語 16 族 42 語是真的，但使用人口少、
搜尋量極低，定位是**能力證明而非流量來源**，提到即可，不要當主打。

### 本土語言專案裡，哪些是我們做的

兩個專案的分工**不一樣**，寫文案前先看這張表：

| | 族語（原語會 / 意傳）| 客語（Gohakka / 瞬息科技）|
| --- | --- | --- |
| 語音辨識 ASR | ✅ 本團隊 | ✅ 本團隊 |
| 語音合成 TTS | ✅ 本團隊 | ✅ 本團隊 |
| 機器翻譯 | ✅ 本團隊 | ❌ 平台方（瞬息科技）|
| 語料整理 | 部分為本團隊 | 部分為本團隊 |

兩邊唯一的差別是**機器翻譯**：族語的是我們做的，客語的不是。
`gohakka.org/copyright` 明文寫「客語語音合成、語音識別技術由牧仁資訊研發」，
同時把機器翻譯歸給瞬息科技 —— 所以客語的翻譯**不能**寫成我們的。
`languages.html` 在引用這句版權宣言的同一段裡，就寫明了機器翻譯與語言模型是瞬息科技的。

語料整理兩邊都是「部分」，語料本身分別屬於客家委員會與原住民族委員會，
所以措辭要保留那個「部分」，不要寫成整批都是我們做的。

出處強度也不一樣：客語有 `gohakka.org/copyright` 可以直接引用；
族語那邊 `ai-labs.ilrdf.org.tw` 只有原語會的版權宣告，沒有任何合作方掛名，
宣稱成立但讀者查不到 —— 哪天能談到一句掛名，那是值得爭取的東西。

## 頁面上一定要留著的限制與歸屬

2026-11 改版時，為了把字數壓下來，這些句子曾經被一起刪掉，比對原始內容後才補回來。
它們不是可以精簡的「細節」：少了它們，網站會說得比產品實際能做的更滿，
被客戶或審查者發現時傷的是信任。改版或精簡文案時，逐項確認這些都還在：

| 頁面 | 必須留著的句子 |
| --- | --- |
| `mosascore.html` | 目前**只支援雙聲道**錄音；**尚未在客戶環境正式上線**；分數**未經真實成交資料驗證**、不提供準確率；長通話的**處理時間會超過音檔長度**；B2B 銷售需另行評估 |
| `mosascore.html` | 「情緒推斷只用於客戶端」的原則（對客服的評分屬於勞動監控，歐盟已禁止工作場所的情緒推斷）|
| `mosaminutes.html` | **目前不能直接接** Google Meet、Microsoft Teams、Zoom |
| `mosatalk.html` | 台語只聽不說；邊緣分離模式**另需一台小型雲端主機** |
| `languages.html` | Gohakka 的機器翻譯與語言模型是瞬息科技的；語料屬於客家委員會、原住民族委員會，本團隊只承擔部分整理 |
| `research.html` | 媒體報導是核心成員**於過往任職單位**主導的技術 |
| 全站 | 不給準確率的行銷數字；沒有合規壓力時，雲端訂閱通常比較適合 |

各產品頁的「規格與限制」區塊裡，限制項目以橘色驚嘆號標示，放在正文、不收合。
英文版 `en/` 的同一頁有同樣的句子，改一邊要改另一邊。

## 改動之後要記得的事

1. **改過文案** → 只改 `index.html`（英文改 `en/index.html`），再跑 `python3 tools/sync-views.py`
   同步到同語言的其他頁（原因見[頁面結構](#頁面結構)）
2. **改過文案** → 重跑 `tools/build-fonts.py`，否則新字缺字
3. **改過任何頁面** → 重跑 `tools/build-sitemap.py`，否則 `lastmod` 過期
4. 推之前跑三支測試（見[測試](#測試)）

## 頁面結構

### 每個檔案都包含全站所有畫面

每個 HTML 檔裡都有 8 個畫面（首頁、三個產品、地端、語言、研究、申請 PoC），
各是一個 `<section class="view" id="v-…">`，只有該頁自己的那一個帶 `on`，其餘 `display:none`。

| 情況 | 行為 |
| --- | --- |
| 有 JavaScript | 點導覽列時不重新載入，直接切換畫面（新畫面從左右滑入），並用 `history.pushState` 把網址換成對應的檔案 |
| 沒有 JavaScript | 導覽列是真的 `<a href>`，點下去就載入那個檔案，而那個檔案的靜態 HTML 本來就顯示自己的畫面 |
| 用 `file://` 直接開 | 照樣切換，只是網址列不變（瀏覽器不允許在 `file://` 上 `pushState`）|

這樣做是為了讓站內切換沒有整頁重讀的頓挫，同時每個網址仍是一個可以被搜尋引擎收錄、
有自己標題與描述的獨立頁面。

代價有兩個，都是刻意接受的：

- **同一段文案在同語言的 7 個檔案裡各有一份**，每個檔案約 150KB。`tools/sync-views.py`
  處理這件事：只改 `index.html`，跑一次就把樣式、所有畫面、頁尾與主程式複製到其他頁，
  並把 `on` 換到各頁自己的畫面。它不碰每頁不同的 `<head>`（標題、描述、正式網址、結構化資料）
  與頁首導覽列。在已同步的頁面上跑它不會有任何改動，可以當成檢查用。
- **原始碼裡有 8 個 `<h1>`**，畫面上只看得到該頁那一個，其餘在隱藏的畫面裡。
  搜尋引擎看得到隱藏畫面的文字，但通常給的權重較低；每頁的 `<title>`、描述與正式網址
  都是獨立的，所以不會被當成同一頁。若哪天要改成「每個檔案只放自己的內容」，
  切換手感可以靠瀏覽器原生的跨頁轉場（`@view-transition`）維持，那是另一次獨立的改動。

`index.html#poc` 是申請頁。有 JavaScript 時由切換程式處理；沒有 JavaScript 時
靠 CSS 的 `:target` 把申請畫面顯示出來（`main:has(#poc:target)`），所以這個連結兩種情況都到得了。

### 動畫與互動

所有程式碼都在每頁末尾同一段 `<script>`，原生 JavaScript，沒有任何框架。

| 項目 | 說明 |
| --- | --- |
| 開場 | V 標誌描邊、兩道弧線亮起、碳黑幕往上掀開。每個瀏覽器分頁只播一次（`sessionStorage`）|
| 直排標題 | 每個畫面的直排標語逐字落下，最後蓋上「地端語音」印章；英文版逐詞落下 |
| 逐字稿示意 | 首頁的國台語逐字稿逐字打出，英文版每句下方有淡淡的英文翻譯 |
| 聲波 | 首頁底部的山稜聲波畫在單一 `<canvas>` 上，跟著滑鼠起伏；捲出畫面就停 |
| 捲動進場 | `.rv` 元素捲進畫面時浮現；數字從 0 跳到實際值 |
| 研究發表 | 依主題篩選 41 篇論文 |
| 申請表單 | 見[申請表單](#申請表單) |

幾條必須維持的性質，都有測試把關：

- **靜態標記就是完整狀態。** 論文清單與篩選鈕直接寫在 HTML 裡，程式只負責篩選；
  數字在捲到之前保持真實數值，開始動畫時才從 0 跳 —— 否則有 JS 時畫面上是「0」、
  沒 JS 時是「10」，`test/render-check.js` 的「有無 JavaScript 可見文字量相同」會失敗。
- **`prefers-reduced-motion`**：開場不播、不位移、循環動畫停住，但淡入與切換仍在。
- **只動 `transform` 與 `opacity`。** 切換時不碰版面屬性，連續切換十次不掉幀；
  聲波從上百個 DOM 元素改成單一 canvas 也是為了這件事。

### 視覺規範

顏色、字標與分頁圖示來自 Voxmosa 品牌套件：碳黑 `#141413`、暖白 `#f4f3f0`、
訊號橘 `#ED9A4A`（淺底上的橘色文字用 `#c47a20`，對比才夠）。字標是外框化的 SVG，
不要改回文字。樣式全部在每頁 `<head>` 的同一段 `<style>`，以 class 撰寫，沒有 inline 的版面樣式。

頁首在中英文之間必須**位置不動**：切換語言時，語言鈕與「申請 PoC」鈕要停在同一個位置。
做法是兩顆按鈕固定寬度、靠右對齊，導覽分頁從標誌後方靠左排起（三個產品名中英相同，
所以前三格位置也一致），兩種語言用同樣的字級與間距。英文分頁較長，寬度不夠時改成兩行
（分頁移到第二列可以左右滑動），斷點是 1220px，**中英文共用同一個斷點** ——
各用各的斷點，就會出現某些寬度下一種語言單行、另一種兩行的跳動。
改導覽列文字之後，在 1221px 寬確認英文版仍然單行放得下。

### 這些頁面的來歷

| 世代 | 說明 |
| --- | --- |
| 第一代 | 用視覺編輯器 Claude Design 產出，客戶端渲染（`<x-dc>` 模板、React、`support.js`）|
| 第二代 | 烘焙成靜態 HTML，移除 runtime；版面用 inline style 加 `r-*` 響應式 class |
| 第三代（現在）| 2026-11 全面改版：新的視覺與動畫、中英雙語、免重載切換、內容精簡後補回限制與歸屬說明。版面改為 class 撰寫，`#dc-root` / `.sc-host` 與 `r-*` class 都已不存在 |

## 雙語

`en/` 底下的頁面與中文版一一對應。每頁 `<head>` 有 `<link rel="alternate" hreflang>`
指向兩個語言版本（`x-default` 是中文版），`sitemap.xml` 也列了同樣的對應。
導覽列右上的「EN」／「中文」切換時會停在同一頁，不會跳回首頁。

英文用詞的約定：

| 中文 | 英文 |
| --- | --- |
| 台語 | Taigi |
| 原住民族語 | Indigenous languages（16 peoples, 42 languages）|
| 客語六腔 | Sixian, Hailu, Dapu, Raoping, Zhao'an, South Sixian |
| 客家委員會 / 原住民族委員會 | Hakka Affairs Council / Council of Indigenous Peoples |
| 原住民族語言研究發展基金會 | Indigenous Languages Research and Development Foundation（ILRDF）|
| 意傳科技 | iThuan —— **待確認正式英文名稱** |
| 瞬息科技 | Shunxi Technology（音譯）—— **待確認正式英文名稱** |

英文內文用直引號 `"`，不用彎引號 `“ ”`：中文字型會把彎引號畫成全形寬度，字距看起來不對。

示意畫面裡的逐字稿（首頁、MosaMinutes 的校對畫面）在英文版保留中文，
因為要展示的就是中文輸出；MosaScore 的客戶發言則譯成英文並標示「translated from Mandarin」。

## 申請表單

申請頁的表單在每頁末尾的程式裡設定：

```js
var FORM_ENDPOINT = 'https://formspree.io/f/moedvvzw';
```

- **有網址（現況）**：按下送出就直接寄到 Formspree，通知信寄到註冊 Formspree 的信箱，表單原地換成「已收到您的申請」；失敗時顯示錯誤並附上信箱。
  有隱藏欄位 `_gotcha` 擋機器人。改完記得跑 `tools/sync-views.py` 同步到所有頁面。
- **留空**：退回舊做法，開啟訪客的郵件程式並帶入內容。

換收件服務或換帳號時，只改 `index.html` 與 `en/index.html` 這一行，再跑 `tools/sync-views.py`。

建議用 Formspree（免費方案每月 50 封）。表單收集姓名與 Email，依個資法通常要在收集時告知用途，
送出按鈕下方目前**還沒有**個資告知，見[後續可做的事](#後續可做的事)。

## SEO 與 AEO

### 語意標籤

每頁都有 `header` / `nav` / `main` / `section` / `footer` 地標，每個畫面恰好一個 `<h1>`。
首頁的主標語是直排的裝飾文字（`aria-hidden`），另外放一個畫面上看不到的 `<h1 class="sr-only">`
給搜尋引擎與螢幕閱讀器。

> 別誤會這件事的效益。Google 的 SEO Starter Guide 寫得很直白：
> 「Google rarely relies on semantic HTML structure」，而且標題階層順序錯了
> **不會**傷害排名。語意標籤真正換到的是無障礙與可維護性 ——
> 下面那個把公司名讀成 `Vxmosa` 的 bug，就是靠這個方向找出來的。

### 結構化資料：留下來的都是會被消費的

| 頁面 | `@graph` 內容 |
| --- | --- |
| `index.html` | `Organization`（含 `legalName`、`taxID`、`logo`、`award`）、`WebSite` |
| 三個產品頁 | `SoftwareApplication`、一個最小的 `Organization` 節點 |
| `on-premise.html` / `languages.html` / `research.html` | 只有最小的 `Organization` 節點 |
| `en/index.html` | 英文的 `WebSite`、最小的 `Organization` 節點 |
| `en/` 的三個產品頁 | 英文的 `SoftwareApplication`、最小的 `Organization` 節點 |
| `en/` 的其他頁 | 只有最小的 `Organization` 節點 |

完整的 `Organization` 只放中文首頁（Google 的建議），`@id` 是全站共用的
`https://voxmosa.com/#organization`。子頁的 `publisher` 曾經是**裸的 `@id` 存根**，
指向一個只存在於首頁 graph 裡的節點 —— 單獨解析子頁的爬蟲會看到懸空參照，
所以現在每個子頁自己內嵌一個帶 `@type` 與 `name` 的最小節點。

對照 Google 文件逐項核過之後，以下四種**全部移除**了，它們沒有任何東西會消費。
改版過程中曾有一版把 `FAQPage`、`WebPage`、`CollectionPage` 加回去，上線前已依這張表再次移除：

| 移除的型別 | 原因 |
| --- | --- |
| `FAQPage` | **2026-05-07 起 Google 不再顯示 FAQ 複合式結果**，同年 6 月連文件與 Rich Results Test 支援都撤掉了 |
| `ItemList` | Carousel 只支援 Course list / Movie / Recipe / Restaurant，`SoftwareApplication` 不在其中 |
| `WebPage` | Search Gallery 裡沒有這個功能，Google 沒有對應的複合式結果 |
| `BreadcrumbList` | 標的是「首頁 → 自己」，但頁面上根本沒有可見的麵包屑。政策原文：**「Don't mark up content that is not visible to readers of the page.」** |

`SoftwareApplication` 留著，但要知道它**現在拿不到複合式結果**：必要屬性是
`name`、`offers.price`，加上 `aggregateRating` 或 `review` 二選一，我們只有第一個。
這沒有誠實的補法 —— 沒有公開價格、沒有評價，而**把 `price` 填 0 是謊話不是漏洞**，
產品不是免費的。留它是當作對非 Google 消費者的機器可讀產品描述，別期待更多。
`award`、`knowsAbout`、`knowsLanguage`、`areaServed` 同理：不在 Google 的支援屬性表裡，
留著是同一個押注。

### favicon 要有 PNG，SVG 不算

**Google Search 不支援 SVG favicon。** 支援清單是 BMP、GIF、ICO、PNG、JPEG、
PPM、TIFF，而且必須是正方形、至少 8×8、建議大於 48×48。只掛 `favicon.svg`
的話搜尋結果顯示的是通用地球圖示。

所以 `favicon.svg` 留給瀏覽器，另外附一張 `favicon.png`（144×144）給 Google。
`logo.png`（512×512）則是 `Organization.logo` 用的 —— 文件要求的是
「在純白背景上看起來符合預期」的方形識別標誌，所以不能拿深色的 `og.png` 充數。

### 分享縮圖

`og.png` 給中文頁、`og-en.png` 給英文頁，都是 1200×630：碳黑底、字標、主標語、
「地端語音」印章與聲波。每頁的 `og:image:alt` 與 `twitter:card`（`summary_large_image`）都已設定。

### robots.txt 為什麼只有三行

它曾經逐一列出 GPTBot、ClaudeBot、PerplexityBot、Google-Extended 等十二個爬蟲，
各給一段 `Allow: /`。那些區塊**沒有任何作用，而且是個陷阱**：

- `Allow` 不授予任何權限。爬取本來就是預設允許的，所以一份沒有 `Disallow`
  的 robots.txt 等同於沒有 robots.txt。整份檔案唯一有作用的是 `Sitemap:`。
- 更糟的是，規格寫明「User agent specific groups and global groups (`*`) are
  not combined」—— 具名群組**取代** `*` 群組而不是疊加。哪天有人在 `*` 底下
  加一條 `Disallow`，那十二個爬蟲一個都不會繼承。

順帶一提 `Google-Extended` 也不是多數人以為的那樣：它管的是 Gemini 的訓練資料，
原文寫「does not impact a site's inclusion in Google Search」，跟
AI Overviews / AI Mode 無關。

### sitemap 只保留 lastmod 與語言對應

`<changefreq>` 與 `<priority>` 都拿掉了 —— 文件原文：
「Google ignores `<priority>` and `<changefreq>` values.」

`<lastmod>` 會被採用，但有條件：「if it's consistently and verifiably accurate」。
一旦不可信，Google 會整個欄位不再採信 —— 所以這個日期**不由人手寫**。

`tools/build-sitemap.py` 從 git 推導：有未提交改動的檔案取今天，其餘取最後一次
commit 的日期。`test/link-check.js` 會驗證檔案裡的值仍然對得上，對不上就失敗並提示
重跑。手寫的日期一定會過期 —— 這件事發生過一次：六個網址全部停在
`2026-08-29`，其中兩個網址的頁面根本是那天之後才建立的。

現在共 14 個網址（中文 7、英文 7），每個都附 `<xhtml:link rel="alternate" hreflang>`
標明對應的另一語言版本。頁面是自動找的（根目錄與 `en/` 的 `.html`，`404.html` 除外）。

> 因為 `lastmod` 取自 git，**改完頁面要在同一天 commit**。今天跑工具、明天才 commit，
> `link-check.js` 會說日期對不上 —— 重跑一次工具即可。

### 移除了 llms.txt

站上曾經有一份 `llms.txt`。Google 在 2026-06-15 把這句話寫進 AI 優化指南：

> "You don't need to create new machine readable files, AI text files, markup,
> or Markdown to appear in Google Search... Doing so will neither harm nor help
> your site's visibility or rankings in Google Search, as Google Search ignores them."

不傷害也沒幫助，但它重複了一整批會漂移的事實（42 語、DGX Spark GB10、≈1 秒、
MosaScore 的效度保留），每次改文案都要手動同步。

### 標誌的無障礙名稱

字標的 `o` 是 SVG 畫的。第二代頁面的兩側字母是文字，所以在無障礙樹與純文字擷取之下，
公司名稱被讀成 **`Vxmosa`** —— 少一個 o。

現在整個字標都是外框化的 SVG（沒有文字），一律標成 `aria-hidden="true"`，
名稱由外層連結的 `aria-label` 提供（「Voxmosa 首頁」／「Voxmosa home」）。

### 常見問題

產品頁、地端頁與語言頁底部各有自己的常見問題（共 30 題），平常收合、點開才展開；
申請頁另有 4 題。問答全部取自原站既有的事實，沒有新增未經驗證的規格或數字；
「準確率是多少」維持站上一貫的回答方式：不給行銷數字。

起因是關鍵字盤點：使用者實際會打進搜尋框的整串字（「AI 語音會議記錄」「AI 語音客服」
「地端語音 AI」）在早期的文案裡一個都沒出現過。`FAQPage` 標記已經移除（見上表），
但**可見的問答保留** —— 它是真的在回答買家的問題，那本身就是 Google 指南推薦的事，跟有沒有標記無關。

## 測試

推 code 之前跑這三支：

```sh
node test/link-check.js     # 連結會不會 404、導覽列各頁是否一致、sitemap 是否對得上
node test/render-check.js   # 內容有沒有渲染出來（含各種失敗情境）
node test/layout-check.js   # 版面有沒有跑掉
```

三支都**自動找頁面**（根目錄與 `en/` 的 `.html`，`404.html` 除外）。
以前這份清單是寫死在四個地方的，新增頁面時漏加不會有任何東西失敗 ——
頁面只是安靜地沒有測試覆蓋、也沒有字型子集。現在新增頁面不必改任何清單。

內容測試最花時間（14 頁 × 三種情境，其中「極慢網路」每頁刻意等滿 45 秒，合計十幾分鐘），
趕時間可以用 `node test/render-check.js normal` 快速確認。
三支都以離開碼回報結果，失敗會列出是哪一頁、哪個元素、差在哪裡。
版面若是**刻意**改動，用 `node test/layout-check.js --save` 更新基準，
並把基準的 diff 一起提交 —— 那份 diff 就是這次視覺改動的紀錄。

### 連結

```sh
node test/link-check.js
```

檢查每個站內連結的目標檔案與錨點 id 是否真的存在。相對路徑以頁面所在資料夾為準，
所以 `en/` 底下的 `../mosatalk.html` 會被解析成中文版的 `mosatalk.html`。
站外連結只計數、不連線驗證，以免測試依賴外部網路。

`<a href>` 之外，`<link href>`（字型 CSS、favicon、字型 preload）也一併檢查。
preload 的檔名跟 `tools/build-fonts.py` 的產出耦合 —— 字重範圍一改檔名就變，
而 preload 失效時瀏覽器不會報錯，只是白抓一個 404。

導覽列的預期項目是**從首頁推導**的，不是寫死清單：中文頁以 `index.html` 為準，
英文頁以 `en/index.html` 為準。第一版拿各頁的共同項目當清單，等於把當下的不一致固化進測試。

> 這支測試在 2026-11 改版時抓到一個真的錯：英文頁的頁尾是從中文頁尾複製的，
> 連帶把中文頁上的「English」連結也帶過去，指向 `en/index.html` —— 從 `en/` 出發就是
> `en/en/index.html`，點下去 404。畫面上完全正常，只有這支測試看得到。

### 內容

```sh
node test/render-check.js         # 全部情境
node test/render-check.js nojs    # 只跑單一情境
```

零依賴，需 Node 22+ 與本機的 Chrome 或 Chromium。它會自己起 HTTP server 並以
Chrome DevTools Protocol 驅動 headless 瀏覽器，對每個頁面各跑三個情境：

| 情境 | 驗證的事 |
| --- | --- |
| `normal` | 內容顯示正常，且**除了 GA4 之外沒有任何外部請求**（含字型）|
| `nojs` | 關閉 JavaScript 內容照樣完整 |
| `slow` | 30KB/s 慢速連線下仍然完整顯示 |

最後還有一項跨情境斷言：**每頁在有無 JavaScript 之下的可見文字量必須完全相同**。
這是整個靜態化的核心性質，也是最容易在改動中悄悄退步的一項 ——
2026-11 改版時，研究頁的論文清單一度由 JavaScript 產生、數字一度先歸零再跳動，
兩者都會讓這項失敗，上線前改成靜態標記。

正常與慢速情境下若出現任何 JS 例外即判定失敗。判定指標是 `document.body.innerText`
的長度，因為它排除 `display:none` 的內容，恰好等於「使用者實際看得到多少字」。

### 版面

```sh
node test/layout-check.js          # 與基準比對
node test/layout-check.js --save   # 重新產生基準
```

在 375 / 768 / 1440 三種寬度下走訪整個 DOM，記錄每個元素的 bounding rect
與 `display`、`grid-template-columns`、`gap`、`font-size`、`padding`、`max-width`。
元素以「DOM 位置路徑」識別而非選擇器 —— 改動 `style` 屬性或加 class 都不影響對齊，
只有真的動了 DOM 結構才會對不上（那會被明確報成結構差異）。

基準是 `test/baseline/*.txt`，純文字所以 `git diff` 直接看得出哪個元素在哪個
寬度下跑掉了。全頁截圖供人眼比對，兩者都不進版控（見 `.gitignore`）：

- `--save` 寫入 `test/baseline/*.png` —— 基準當下的樣子
- 比對模式寫入 `test/current/*.png` —— **不會覆寫基準**，前後才能並排比對

現在的基準是 2026-11 改版後產生的，第二代頁面的基準已不適用、已整批取代。

每個寬度另外檢查頁首導覽列的每個項目是否**看得見**。手機寬度時導覽列是一排可以
左右滑動的分頁，後面幾項本來就在畫面外，所以「看得見」的定義是：在畫面內，
或位於一個本身在畫面內、可以水平捲動的容器裡（滑得到就算）。
`link-check.js` 只讀原始碼，看得出連結存在、看不出它被容器裁掉或推出畫面。

#### 基準是綁平台的

`test/baseline/` 只在**產生它的那個作業系統 + 瀏覽器**底下有意義。
macOS 與 Linux 對文字行框高度的取整不同，同一份 HTML 在兩邊量到的
文字元素高度會差 1–2px，而且沿著頁面往下累積成大量 y 位移 ——
實測拿 macOS 產生的基準在 Linux 上跑未改動的版本，5046 個元素裡 4046 個對不上。

那些差異全部是垂直方向的：**x 與寬度是 0 差異**，只有小字級的文字行矮了 1–2px。
換句話說那個數字不是「版面壞了」，是「基準換平台就不能用」。

所以 `--save` 會把瀏覽器版本與平台寫進 `test/baseline/.env.txt`，
比對時若對不上會先印一段警告，說明底下的差異多半不是真的跑版。
在別的平台上要判斷改動本身的影響，先用未改動的版本 `--save` 一次，再改、再比對。

量測前會用 `prefers-reduced-motion: reduce` 把動畫凍結在完整狀態，
所以每次量到的都是同一幀。這也是動畫本身支援的行為，不是測試專用的後門。

另外保險一層：同一次載入內間隔取兩張快照，凡是自己就會變的欄位一律標成 `*`，
比對時視為萬用字元 —— 讓量測器自己找出雜訊，不必人工維護忽略清單。
遮罩只增不減，因此連續兩次 `--save` 產生的基準完全相同。

## 字型

字型也是自架的。**渲染頁面所需的一切都由本站供應**，唯一的外部請求是 GA4
（`test/render-check.js` 的 `normal` 情境會驗證這件事：允許清單以外的網域一律判定失敗）。

這條規則換到的是三件事：

- **在受限網路裡顯示一致。** 買家坐在政府與金融的內網，對外連線常被過濾。
  頁面不依賴外部資源，那裡看到的畫面就跟外面一樣。
- **沒有第三方程式碼可以被抽換。** 供應鏈攻擊（例如 2024 年的 Polyfill.io）
  的前提是頁面會執行別人網域上的程式，這裡沒有。
- **量測穩定。** 測試不會因為外部網路而時好時壞。

GA4 是刻意的例外，因為它是**量測而非渲染** —— 它載不到的時候，頁面沒有任何改變。
它跟產品的「資料不出網」是兩回事：後者講的是客戶的錄音與逐字稿不離開客戶機房，
跟行銷網站的訪客分析無關。

```sh
python3 -m venv .venv && .venv/bin/pip install fonttools brotli
.venv/bin/python tools/build-fonts.py
```

> 若系統沒有 `python3-venv`（Debian/Ubuntu 要另外裝套件），可以改成裝到
> 獨立目錄，不動到系統的 Python：
>
> ```sh
> python3 -m pip install --target .pylibs fonttools brotli
> PYTHONPATH=.pylibs PATH=.pylibs/bin:$PATH python3 tools/build-fonts.py
> ```

腳本從 google/fonts 上游 repo 抓字型原始檔，子集化成站上實際用到的字元，輸出
`vendor/fonts/*.woff2` 與 `vendor/fonts/fonts.css`，頁面只 link 後者。
沒有被 `fonts.css` 引用到的舊產物會在每次執行時自動刪掉。

| 字型 | 用途 | 形式 | 大小 |
| --- | --- | --- | --- |
| Noto Serif TC | 中英文標題、直排標語、大數字（700、900）| 可變字型 700–900 | 359KB |
| Noto Sans TC | 中文內文（400、500、700）| 可變字型 400–700 | 277KB |
| Space Grotesk | 英文內文與按鈕（400、500、700）| 可變字型 400–700 | 18KB |
| IBM Plex Mono | 標籤、編號、時間戳（400、500）| 兩個靜態檔 | 共 13KB |

合計約 670KB（第二代約 340KB）。多出來的幾乎全是改版新加的 Noto Serif TC ——
標題改用明體是這次視覺的核心，所以接受這個代價。字元集隨文案增減，目前約 970 個字元、
其中約 860 個中日韓與全形符號；這兩個數字不必手動維護，執行腳本時會印出當下的值。
頁面 preload 的是 Noto Serif TC，因為首屏最大的元素是明體標題。

有幾件事踩過才知道：

- 原始檔要抓 **google/fonts 上游的完整檔**，不能走 Google Fonts 的 CSS API ——
  API 送的已經照 `unicode-range` 切成上百個分片，而我們要自己重新子集化，需要的是未分割的完整檔。
  以前靜態字重仍走 CSS API，2026-11 改成全部從上游 repo 取得，
  因為那支 API 在部分受限網路裡連不到。
- 先用 `fonttools varLib.instancer` 把 `wght` 軸砍到實際用到的範圍再子集化字元。
  用不到的字重端點連帶內插資料一起省掉。
- `@font-face` 的 `format()` 要寫 **`woff2`**，不是 `woff2-variations`。
  後者是過渡期寫法，部分瀏覽器不認得，會整條規則跳過 —— 字型直接不生效，而且不會報錯。

> ⚠️ **改過頁面文案後要重跑這支腳本**，否則新增的字會變成豆腐格。

字元集是從所有 HTML 的**原始碼**取聯集，不是從渲染結果 —— 這樣連只在
JavaScript 執行後才出現的字串也一定涵蓋得到。代價是原始碼裡的註解也會貢獻字元，
讓子集略大於實際所需。這個取捨是刻意的：漏字是使用者看得到的缺陷，多幾 KB 不是。

字型授權見 `vendor/fonts/LICENSE.md`（四套皆為 SIL OFL 1.1，允許子集化與散布）。

## 部署

將本資料夾內所有檔案（含 `.nojekyll`、`CNAME`、`vendor/` 與 `en/`）放到 repository 根目錄，
push 到 `main`，在 Settings → Pages 選擇 Deploy from a branch → `main` / `/ (root)`。

> `.nojekyll` 用於停用 Jekyll 處理，避免底線開頭的檔名被忽略。
> `CNAME` 是自訂網域 `voxmosa.com`；正式網址、sitemap 與分享縮圖都寫這個網域。

## 本機預覽

直接用瀏覽器點開 HTML（`file://`）即可，字型與腳本都走相對路徑，畫面切換也照常運作
（只是網址列不會跟著變）。若要模擬正式環境（網址會跟著換、`404.html` 會生效）：

```sh
python3 -m http.server 8000
```

頁面在完全離線的環境也能正常顯示。

## 後續可做的事

上線前：

- **表單補上個資告知**。表單收集姓名與 Email，依個資法通常要在收集時告知用途、
  保存方式與聯絡窗口。對一家主打資安合規的公司，這一行少了很顯眼。確切寫法請懂法規的人看過。
- **在 iPhone 與 Mac 的 Safari 實際看一次**。測試都跑在 Chrome 上；直排標語、
  直排裡橫放的「AI」、畫面滑入這幾個效果，Safari 的處理方式可能不同。
- **確認兩家合作單位的正式英文名稱**（意傳科技、瞬息科技），見[雙語](#雙語)。
- **確認對外信箱**。全站用 `how@voxmosa.com`；第二代頁面是 `hazel@voxmosa.com`。

內容面：

- **客語六腔的音檔樣本**，放在語言頁的客語區塊底下。同一句話六種腔調，各 10–15 秒。
  文字寫「六腔全數涵蓋」只是宣稱，聽到大埔腔與饒平腔的差別才是證據。
  做法上要維持站上的兩條硬性質：`<audio controls>` 不需要 JavaScript（不破壞
  有無 JS 內容相同），音檔自架於 repo 內（不對外發出請求）。六個檔案控制在 300KB 以內。
- **首頁的逐字稿換成真的錄音**。現在標示為「示意畫面」；播放真錄音時逐字稿跟著跑，
  比任何文案都更能證明「聽得懂臺灣」。
- **公開可重現的評測報告**。整個網站的核心主張是「不給行銷數字，給可重現的數字」，
  但 CER 對照表、方法論、原始音檔都還是「即將公開」。就算只先公開一個語言、一組測試集也好。
- **hero 的能力標籤換一格**（`封閉網路可運行／無按次 API 費用／模型自行訓練`）。
  第三項幾乎人人都能說，而族語 42 語、客語六腔是短期內拿不出第二家的東西。
- **加圖片**。全站零張 `<img>`，這是 Google 的 AI features 七項要求裡唯一失守的一項
  （「Supporting your textual content with high-quality images and videos」）。
  Google Images **支援 SVG**，所以站上的示意圖只要抽成 `.svg` 檔、用 `<img src alt>` 引用就能被索引。
- **`Organization` 補齊可查證的公司身分**：`address`、`telephone`、`foundingDate`。
  `legalName` 與 `taxID` 已經有了。要等對方提供資料。
- **團隊要具名**。Google 的 helpful content 指南問「Is it self-evident to your
  visitors who authored your content?」目前研究頁沒有指名任何人。

技術面：

- **每個檔案只放自己的內容**。見[頁面結構](#頁面結構)的取捨；改了之後
  `tools/sync-views.py` 就不需要了，頁面也會從 150KB 降到 30KB 左右。
- **字型 swap 的版面位移**。大標題先用系統字型畫、再換成 Noto Serif TC，換行可能改變並讓底下位移。
  用 `size-adjust` / `ascent-override` 給 fallback 字型做度量校正，大約六行 CSS。
- **10–11px 的標籤字**。等寬字的小標籤是品牌特徵，但在手機上偏小，可以考慮在窄螢幕放大 1px。

## 授權

網站本身採 Unlicense（見 `LICENSE`），釋出至公眾領域。

`vendor/` 內的第三方資源各自沿用原授權，不受上述影響：

- 四套字型 —— SIL OFL 1.1，詳見 `vendor/fonts/LICENSE.md`
