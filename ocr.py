from __future__ import annotations

import argparse
from pathlib import Path

import cv2
import pytesseract
from docx import Document

def extract_text(image_path: Path) -> str:
    image = cv2.imread(str(image_path))
    if image is None:
        raise FileNotFoundError(f"Image not found or unreadable: {image_path}")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    scaled = cv2.resize(gray, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
    processed = cv2.threshold(scaled, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return pytesseract.image_to_string(processed, lang="por").strip()

def save_docx(text: str, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    doc = Document()
    doc.add_paragraph(text)
    doc.save(output_path)

def main() -> None:
    parser = argparse.ArgumentParser(description="OCR experimental pipeline with OpenCV + Tesseract")
    parser.add_argument("image", type=Path)
    parser.add_argument("-o", "--output", type=Path, default=Path("output/ocr_result.docx"))
    args = parser.parse_args()
    text = extract_text(args.image)
    print(text)
    save_docx(text, args.output)
    print(f"Saved: {args.output}")

if __name__ == "__main__":
    main()
