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
