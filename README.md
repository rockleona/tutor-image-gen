---
marp: true
---

# 天氣預報

---

1. 事前要準備甚麼東西
   1. 圖片資料 : Unsplash **API**
   2. 天氣資料 : [氣象局開放資料 **API**](https://opendata.cwa.gov.tw/dataset/forecast/F-C0032-001)
   3. Python : 
      + requests (HTTP 模組，取得網路上的資料)
      + PIL (又稱 pillow，圖片編輯模組)

---

2. 執行的過程要怎麼處理
   1. 取得天氣資料 : 36 小時內的天氣預測 (麻煩!)
   2. 取得照片資料 : 
      1. 呼叫 Unsplash API : **隨機取得背景圖**
      2. 取得照片的網址
      3. 下載網址內的照片
      4. 取得照片檔案

---

   3. 在照片上寫上天氣資料
      + 台南市
      + 今天日期、上午or下午
      + Wx(天氣現象)
      + MaxT(最高溫度)
      + MinT(最低溫度)
      + CI(舒適度)
      + PoP(降雨機率)
3. 圖片的儲存
4. 定時、定期的更新資料 : 請 GitHub Action 處理

---