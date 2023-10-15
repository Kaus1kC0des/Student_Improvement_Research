import pdfplumber
import pandas as pd

# Path: raw_data/biotech_data/22BT114.pdf
with open("raw_data/biotech_data/22BT114.pdf", "rb") as f:
    pdf = pdfplumber.load(f)
    page = pdf.pages[0]
    text = page.extract_text()
    print(text)