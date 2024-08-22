# import argparse
# import pytesseract
# from PIL import Image, ImageEnhance
# import re
# import os

# # pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# def extract_text_from_image(image_path):
#     try:
#         image = Image.open(image_path)
#         image = image.resize((image.width * 2, image.height * 2))
#         image = image.convert("L")
        
#         extracted_text = pytesseract.image_to_string(image, lang='eng', config='--psm 6') 
                
#         return extracted_text.strip()
       
#     except Exception as e:
#         print(f"Error processing {image_path}: {e}")
#         return None

# def save_text_to_file(text, output_path, mode='w'):
#     try:
#         with open(output_path, mode, encoding='utf-8') as file:
#             file.write(text)
#         print(f"Text successfully saved to {output_path}")
#     except Exception as e:
#         print(f"Error saving text to file: {e}")

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Extract text from multiple images using Tesseract OCR")
#     parser.add_argument("image_folder", type=str, help="Path to the folder containing image files")
#     parser.add_argument("output_path", type=str, help="Path to save the extracted text")
#     args = parser.parse_args()

#     image_files = [os.path.join(args.image_folder, f) for f in os.listdir(args.image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

#     if not image_files:
#         print(f"No images found in the folder {args.image_folder}")
#     else:
#         print(f"Processing images in folder: {args.image_folder}")
        
#         all_extracted_text = ""
#         for image_file in image_files:
#             print(f"Processing image: {image_file}")
#             extracted_text = extract_text_from_image(image_file)
#             if extracted_text:
#                 all_extracted_text += f"Text from {os.path.basename(image_file)}:\n{extracted_text}\n\n"

        
#         if all_extracted_text:
#             save_text_to_file(all_extracted_text, args.output_path)
#         else:
#             print("No text extracted from any of the images.")
