import pytesseract

# Set the path for the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def perform_ocr(image):
    """
    Perform OCR on the preprocessed image.

    Args:
        image: The preprocessed image on which to perform OCR.

    Returns:
        str: The text extracted from the image using OCR.
    """
    # Perform OCR on the preprocessed image
    ocr_result = pytesseract.image_to_string(image)
    return ocr_result