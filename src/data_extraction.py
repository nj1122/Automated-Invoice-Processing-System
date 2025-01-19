import re

def extract_data(ocr_text):
    """
    Extract fields from OCR text using regular expressions.

    Args:
        ocr_text (str): The text extracted from the OCR process.

    Returns:
        tuple: A tuple containing the extracted invoice number, date, total amount, and vendor name.
               If a field is not found, its value will be None.
    """
    print (ocr_text)
    # Extract invoice number using regex
    invoice_number_match = re.search(r'Invoice (Number|No\.|No\,|No\.\:):? (\d+)', ocr_text)
    
    # Try multiple date formats
    date_patterns = [
        r'(\d{2}/\d{2}/\d{4})',  # MM/DD/YYYY
        r'(\d{4}-\d{2}-\d{2})',  # YYYY-MM-DD
        r'(\d{2}-\d{2}-\d{4})',  # DD-MM-YYYY
        r'(\d{1,2} [A-Za-z]+ \d{4})',  # D Month YYYY
    ]
    date_match = None
    for pattern in date_patterns:
        date_match = re.search(pattern, ocr_text)
        if date_match:
            break
    
    # Extract total amount using regex
    total_amount_match = re.search(r'Total ([\%\$]?\d+(\.\d{2})?)', ocr_text)
    
    # Extract vendor name using regex
    vendor_name_match = re.search(r'(Vendor|BILLED TO):\s*(\w+ \w+)', ocr_text)

    # Get the matched groups or None if not found
    invoice_number = invoice_number_match.group(2) if invoice_number_match else None
    date = date_match.group(1) if date_match else None
    total_amount = total_amount_match.group(1) if total_amount_match else None
    vendor_name = vendor_name_match.group(2) if vendor_name_match else None

    return invoice_number, date, total_amount, vendor_name