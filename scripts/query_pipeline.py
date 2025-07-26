from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# Use the same model as in build_index.py
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/distiluse-base-multilingual-cased-v1")
vectorstore = Chroma(persist_directory="vectorstore/", embedding_function=embedding_model)

def get_top_chunks(query, k=3):
    results = vectorstore.similarity_search(query, k=k)
    return [doc.page_content for doc in results]
