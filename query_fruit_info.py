import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# **讀取 `identify_fruit.py` 產生的水果名稱**
with open("recognized_fruit.txt", "r", encoding="utf-8") as file:
    fruit_name = file.read().strip()

# 讀取 FAISS 索引
index = faiss.read_index("C:/Users/HRCla/Desktop/ollama/fruit_index.faiss")
model = SentenceTransformer("all-MiniLM-L6-v2")

# 讀取水果 JSON 資料
with open("C:/Users/HRCla/Desktop/ollama/fruit_dataset.json", "r", encoding="utf-8") as file:
    fruit_data = json.load(file)

# 在 FAISS 中檢索最相關的營養資訊
query_vector = model.encode([fruit_name])
_, nearest_idx = index.search(np.array(query_vector), 1)

retrieved_info = fruit_data[nearest_idx[0][0]]

# **修正：確保存儲時 UTF-8 正確**
with open("retrieved_fruit_info.json", "w", encoding="utf-8") as file:
    json.dump(retrieved_info, file, ensure_ascii=False, indent=4)

# 顯示檢索結果
print(f"找到的水果資訊：\n名稱：{retrieved_info['fruit']}\n營養資訊：{retrieved_info['nutrition']}\n健康說明：{retrieved_info['health_benefits']}")
