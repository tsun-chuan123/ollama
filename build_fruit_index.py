import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# 讀取水果 JSON 資料
json_path = "C:/Users/HRCla/Desktop/ollama/fruit_dataset.json"
faiss_path = "C:/Users/HRCla/Desktop/ollama/fruit_index.faiss"

try:
    with open(json_path, "r", encoding="utf-8") as file:
        fruit_data = json.load(file)
except FileNotFoundError:
    print(f"❌ 找不到 {json_path}，請確認 JSON 檔案是否存在。")
    exit(1)

# 使用 SentenceTransformer 來將文字轉成向量
model = SentenceTransformer("all-MiniLM-L6-v2")

# 建立向量資料庫（合併水果名稱 + 營養資訊 + 健康說明）
text_data = [f"{f['fruit']} - {f['nutrition']} {f['health_benefits']}" for f in fruit_data]

# 轉換成向量
vectors = model.encode(text_data)

# 初始化 FAISS 向量索引
index = faiss.IndexFlatL2(vectors.shape[1])
index.add(np.array(vectors))

# 儲存索引
faiss.write_index(index, faiss_path)

print(f"✅ 向量索引建立完成！已儲存為 {faiss_path}")
