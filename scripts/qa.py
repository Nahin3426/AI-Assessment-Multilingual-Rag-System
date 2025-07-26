# qa.py
from llama_cpp import Llama
from query_pipeline import get_top_chunks

# Load your local model
llm = Llama(
    model_path= r"C:\Project works\AI RAG\model\llama-3-8b-bangla-GGUF-Q4_K_M-unsloth.Q4_K_M.gguf",
    n_ctx=2048,
    n_threads=6,
    n_batch=64,
    seed=42
)
print("✅ Local Bangla LLaMA model loaded")



def generate_answer(query: str, k: int = 3) -> str:
    chunks = get_top_chunks(query, k=k)
    context = "\n\n".join(chunks)

    print("\n📄 Retrieved Context:\n", context)  # 👈 Add this line

    prompt = f"Context:\n{context}\n\nQuestion:\n{query}\n\nAnswer:"
    output = llm(prompt, max_tokens=256, temperature=0.3)
    return output["choices"][0]["text"].strip()
