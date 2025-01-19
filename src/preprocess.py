import cv2

def preprocess_image(image_path):
    """
    Preprocess the image for OCR.

    Args:
        image_path (str): The file path to the invoice image.

    Returns:
        preprocessed_image: The preprocessed binary image.
    """
    # Load image
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Binarize the image using Otsu's thresholding
    _, preprocessed_image = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    return preprocessed_image