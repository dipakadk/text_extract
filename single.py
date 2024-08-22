import argparse
import pytesseract
from PIL import Image, ImageEnhance
import re

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        image = image.resize((image.width * 2, image.height * 2))
        image = image.convert("L")
        # image = ImageEnhance.Contrast(image).enhance(0.1)
        
        extracted_text = pytesseract.image_to_string(image, lang='eng', config='--psm 6') 
        
        # cleaned_text = re.sub(r'[^\w\s\n]', '', extracted_text)
        
        return extracted_text.strip()
       
    except Exception as e:
        print(f"Error: {e}")
        return None

def save_text_to_file(text, output_path):
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"Text successfully saved to {output_path}")
    except Exception as e:
        print(f"Error saving text to file: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract text from images using Tesseract OCR")
    parser.add_argument("image_path", type=str, help="Path to the image file")
    parser.add_argument("output_path", type=str, help="Path to save the extracted text")
    args = parser.parse_args()

    print(f"Processing image: {args.image_path}")
    
    extracted_text = extract_text_from_image(args.image_path)
    
    if extracted_text:
        print("Extracted Text:\n")
        print(extracted_text)
        
        save_text_to_file(extracted_text, args.output_path)
    else:
        print("Text extraction failed.")
