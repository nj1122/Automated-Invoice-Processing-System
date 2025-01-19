from preprocess import preprocess_image
from ocr import perform_ocr
from data_extraction import extract_data
from categorization import categorize_by_vendor

def main(image_path):
    """
    Main driver function to run the invoice processing pipeline.

    Args:
        image_path (str): The file path to the invoice image.
    """
    # Preprocess the image
    preprocessed_image = preprocess_image(image_path)
    if preprocessed_image is not None:
        # Perform OCR on the preprocessed image
        ocr_text = perform_ocr(preprocessed_image)
        if ocr_text:
            # Extract data from the OCR text
            invoice_number, date, total_amount, vendor_name = extract_data(ocr_text)
            # Categorize the invoice by vendor
            category = categorize_by_vendor(vendor_name)
            # Print the extracted and categorized information
            print(f"Invoice Number: {invoice_number}")
            print(f"Date: {date}")
            print(f"Total Amount: {total_amount}")
            print(f"Vendor Name: {vendor_name}")
            print(f"Category: {category}")
        else:
            print("OCR processing failed.")
    else:
        print("Image preprocessing failed.")

if __name__ == "__main__":
    # Example image path
    image_path = 'data/sample_invoices/sample_invoice.png'
    main(image_path)