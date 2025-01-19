# Automated Invoice Processing System

## Project Description
This project is an end-to-end solution for processing scanned invoices, extracting key information, and categorizing the invoices by vendor.

## Setup Instructions
1. Clone the repository.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Place sample invoice images/PDFs in the `data/sample_invoices/` directory.
4. Run the main script using `python src/main.py`.

## Components
- `preprocess.py`: Image preprocessing code.
- `ocr.py`: OCR extraction code.
- `data_extraction.py`: Code to extract fields (invoice number, date, etc.).
- `categorization.py`: Vendor categorization code.
- `main.py`: Main driver script to run the processing pipeline.