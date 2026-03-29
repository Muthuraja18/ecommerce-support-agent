from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from src.ingestion import load_documents, split_docs

def build_db():
    docs = load_documents()
    chunks = split_docs(docs)

    embeddings = HuggingFaceEmbeddings()
    db = FAISS.from_documents(chunks, embeddings)

    db.save_local("db/faiss_index")

def load_db():
    embeddings = HuggingFaceEmbeddings()
    return FAISS.load_local("db/faiss_index", embeddings, allow_dangerous_deserialization=True)

if __name__ == "__main__":
    print("🚀 Building FAISS index...")

    docs = load_documents("data/policies")
    print(f"Loaded {len(docs)} documents")

    chunks = split_docs(docs)
    print(f"Created {len(chunks)} chunks")

    embeddings = HuggingFaceEmbeddings()
    db = FAISS.from_documents(chunks, embeddings)

    db.save_local("faiss_index")

    print("✅ FAISS index created successfully!")