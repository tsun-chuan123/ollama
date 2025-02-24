import subprocess
import json
import sys

try:
    with open("recognized_fruit.txt", "r", encoding="utf-8") as file:
        fruit_name = file.read().strip()
except FileNotFoundError:
    print("❌ 找不到 `recognized_fruit.txt`，請先執行 `identify_fruit.py`。")
    sys.exit(1)

try:
    with open("retrieved_fruit_info.json", "r", encoding="utf-8") as file:
        retrieved_info = json.load(file)
except FileNotFoundError:
    print("❌ 找不到 `retrieved_fruit_info.json`，請先執行 `query_fruit_info.py`。")
    sys.exit(1)

if not retrieved_info:
    print("❌ `retrieved_fruit_info.json` 內容為空！")
    sys.exit(1)

final_prompt = f"""
You are a nutritionist specializing in fruits. Below is the verified nutritional information for "{retrieved_info['fruit']}".

---
**Nutritional Information (Per 100g):**
{retrieved_info['nutrition']}

**Health Benefits:**
{retrieved_info['health_benefits']}
---

Instructions:
1. List the nutritional information and health benefits exactly as provided.
2. Do not add any new details not found in the data.
3. If explicitly asked about anything not in the data, respond with: "I only provide nutritional information based on the given data."
"""


# print("=== [DEBUG] Prompt for LLaVA ===")
# print(final_prompt)
# print("=================================\n")

# 改用 "ollama run" 而不是 "ollama prompt"
command = [
    "ollama",
    "run",
    "llava",  # 若你的模型是 "llava:latest"，可寫 "llava:latest"
    final_prompt
]

result = subprocess.run(
    command,
    capture_output=True,
    text=True,
    encoding="utf-8",
    errors="replace"  # 若有無法解碼的字元，替換為 �
)

print("=== LLaVA 回答 ===")
print(result.stdout)

if result.stderr:
    print("\n[stderr from Ollama]:")
    print(result.stderr)
