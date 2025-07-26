from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_bangla_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def chunk_text(text, chunk_size=500, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ".", "।", "?"],  # Include Bangla "।"
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_text(text)

def build_index():
    print("📄 Loading Bangla OCR text...")
    bangla_text = load_bangla_text("../data/ocr_extracted_text.txt")

    print("🔗 Splitting text into chunks...")
    chunks = chunk_text(bangla_text)
    print(f"📦 Total chunks: {len(chunks)}")

    print("📈 Generating embeddings...")
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/distiluse-base-multilingual-cased-v1")

    vectorstore = Chroma.from_texts(chunks, embedding_model, persist_directory="vectorstore/")

    print("✅ Vectorstore built and saved.")

if __name__ == "__main__":
    build_index()
