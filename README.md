# CampusEye：智慧教室人流分析與預測平台

## 組員
- 組長：温奕丞
- 組員：林珞碁
- 組員：金暐澄

## 專題簡介
CampusEye 是一個結合 Jetson Orin Nano、攝影機、Flask、PostgreSQL、爬蟲與資料分析的智慧教室人流分析與預測平台。

本系統透過攝影機擷取教室即時畫面，利用 AI 模型進行人數偵測與空間使用狀況分析，並結合網站爬蟲蒐集課表、活動資訊等外部資料，將資料儲存至 PostgreSQL 資料庫中，再透過 Flask 網站提供即時查詢、歷史分析與人流預測功能。

## 專題目標
1. 建立 GitHub 協作開發流程
2. 使用 Flask 建置網站後端
3. 使用 Render PostgreSQL 儲存系統資料
4. 使用爬蟲蒐集課表、活動或相關外部資訊
5. 分析教室人流變化與熱門時段
6. 加入 AI 模型提升分析能力
7. 串接 Jetson Orin Nano 與攝影機進行軟硬體整合

## 系統功能
- 教室即時人流偵測
- 教室歷史人流查詢
- 熱門時段分析
- 教室使用率分析
- 未來人流預測
- 外部資料整合分析
- 網頁介面展示結果

## 預計使用技術
- Python
- Flask
- PostgreSQL
- Render
- Selenium / Playwright
- OpenCV
- YOLO / 人流辨識模型
- HTML / CSS / JavaScript
- Git / GitHub

## 專案架構（暫定）
```text
campuseye-final-project/
├── README.md
├── app/
│   ├── app.py
│   ├── routes/
│   ├── templates/
│   ├── static/
│   └── models/
├── crawler/
├── analysis/
├── ai_model/
├── jetson_device/
├── docs/
└── requirements.txt