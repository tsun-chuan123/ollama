import subprocess
import re

# **設定水果圖片的完整路徑**
image_path = "C:/Users/HRCla/Desktop/ollama/images/cherry_fruit/image_12.jpg"

# **LLaVA 只回應水果名稱**
llava_prompt = """
請分析這張圖片，並只輸出單一水果名稱（例如 'Apple', 'Banana', 'Grape', 'Kiwi', 'Mango', 'Orange', 'Strawberry', 'Chickoo', 'Cherry'）。
不要多餘的字、標點、數字或解釋。若無法辨識，請盡量猜類似水果名稱。
若你想列出多個可能，只能擇一最有信心的名稱。
若你不確定，請盡量猜 'Chickoo'。
"""

# **執行 LLaVA，確保回傳純水果名稱**
command = ["ollama", "run", "llava", llava_prompt, image_path]
result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")

# **取得 LLaVA 回應並清理格式**
fruit_name = result.stdout.strip()

# **移除數字、標點符號，確保只保留水果名稱**
fruit_name = re.sub(r'[^A-Za-z ]', '', fruit_name).strip()

# **處理可能的複數轉單數（例如 Bananas → Banana）**
if fruit_name.endswith("s") and not fruit_name.lower() in ["cherries"]:
    fruit_name = fruit_name[:-1]

# **將識別出的水果名稱存入檔案**
with open("recognized_fruit.txt", "w", encoding="utf-8") as file:
    file.write(fruit_name)

# **顯示結果**
print(f"圖片中的水果是：{fruit_name}")
