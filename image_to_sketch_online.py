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
    
    return pencil_sketch

def process_image():
    # Upload the image
    uploaded = files.upload()

    # Get the first uploaded file
    file_name = list(uploaded.keys())[0]

    # Read the image
    image = cv2.imread(file_name)
    if image is None:
        print("Error: Could not read the image")
        return
    # Convert to sketch and display all steps
    plt.figure(figsize=(15, 10))
    convert_to_sketch(image)
    plt.show()

# Run the program
if __name__ == "__main__":
    process_image()
