# 📚 RAG Book Assistant

A simple **Retrieval-Augmented Generation (RAG)** app that lets you upload a PDF book and ask questions about its content. The app extracts text from the PDF, splits it into chunks, creates embeddings, stores them in ChromaDB, retrieves relevant passages, and asks a Groq-hosted language model to answer using that context.

## ✨ Features

- Upload a PDF book through a Streamlit interface.
- Extract PDF text with `PyPDFLoader`.
- Split text into chunks using `RecursiveCharacterTextSplitter`.
- Generate embeddings with `sentence-transformers/all-MiniLM-L6-v2`.
- Store and retrieve chunks with ChromaDB.
- Use Maximum Marginal Relevance (MMR) retrieval to select relevant context.
- Generate context-grounded answers with a Groq chat model.
- Instruct the model to say when the answer is not found in the document.

## 🧰 Tech Stack

- Python
- Streamlit
- LangChain
- Groq API
- Hugging Face Sentence Transformers
- ChromaDB
- PyPDF

## 📁 Project Structure

```text
rag-book-assistant/
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── LICENSE
├── README.md
└── docs/
    ├── PROJECT_OVERVIEW.md
    └── SETUP.md
```

The `chroma_db/` directory is created locally when the app builds its vector database. It is ignored by Git because it contains generated data.

## ⚙️ Requirements

- Python 3.10 or newer (Python 3.11 is a good default).
- A Groq API key.
- Internet access for the Groq API and the first download of the embedding model.

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/rag-book-assistant.git
cd rag-book-assistant
```

Replace `YOUR-USERNAME` with your GitHub username and adjust the repository name if needed.

### 2. Create and activate a virtual environment

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows PowerShell**
```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure your API key

Copy `.env.example` to `.env` and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get a key from the [Groq Console](https://console.groq.com/keys). **Never commit your `.env` file or expose your API key.**

### 5. Run the app

```bash
streamlit run app.py
```

Streamlit will show a local URL, usually `http://localhost:8501`.

### 6. Use the app

1. Upload a PDF book.
2. Click **Create Vector Database** and wait for processing to finish.
3. Enter a question in the question box.
4. Click **Get Answer** to see the response.

## 🧠 How It Works

1. **Load:** `PyPDFLoader` extracts text and page metadata from the PDF.
2. **Split:** The text is split into chunks of 1,000 characters with 200 characters of overlap.
3. **Embed:** `all-MiniLM-L6-v2` converts chunks into vector embeddings.
4. **Store:** ChromaDB stores the chunks and their embeddings in `./chroma_db`.
5. **Retrieve:** MMR retrieves up to four relevant chunks from a candidate set of ten.
6. **Generate:** The Groq chat model receives the retrieved context and question, then generates an answer.

## 🔐 Environment Variables

| Variable | Required | Description |
|---|---|---|
| `GROQ_API_KEY` | Yes | API key used by `ChatGroq`. |

## ⚠️ Notes and Limitations

- **Model availability:** The app currently uses `openai/gpt-oss-120b` through Groq. Model availability and naming can change. If Groq reports that the model is unavailable, select a currently supported model in the Groq Console and update the `ChatGroq(model=...)` line in `app.py`.
- **Local storage:** The vector database is saved in `./chroma_db`. This starter version reuses that directory between runs. If you process multiple books, their chunks may be mixed together; clear the directory or add per-book collection management before using it for separate books.
- **Duplicate chunks:** Clicking **Create Vector Database** repeatedly can add the same PDF chunks again. For a more robust version, add collection reset or document-specific IDs.
- **PDF quality:** Scanned PDFs may need OCR; this version extracts text and does not perform OCR.
- **Answer quality:** RAG can still produce incomplete or incorrect answers. Verify important information against the source book.
- **Privacy:** Uploaded content is processed locally for embeddings and storage, while retrieved text is sent to the configured Groq API for answer generation. Do not upload documents you are not allowed to process or share.

## 🛠️ Troubleshooting

- **`GROQ_API_KEY` error:** Check that `.env` exists in the project root and contains a valid key.
- **Model not found / unavailable:** Update the model ID in `app.py` to one currently supported by your Groq account.
- **Missing Python package:** Activate the project virtual environment and run `pip install -r requirements.txt`.
- **No answer interface appears:** Build the vector database first; the app shows the question interface when `./chroma_db` exists.
- **PDF has no extracted text:** The PDF may be scanned or image-only and require OCR.

## 🗺️ Possible Improvements

- Keep separate Chroma collections for each uploaded book.
- Add a **Clear / Rebuild Database** button.
- Display source page numbers with answers.
- Add chat history and streaming responses.
- Support DOCX, TXT, and website sources.
- Add OCR support for scanned PDFs.
- Add tests and deploy the app.

## 📸 Screenshots

Add screenshots of the app here after running it, for example:

```markdown
![PDF upload screen](screenshots/upload-screen.png)
![Question and answer screen](screenshots/qa-screen.png)
```

## 🤝 Contributing

Issues and pull requests are welcome. For substantial changes, open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE).

---

If this project helps you, consider giving the repository a ⭐ on GitHub.
