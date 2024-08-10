from src.fetcher import fetch_pdf_content

pdf_path = "path/to/your/document.pdf"
content = fetch_pdf_content(pdf_path)

if content:
    # Print the first 100 characters of the content
    print("Content:", content[:100])
else:
    print("Failed to fetch content.")
