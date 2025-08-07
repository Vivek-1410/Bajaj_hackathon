import os
import fitz  

def extract_text_from_pdfs(pdf_folder_path):
    combined_text = ""
    for filename in sorted(os.listdir(pdf_folder_path)):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder_path, filename)
            doc = fitz.open(pdf_path)
            text = "\n".join([page.get_text() for page in doc])
            combined_text += f"\n\n--- Content from {filename} ---\n\n{text}"
    return combined_text
