import json
import subprocess

# 讀取水果 JSON 資料
with open("fruit_dataset.json", "r", encoding="utf-8") as file:
    fruit_data = json.load(file)

# 取得水果的營養資訊
selected_fruit = "Apple"  # 這裡可以換成你的水果類型
fruit_info = next((f for f in fruit_data if f["fruit"].lower() == selected_fruit.lower()), None)

if fruit_info:
    nutrition_info = fruit_info["nutrition"]
    health_benefits = fruit_info["health_benefits"]
else:
    nutrition_info = "找不到該水果的營養資訊。"
    health_benefits = ""

# 設定水果圖片的完整路徑
image_path = "C:/Users/HRCla/Desktop/ollama/images/apple_fruit/image_1.jpg"

# 建立 LLaVA 指令，傳遞圖片並請求營養分析
command = f'ollama run llava "你是一位專業的營養師，請分析這張圖片，並提供該水果的營養資訊與健康建議：\n{nutrition_info}\n{health_benefits}" "{image_path}"'

# 執行命令並獲取輸出
result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding="utf-8")

# 顯示 LLaVA 回答
print("LLaVA 回答:", result.stdout)
