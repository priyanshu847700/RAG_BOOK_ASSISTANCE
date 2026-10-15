import streamlit as st
import os
import tempfile
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

st.title("📚 RAG Book Assistant")
st.write("Upload a book and ask questions from it.")

uploaded_file = st.file_uploader("Upload a PDF book", type="pdf")

if uploaded_file:

    if st.button("Create Vector Database"):

        with st.spinner("Processing book..."):

            with tempfile.NamedTemporaryFile(
                delete=False, suffix=".pdf"
            ) as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
                file_path = tmp_file.name

            try:
                docs = PyPDFLoader(file_path).load()

                splitter = RecursiveCharacterTextSplitter(
                    chunk_size=1000,
                    chunk_overlap=200
                )

                chunks = splitter.split_documents(docs)

                embedding_model = HuggingFaceEmbeddings(
                    model_name="sentence-transformers/all-MiniLM-L6-v2"
                )

                vector_store = Chroma(
                    persist_directory="./chroma_db",
                    embedding_function=embedding_model
                )

                vector_store.add_documents(chunks)

                st.success("Vector database created successfully!")

            finally:
                os.remove(file_path)


# Load existing vector database
if os.path.exists("./chroma_db"):

    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = Chroma(
        persist_directory="./chroma_db",
        embedding_function=embedding_model
    )

    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 4,
            "fetch_k": 10,
            "lambda_mult": 0.5
        }
    )

    llm = ChatGroq(model="openai/gpt-oss-120b")

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """You are a helpful AI assistant.
            Use ONLY the provided context to answer.
            If the answer is not present in the context,
            say: "I could not find the answer in the document."
            """
        ),
        (
            "human",
            """Context: {context}
            Question: {question}"""
        )
    ])

    st.divider()
    st.subheader("Ask Questions From the Book")

    query = st.text_input("Enter your question")

    if st.button("Get Answer") and query:

        with st.spinner("Finding your answer..."):

            docs = retriever.invoke(query)

            context = "\n\n".join(
                [doc.page_content for doc in docs]
            )

            final_prompt = prompt.invoke({
                "context": context,
                "question": query
            })

            response = llm.invoke(final_prompt)

        st.write("### AI Answer")
        st.write(response.content)