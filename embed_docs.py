import os
import pickle
import faiss
from sentence_transformers import SentenceTransformer
import numpy as np

docs_path = "CI:CD Docs"
chunks, sources = [], []

# Chunk docs
for file in os.listdir(docs_path):
    with open(os.path.join(docs_path, file), "r", encoding="utf-8") as f:
        content = f.read()
        for i in range(0, len(content), 500):
            chunks.append(content[i:i+500])
            sources.append(file)

# Embed
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(chunks)
dimension = embeddings[0].shape[0]

# Create FAISS index
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings).astype("float32"))

# Save
faiss.write_index(index, "faiss_index.index")
with open("chunks_sources.pkl", "wb") as f:
    pickle.dump((chunks, sources), f)

print("✅ Index created and saved.")
