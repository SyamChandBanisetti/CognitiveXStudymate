import streamlit as st
from utils.pdf_loader import extract_chunks_from_pdf
from utils.vector_store import create_faiss_index, retrieve_chunks
from utils.qa_engine import ask_question

st.title("📚 StudyMate – AI Study Assistant")

uploaded_files = st.file_uploader("Upload your study PDFs", accept_multiple_files=True, type=["pdf"])
question = st.text_input("Ask a question based on your documents")

if uploaded_files and question:
    st.write("🔄 Processing PDFs...")
    all_chunks = []

    for file in uploaded_files:
        chunks = extract_chunks_from_pdf(file)
        all_chunks.extend(chunks)

    st.success("✅ Text extracted and chunked.")
    
    st.write("🔍 Retrieving relevant content...")
    index, chunk_texts = create_faiss_index(all_chunks)
    top_chunks = retrieve_chunks(index, chunk_texts, question)

    st.write("💬 Generating answer...")
    answer = ask_question(top_chunks, question)

    st.subheader("Answer:")
    st.write(answer)
