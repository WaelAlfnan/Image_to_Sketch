# Image to Pencil Sketch Converter

This Python application converts images into pencil sketches using OpenCV. It provides a simple graphical user interface to load images, view the conversion results, and save the generated sketches.

## Features

- Load images from your computer
- Convert images to pencil sketches in real-time
- View original and sketch images side by side
- Save the generated sketches as image files
- Supports various image formats (JPG, PNG, BMP, GIF)

## Requirements

- Python 3.7 or higher
- OpenCV
- NumPy
- Pillow (PIL)
- Tkinter (usually comes with Python)

## Installation

1. Clone this repository or download the source code
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python image_to_sketch.py
   ```

2. Click the "Load Image" button to select an image from your computer
3. The application will display the original image and its pencil sketch version side by side
4. Click the "Save Sketch" button to save the generated sketch
5. Choose the location and format for saving the sketch

## How It Works

The application uses the following steps to convert an image to a pencil sketch:

1. Convert the image to grayscale
2. Invert the grayscale image
3. Apply Gaussian blur to the inverted image
4. Invert the blurred image
5. Blend the grayscale image with the blurred inverse using a dodge blend

## License

This project is open source and available under the MIT License. 