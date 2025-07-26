from llama_cpp import Llama

llm = Llama(
    model_path=r"C:\Project works\AI RAG\model\llama-3-8b-bangla-GGUF-Q4_K_M-unsloth.Q4_K_M.gguf",
    n_ctx=2048,
    n_threads=6,
    n_batch=64
)

prompt = "Q: বাংলাদেশ কবে স্বাধীনতা লাভ করে?\nA:"
response = llm(prompt, max_tokens=100, temperature=0.7)
print(response["choices"][0]["text"].strip())

