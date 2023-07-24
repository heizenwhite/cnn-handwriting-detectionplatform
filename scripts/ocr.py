import os
import cv2
import pytesseract

# Set the path to the tesseract executable
# pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'

# Directory where your images are located
image_directory = 'C:/Personal Data/Hackathon/hackathon-BreakingAIgorithms/cdc'

# Get a list of all image files in the directory
image_files = [f for f in os.listdir(image_directory) if f.endswith('.jpg') or f.endswith('.png')]

for image_file in image_files:
    # Load the image from file
    image = cv2.imread(os.path.join(image_directory, image_file))

    # Convert the image to gray scale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Run OCR on the gray scale image
    text = pytesseract.image_to_string(gray_image)

    print(f'Text from {image_file}:\n{text}\n')
