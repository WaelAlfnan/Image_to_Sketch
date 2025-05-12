# Image to Pencil Sketch Converter

This project converts an image to a pencil sketch using OpenCV and displays each step of the process. The project is designed to run in Google Colab.

## Features

- **Image Upload:** Allows users to upload an image file.
- **Grayscale Conversion:** Converts the uploaded image to grayscale.
- **Inversion:** Inverts the grayscale image.
- **Gaussian Blur:** Applies a Gaussian blur to the inverted image.
- **Inverted Blur:** Inverts the blurred image.
- **Pencil Sketch Creation:** Blends the grayscale image with the inverted blurred image to create a pencil sketch.
- **Step-by-Step Display:** Displays each step of the process for better understanding.

## Requirements

- Python 3.x
- OpenCV
- NumPy
- Google Colab
- Matplotlib

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/WaelAlfnan/Image_to_Sketch.git
    cd Image_to_Sketch
    ```

2. **Install the required libraries:**

    ```bash
    pip install opencv-python-headless numpy matplotlib
    ```

## Usage

1. **Upload the image:**

    The script will prompt you to upload an image file when you run it.

2. **Run the script:**

    ```python
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
    ```

## How It Works

1. **Upload the Image:**
   - The user uploads an image file.
   
2. **Convert to Grayscale:**
   - The image is converted to a grayscale image.
   
3. **Invert the Grayscale Image:**
   - The grayscale image is inverted.
   
4. **Apply Gaussian Blur:**
   - A Gaussian blur is applied to the inverted image.
   
5. **Invert the Blurred Image:**
   - The blurred image is inverted.
   
6. **Create the Pencil Sketch:**
   - The pencil sketch is created by blending the grayscale image with the inverted blurred image using the `cv2.divide` function.

## Example

Here is an example of the process:

1. **Original Image**
2. **Grayscale Image**
3. **Inverted Grayscale Image**
4. **Blurred Image**
5. **Inverted Blurred Image**
6. **Pencil Sketch**

## Team Members

- Abdulrahman Sherif Solaimani
- Ahmed Osama Mohammed Khairy
- Omar Arshad Mohammed
- Wael Bahaa Aldien Mostafa
- Mohamed Ali Hassan Aref

## License

This project is licensed under the MIT License. See the LICENSE file for details.
