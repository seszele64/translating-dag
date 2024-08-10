import fitz  # PyMuPDF


def fetch_pdf_content(pdf_path):
    """
    Fetches the text content from a PDF file.

    Parameters:
    - pdf_path: Path to the PDF file.

    Returns:
    - A string containing the text content of the PDF.
    """
    try:
        # Open the PDF file
        doc = fitz.open(pdf_path)
        text = ""
        # Iterate through each page in the PDF
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)  # Load a page
            text += page.get_text()  # Extract text from the page
        doc.close()
        return text
    except Exception as e:
        print(f"Failed to fetch PDF content: {e}")
        return None
