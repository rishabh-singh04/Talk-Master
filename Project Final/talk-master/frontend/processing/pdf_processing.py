import fitz  # PyMuPDF
import os  # <-- Add this line

def extract_text_from_pdf(pdf_path):
    if not os.path.exists(pdf_path):  # Check if the file exists
        raise FileNotFoundError(f"File not found: {pdf_path}")

    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text("text") + "\n"
    return text.strip()
