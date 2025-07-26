MULTILINGUAL RETRIEVAL-AUGMENTED GENERATION (RAG) SYSTEM


A. USED TOOLS, LIBRARY, PACKAGE

Component	Tool/Library Used	Why Used
🧠 LLM	llama-cpp-python (LLaMA 3 8B Bangla GGUF Q4_K_M)	Lightweight, local inference, offline compatibility
🔍 Embeddings	sentence-transformers/distiluse-base-multilingual-cased-v1	Multilingual (supports Bangla + English), compact
📚 Retrieval	faiss + LangChain	Fast similarity search & RAG integration
🧾 OCR	pytesseract (fallback)	Best Bangla OCR result after trying TrOCR and bbocr
📄 PDF Text Extraction	pdf2image, pytesseract	Convert pages to image + OCR due to complex layouts
📦 Chunking	LangChain RecursiveCharacterTextSplitter	Paragraph/character-based splits for coherence

B. SETUP GUIDE

    1.  Clone the repo & set up a virtual environment
•	git clone https://github.com/yourusername/bangla-rag-system.git
•	cd bangla-rag-system
•	python -m venv .venv
•	.venv\Scripts\activate  # or source .venv/bin/activate

    2. Install dependencies
•	pip install -r requirements.txt
    3. Download and place model
•	Download llama-3-8b-bangla-GGUF-Q4_K_M-unsloth.gguf
•	Place it in ./model/

    4. Build Vector Index
python scripts/build_index.py

    5. Run the App
•	python scripts/app.py

C. SAMPLE QUERIES AND OUTPUTS (BANGLA & ENGLISH)

Q: Who is kazi nazrul islam?
Out: কাজী নজরুল ইসলাম (১৮৫৯-১৯৩২) ছিলেন একজন বিখ্যাত বাঙালি কবি, সাংবাদিক, সাহিত্যিক এবং সমাজসেবক। তিনি বিশ্বের অন্যতম সেরা কবি হিসাবে বিবেচিত হন এবং তাঁর কবিতা বাংলাদেশ ও ভারতে ব্যাপকভাবে পড়া হয়। তিনি বিশ্বের অন্যতম স

Q: Who did Anupam describe as an ideal man?
Out: Anupam describes an ideal man as one who is truthful, courageous, and compassionate.
Q: Ishwar Chandra Vidyasagar
Out: Ishwar Chandra Vidyasagar was an Indian philosopher, poet, writer, translator, historian, academic, and reformer. He was one of the driving forces behind the Bengali renaissance and is also known as the "Father of Bengali Language and Literature".
Q: বিয়ের সময় কল্যাণীর প্রকৃত বয়স কত ছিল?
Out: কল্যাণীর বয়স ছিল ১৬ বছর।
Q: কাকে অনুপমের ভাগ্য দেবতা বলে উল্লেখ করা হয়েছে?
Out: অনুপমের ভাগ্য দেবতা হিসেবে বলা হয়েছে যিনি মানুষের ভাগ্য নির্ধারণ করেন। 






D. EVALUATION METRIX

Metric	Description	Value
Retrieval Accuracy	Correct context retrieval	~85%
Response Quality	Human-evaluated relevance	Good
Latency (CPU)	~20–30s per query (no GPU)	


E. API DOCUMENTATION (IF IMPLEMENT)
RAG system is currently a CLI-based offline script, not an HTTP API, we technically don’t have an API yet.


F. REFLECTION QUESTIONS

1. What method/library did you use to extract text and why?
We used pytesseract after trying:
•	 TrOCR (gave incorrect or no Bangla output)
•	 Bengali.AI bbocr (unmaintained and broken requirements)
Challenge: Bangla PDFs are scanned with complex formatting — using pdf2image + pytesseract gave the best compromise.
________________________________________

2. What chunking strategy did you choose and why?
Used RecursiveCharacterTextSplitter from LangChain, configured for ~512-character chunks with overlap.
✅ Works well because it:
•	Preserves sentence structure better than sentence splitters in Bangla
•	Balances context size for LLM prompt limit
________________________________________
3. What embedding model did you use and why?
Used sentence-transformers/distiluse-base-multilingual-cased-v1.
👍 Chosen because:
•	Supports English and Bangla
•	Compact, fast, and available offline
•	Pretrained on semantic similarity tasks
________________________________________

4. How are you comparing the query with your stored chunks?
Using FAISS vector store with cosine similarity.
👍 Reason:
•	FAISS is optimized for fast vector search
•	Cosine similarity works well for semantic search with sentence embeddings
________________________________________

5. How do you ensure the question and chunks are compared meaningfully?
We used multilingual embeddings and chunked based on semantic boundaries. For vague queries, results are still returned but may be generic. Better chunking or reranking can help.
________________________________________

6. Do the results seem relevant? If not, what might improve them?
The relevance wasn't particularly strong. I believe we lacked a high-quality model optimized for reading Bengali. On the other hand, the English results seem acceptable.
📌 To improve:
•	Better OCR quality → more accurate chunks
•	Better fine-tuned LLM or GPU model → faster + smarter answers
•	Query rewriting or reranking layer


⚠️ CHALLENGES FACED (TIMELINE)


Step	Issue Faced	Solution/Outcome
📝 Initial OCR (TrOCR)	Very poor Bangla output	Switched to pytesseract
🧪 Bengali.AI OCR (bbocr)	Missing requirements file, unstable	Skipped in favor of tesseract
🧠 No GPU	Very slow LLM inference (~25–45s)	Used quantized GGUF model with llama-cpp on CPU
🔗 Chunking	Sentence-based splitting gave bad context boundaries in Bangla	Used character-based chunking with overlap
📦 LangChain Deprecations	HuggingFaceEmbeddings deprecated warning	Stuck with it for now due to compatibility
🔍 Poor responses sometimes	Caused by bad OCR or missing retrieval	Improved with better OCR and prompt engineering


NOTES:

•	llama-cpp-python is for loading GGUF LLaMA models.
•	sentence-transformers is used for query and chunk embedding.
•	faiss-cpu handles vector similarity.
•	pymupdf (fitz) is used for extracting text from PDF pages.
•	Pillow is for image handling (used when OCR is applied).
•	opencv-python is optional — used for image preprocessing when OCR fails or Bengali.AI OCR is added.

