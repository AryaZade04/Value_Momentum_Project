#older
import fitz  # PyMuPDF

def extract_text_from_pdf(file):
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

import fitz  # PyMuPDF

def extract_text_from_pdf(file):
    """
    Extract clean text from a PDF file using PyMuPDF.
    Handles multiple pages and removes extra spaces or line breaks.
    """
    text = ""

    # Open the PDF directly from uploaded file (stream)
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page_num, page in enumerate(doc, start=1):
            page_text = page.get_text("text").strip()
            text += f"\n--- Page {page_num} ---\n{page_text}\n"

    # Clean up unwanted whitespace and multiple newlines
    clean_text = " ".join(text.split())

    return clean_text
