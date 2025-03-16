from PIL import Image
import pytesseract
import os

def extract_text_from_image(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"File not found: {image_path}")
    
    image = Image.open(image_path)
    return pytesseract.image_to_string(image)
