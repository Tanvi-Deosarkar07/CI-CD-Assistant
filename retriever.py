import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index("faiss_index.index")
with open("chunks_sources.pkl", "rb") as f:
    chunks, sources = pickle.load(f)

def retrieve(query, top_k=3):
    query_vec = model.encode([query])
    query_vec = np.array(query_vec).astype("float32")
    D, I = index.search(query_vec, top_k)
    return [chunks[i] for i in I[0]], [sources[i] for i in I[0]]
