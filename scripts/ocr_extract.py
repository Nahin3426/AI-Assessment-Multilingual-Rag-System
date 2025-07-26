from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import os

PDF_PATH = "../data/HSC26-Bangla1st-Paper.pdf"
OUTPUT_PATH = "C:\Project works\AI RAG\data\ocr_extracted_text.txt"
LANG = "ben+eng"  # Tesseract will try both Bengali and English

def extract_text_with_tesseract(pdf_path, lang="ben"):
    print("📄 Converting PDF pages to images...")
    pages = convert_from_path(pdf_path, dpi=300)
    full_text = ""

    for i, page in enumerate(pages):
        print(f"🔍 OCR on page {i+1}/{len(pages)}...")
        text = pytesseract.image_to_string(page, lang=lang)
        full_text += text + "\n\n"

    return full_text.strip()

if __name__ == "__main__":
    text = extract_text_with_tesseract(PDF_PATH, lang=LANG)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"✅ OCR text saved to: {OUTPUT_PATH}")
