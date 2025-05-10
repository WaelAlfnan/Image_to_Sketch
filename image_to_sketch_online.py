import cv2
import numpy as np
from google.colab import files
from IPython.display import Image, display
import matplotlib.pyplot as plt

def convert_to_sketch(image):
    """Convert the image to a pencil sketch"""
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Invert the grayscale image
    inverted_image = 255 - gray_image
    
    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    
    # Invert the blurred image
    inverted_blurred = 255 - blurred_image
    
    # Create the pencil sketch by blending
    pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
    
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
    
    # Convert to sketch
    sketch = convert_to_sketch(image)
    
    # Display original and sketch side by side
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(sketch, cmap='gray')
    plt.title('Pencil Sketch')
    plt.axis('off')
    
    plt.show()
    
    # Save the sketch
    output_file = 'sketch_' + file_name
    cv2.imwrite(output_file, sketch)
    
    # Download the sketch
    files.download(output_file)

# Run the program
if __name__ == "__main__":
    process_image() 