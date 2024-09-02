

#i ran it on colab, so remove the ! before pip before running on machine.

!pip install transformers torch pymupdf
!apt install tesseract-ocr
!apt install libtesseract-dev
!pip install Pillow
!pip install pytesseract
!pip install pdf2image matplotlib
!apt-get install poppler-utils
!pip install pdf2image

import fitz  # PyMuPDF
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import difflib
import re
import os

# Path to your PDF and output text files
pdf_path = "document.pdf"
ocr_text_path = "ocr_textfile.txt"
pdf_text_path = "pdf_textfile.txt"
differences_path = "differences.txt"

# Function to extract text from image using Tesseract
def extract_text_from_image(image):
    text = pytesseract.image_to_string(image, lang='eng', config='--psm 6')
    return text

# Extract text from PDF using OCR
def extract_text_with_ocr(pdf_path, output_txt_path):
    images = convert_from_path(pdf_path)
    all_text = [extract_text_from_image(image) for image in images]
    full_text = "\n".join(all_text)

    with open(output_txt_path, 'w', encoding='utf-8') as file:
        file.write(full_text)

    print(f"OCR text extracted and saved to {output_txt_path}")

# Extract text from PDF using PyMuPDF
def extract_text_from_pdf(pdf_path, output_txt_path):
    pdf_document = fitz.open(pdf_path)
    all_text = [pdf_document.load_page(page_number).get_text() for page_number in range(len(pdf_document))]
    full_text = "\n".join(all_text)

    with open(output_txt_path, 'w', encoding='utf-8') as file:
        file.write(full_text)

    print(f"PDF text extracted and saved to {output_txt_path}")

# Normalize text by removing extra whitespace and new lines
def normalize_text(text):
    return re.sub(r'\s+', ' ', text).strip()

# Preprocess text (remove patterns like "(1)", "(2)", etc.)
def preprocess_text(text):
    text = re.sub(r'\(\d+\)', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Compare two texts and find differences
def compare_texts(text1, text2):
    # Preprocess the texts
    text1 = preprocess_text(text1)
    text2 = preprocess_text(text2)

    words1 = text1.split()
    words2 = text2.split()

    longer_words, shorter_words = (words1, words2) if len(words1) >= len(words2) else (words2, words1)

    # Prepare result list
    result = []

    mismatch_count = 0

    # Compare words and mark mismatches
    for i, word in enumerate(longer_words):
        if i < len(shorter_words):
            if word != shorter_words[i]:
                result.append(f"{word}/mismatch")
                mismatch_count += 1
            else:
                result.append(word)
        else:
            result.append(f"{word}/mismatch")
            mismatch_count += 1

   
    return ' '.join(result), mismatch_count

# Main execution

# Extract texts from PDF using OCR and PyMuPDF
extract_text_with_ocr(pdf_path, ocr_text_path)
extract_text_from_pdf(pdf_path, pdf_text_path)

# Read extracted texts
with open(ocr_text_path, 'r', encoding='utf-8') as file:
    ocr_text = file.read()

with open(pdf_text_path, 'r', encoding='utf-8') as file:
    pdf_text = file.read()

# Normalize texts
normalized_ocr_text = normalize_text(ocr_text)
normalized_pdf_text = normalize_text(pdf_text)

# Compare the texts and get mismatches
annotated_text, mismatch_count = compare_texts(normalized_ocr_text, normalized_pdf_text)

# Print mismatch count
print(f"Number of mismatches: {mismatch_count}")

# Save the mismatches and strings to the differences file
with open(differences_path, 'w', encoding='utf-8') as file:
    file.write(f"Number of mismatches: {mismatch_count}\n\n")
    file.write("OCR Text:\n")
    file.write(normalized_ocr_text + "\n\n")
    file.write("PDF Text:\n")
    file.write(normalized_pdf_text + "\n\n")

print(f"Differences, including mismatch count and text, saved to '{differences_path}'")


# future works
  # marking mismatches in pdf
  # html representation of pdf
  # show info on hover