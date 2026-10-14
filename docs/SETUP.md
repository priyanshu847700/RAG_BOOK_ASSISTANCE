# Setup Guide

## Prerequisites

- Python 3.10 or newer; Python 3.11 is a practical default.
- A Groq API key.
- Internet access for API calls and the initial embedding-model download.

## macOS / Linux

```bash
git clone https://github.com/priyanshu847700/RAG_BOOK_ASSISTANCE.git
cd rag-book-assistant
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
cp .env.example .env
```

Open `.env`, replace the placeholder with your actual key, and run:

```bash
streamlit run app.py
```

## Windows PowerShell

```powershell
git clone https://github.com/priyanshu847700/RAG_BOOK_ASSISTANCE.git
cd rag-book-assistant
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

Edit `.env` with your key, then run:

```powershell
streamlit run app.py
```

## GitHub Safety Checklist

- Keep `.env` out of Git.
- Commit `.env.example`, not the real secret.
- Do not commit private books or the generated `chroma_db/` folder.
- Check `git status` before pushing.

## Push to GitHub

Create an empty repository on GitHub, then from the project directory:

```bash
git init
git add .
git commit -m "Initial commit: RAG Book Assistant"
git branch -M main
git remote add origin https://github.com/priyanshu847700/RAG_BOOK_ASSISTANCE.git
git push -u origin main
```

Replace the example GitHub URL with your own repository URL.
