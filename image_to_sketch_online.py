import cv2
import numpy as np
from google.colab import files
from IPython.display import Image, display
import matplotlib.pyplot as plt

def display_image(image, title, position):
    """Helper function to display an image with a title"""
    plt.subplot(position)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
def convert_to_sketch(image):
    """Convert the image to a pencil sketch and display each step"""
    
    # Display original image
    display_image(image, "Original Image", 231)
    
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    display_image(gray_image, "Grayscale Image", 232)
    
    # Invert the grayscale image
    inverted_image = 255 - gray_image
    display_image(inverted_image, "Inverted Grayscale Image", 233)
    
    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    display_image(blurred_image, "Blurred Image", 234)
    
    # Invert the blurred image
    inverted_blurred = 255 - blurred_image
    display_image(inverted_blurred, "Inverted Blurred Image", 235)
    
    # Create the pencil sketch by blending
    pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
    display_image(pencil_sketch, "Pencil Sketch", 236)
    
    return pencil_sketch
