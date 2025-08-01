import fitz  # PyMuPDF

def extract_chunks_from_pdf(uploaded_file, chunk_size=500):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    return chunks
