# OCR-Python

Experimental OCR pipeline using OpenCV preprocessing + Tesseract, with local DOCX export.

## Run

Install Tesseract OCR with the Portuguese language data (`por`) on the target machine.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python ocr.py "documento.jpg" -o output/resultado.docx
```

## Pipeline

```text
Image
  ↓
OpenCV grayscale / resize / Otsu
  ↓
Tesseract (por)
  ↓
Text
  └── DOCX
```

This project is retained as an **experimental baseline**. It is not the primary AYORAI OCR engine. The newer [AYORAI Offline OCR API](https://github.com/Ayorinha/ayorai/tree/feat/offline-ocr-api) is the Windows-first path for testing the OneOCR runtime.

Do not commit real identity documents or confidential data.

## Author

**Anderson Leon Ayora** — Data Scientist | AI Engineer | Data Architect
