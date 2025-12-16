本專案為 Python Tkinter 佈局管理練習，目標是熟悉並比較三種常見的版面配置方式：

- `pack`
- `grid`
- `place`

三個程式需使用不同的佈局管理方式，但最終顯示的視窗外觀必須完全一致。

---

## 專案結構

tk-layout-quiz4/
├── tk_pack.py
├── tk_grid.py
├── tk_place.py
├── .gitattributes
├── .gitignore
├── LICENSE
└── README.md

yaml
複製程式碼

---

## 視窗規格

- 視窗大小：`400 x 300`
- 視窗不可調整大小
- Tkinter 內建函式庫，無需額外安裝套件

---

## 介面配置說明

### 區塊結構（共 5 個 Frame）

| 區塊 | 顏色 | 尺寸 / 比例 |
|----|----|----|
| 左側欄 | lightgreen | 寬 40px（10%） |
| 右側欄 | lightblue | 寬 40px（10%） |
| 上層 | red | 高 60px（20%） |
| 中層 | yellow | 填滿剩餘空間 |
| 下層 | blue | 高 30px（10%） |

---

## 標籤（Label）設定

- 位置：紅色（Top）區塊內
- 文字內容：
  - `left`
  - `center`
  - `Right`
- 樣式：
  - 背景色：white
  - 文字色：black
- 對齊方式：靠上（Top / North）

---

## 各程式說明

### tk_pack.py
- 使用 `pack()` 進行佈局
- 利用 `side` 與 `fill` 控制左右與上下配置
- 對固定高度區塊使用 `pack_propagate(False)`

### tk_grid.py
- 使用 `grid()` 搭配 `rowconfigure`、`columnconfigure`
- 透過 `weight` 分配剩餘空間
- 使用 `sticky='nsew'` 控制延展方向

### tk_place.py
- 使用 `place()` 搭配相對比例配置
- 透過 `relx`、`rely`、`relwidth`、`relheight` 計算區塊比例
- 符合響應式設計概念

---

## 執行方式

請使用 Python 3 執行以下任一檔案：

```bash
python tk_pack.py
python tk_grid.py
python tk_place.py