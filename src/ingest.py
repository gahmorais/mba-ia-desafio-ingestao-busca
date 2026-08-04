from langchain_postgres.vectorstores import PGVector
from botocore import model
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from pathlib import Path
from h11._abnf import chunk_size
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
import os
from dotenv import load_dotenv

load_dotenv()


PDF_PATH = os.getenv("PDF_PATH")

def ingest_pdf():

    for k in ("OPENAI_API_KEY", "PG_VECTOR_COLLECTION_NAME", "DATABASE_URL"):
        if not os.getenv(k):
            raise RuntimeError(f"Environment variable {k} is not set")
    
    current_dir = Path(__file__).parent
    pdf_path = current_dir / PDF_PATH
    docs = PyPDFLoader(pdf_path)
    splits = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=150, 
        add_start_index=False).split_documents(docs)
    if not splits:
        raise SystemExit(0)
    
    enriched = [
        Document(
            page_content=d.page_content,metadata={k:v for k,v in d.metadata.items() if v not in ("",None)})
        for d in splits
    ]

    ids = [f"doc-{i}" for i in range(len(enriched))]

    embeddings = OpenAIEmbeddings(model=os.getenv("OPENAI_EMBEDDING_MODEL","text-embedding-3-small"))

    store = PGVector(
        embeddings=embeddings,
        collection_name=os.getenv("PG_VECTOR_COLLECTION_NAME"),
        connection=os.getenv("DATABASE_URL"),
        use_jsonb=True
    )

    store.add_documents(docs=enriched,ids=ids)

def _clean_metadata(metadata: dict) -> dict:
    return {k: v for k, v in metadata.items() if v not in ("",None)}

if __name__ == "__main__":
    ingest_pdf()