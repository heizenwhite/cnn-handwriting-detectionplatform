import easyocr
import cv2
import re
from matplotlib import pyplot as plt
import numpy as np
#IMAGE 

IMAGE_PATH = 'TEST_41370.jpg'


reader = easyocr.Reader(['en'])
result = reader.readtext(IMAGE_PATH)
result

top_left = tuple(result[0][0][0])
bottom_right = tuple(result[0][0][2])
text = result[0][1]
font = cv2.FONT_HERSHEY_SIMPLEX


img = cv2.imread(IMAGE_PATH)

for detection in result: 
    text = detection[1]
    text_without_spaces = re.sub(r'\s', '', text)
    print(text_without_spaces)