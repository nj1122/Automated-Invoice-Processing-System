# Project Documentation

## Architecture
The system consists of several components:
- **Preprocessing**: Preprocesses the scanned invoice images to improve OCR accuracy.
- **OCR**: Extracts text from the preprocessed images.
- **Data Extraction**: Extracts key fields from the OCR text.
- **Categorization**: Categorizes invoices by vendor.
- **Storage**: Stores the extracted data in a database.

## Design Choices
- **OpenCV**: Used for image preprocessing.
- **Tesseract**: Used for OCR.
- **Regex**: Used for data extraction.
- **SQLite**: Used for data storage.

## Skillsets Required
- Python programming
- Image processing
- OCR techniques
- Regular expressions
- Database management

## Future Work
- Improve preprocessing techniques.
- Enhance data extraction with more robust methods.
- Implement a web interface for uploading invoices and viewing results.