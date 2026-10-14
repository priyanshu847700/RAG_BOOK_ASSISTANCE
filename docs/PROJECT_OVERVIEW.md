# Project Overview

## Goal

RAG Book Assistant lets a user ask questions about a PDF book and receive answers grounded in retrieved passages from that book.

## Main Components

| Component | Responsibility |
|---|---|
| Streamlit | Upload interface and question/answer UI |
| PyPDFLoader | Extracts PDF text and page metadata |
| RecursiveCharacterTextSplitter | Splits extracted text into overlapping chunks |
| Hugging Face `all-MiniLM-L6-v2` | Creates embeddings locally |
| ChromaDB | Persists chunk embeddings and supports similarity retrieval |
| LangChain retriever with MMR | Retrieves a diverse set of relevant chunks |
| Groq via `ChatGroq` | Generates a response from the retrieved context |

## Request Flow

```text
PDF upload
   ↓
Extract PDF text
   ↓
Split into chunks
   ↓
Create embeddings
   ↓
Save chunks in ChromaDB
   ↓
User asks a question
   ↓
Retrieve relevant chunks (MMR)
   ↓
Send context + question to Groq model
   ↓
Display answer in Streamlit
```

## Current Design Decisions

- Chunk size: 1,000 characters.
- Chunk overlap: 200 characters.
- Retrieval: MMR with `k=4`, `fetch_k=10`, and `lambda_mult=0.5`.
- Embedding model: `sentence-transformers/all-MiniLM-L6-v2`.
- The prompt instructs the LLM to use only retrieved context and explicitly say when the answer is absent.

## Known Limitations

- The current implementation uses one persistent local Chroma directory, so different books can share the same stored collection.
- Reprocessing the same PDF may add duplicate chunks.
- The app does not show retrieved source passages or page citations in the answer.
- Scanned PDFs require OCR, which is not implemented.
