

# PDF Text Comparison / Glyph Unicode Mismatch Finder

This Python tool extracts text from a PDF file using both OCR (Optical Character Recognition) and direct text extraction methods, then compares the two outputs to identify and count mismatches. The mismatches are saved in a text file for further analysis.

## Features

- **Text Extraction via OCR**: Uses Tesseract to extract text from PDF images.
- **Text Extraction via PyMuPDF**: Directly extracts text from PDF using PyMuPDF.
- **Text Normalization**: Cleans and normalizes text to facilitate accurate comparison.
- **Text Comparison**: Compares the extracted texts word by word to identify mismatches.
- **Mismatch Counting**: Counts the number of mismatches between the two texts.
- **Logging Mismatches**: Saves mismatches and the compared texts to a file.

## Installation

Before running the script, ensure you have the following dependencies installed:

```bash
pip install transformers torch pymupdf
apt install tesseract-ocr
apt install libtesseract-dev
pip install Pillow
pip install pytesseract
pip install pdf2image matplotlib
apt-get install poppler-utils
pip install pdf2image
```

## Usage

1. **Set the Paths**:
   - Specify the path to your PDF file and output text files in the script.

   ```python
   pdf_path = "document.pdf"
   ```

2. **Run the Script**:
   - The script will extract text using OCR and PyMuPDF, compare the texts, and save the mismatches to the specified output file.

   ```bash
   python app.py
   ```

3. **Review the Results**:
   - Check the `differences.txt` file for the mismatch count and the text comparison.

## Output

- **Mismatch Count**: The number of mismatches between the OCR-extracted text and the PyMuPDF-extracted text.
- **Text Differences**: The OCR and PDF texts with mismatches annotated.

## Future Enhancements

- **PDF Mismatch Marking**: Highlight mismatches directly in the PDF.
- **HTML Representation**: Create an HTML representation of the PDF with mismatches.
- **Hover Info**: Show detailed information on mismatches when hovering over highlighted text in the HTML view.

## License

This project is licensed under the MIT License.

---

https://github.com/user-attachments/assets/7e8c6367-f1ae-4e0f-8f01-906a2b817d5c

