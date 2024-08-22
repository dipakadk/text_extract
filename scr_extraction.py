import pytesseract
from PIL import Image
import os

# Set the Tesseract executable path (adjust the path according to your system)
pytesseract.pytesseract.tesseract_cmd = r"D:\Palm mind task\Text Extraction from images\Tesseract-OCR\tesseract.exe"

# Define the output file path
OUTPUT_FILE = "test.txt" 

def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        # Image clear banauna ko lagi
        image = image.resize((image.width * 2, image.height * 2))
        image = image.convert("L")
        
        extracted_text = pytesseract.image_to_string(image, lang='eng', config='--psm 6')
        return extracted_text.strip()
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None

def save_text_to_file(text, output_path, mode='w'):
    try:
        with open(output_path, mode, encoding='utf-8') as file:
            file.write(text)
        print(f"Text successfully saved to {output_path}")
    except Exception as e:
        print(f"Error saving text to file: {e}")

if __name__ == "__main__":
    input_path="D:\Palm mind task\Text Extraction from images\cv_test.png"

    if os.path.isdir(input_path):
        image_files = [os.path.join(input_path, f) for f in os.listdir(input_path) if f.endswith(('.png', '.jpg', '.jpeg'))]
        if not image_files:
            print(f"No images found in the folder {input_path}")
            exit()
    elif os.path.isfile(input_path) and input_path.endswith(('.png', '.jpg', '.jpeg')):
        image_files = [input_path]
    else:
        print("Invalid input path. Please provide a valid image file or folder.")
        exit()




    all_extracted_text = ""
    for image_file in image_files:
        print(f"Processing image: {image_file}")
        extracted_text = extract_text_from_image(image_file)
        if extracted_text:
            all_extracted_text += f"Text from {os.path.basename(image_file)}:\n{extracted_text}\n\n"


    if all_extracted_text:
        save_text_to_file(all_extracted_text, OUTPUT_FILE)
    else:
        print("No text extracted from any of the images.")