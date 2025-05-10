import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

class ImageToSketchConverter:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Image to Pencil Sketch Converter")
        self.window.geometry("1200x600")
        
        # Create main frame
        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack(padx=10, pady=10)
        
        # Create image display labels
        self.original_label = tk.Label(self.main_frame, text="Original Image")
        self.original_label.grid(row=0, column=0, padx=10)
        
        self.sketch_label = tk.Label(self.main_frame, text="Pencil Sketch")
        self.sketch_label.grid(row=0, column=1, padx=10)
        
        # Create buttons
        self.button_frame = tk.Frame(self.window)
        self.button_frame.pack(pady=10)
        
        self.load_button = tk.Button(self.button_frame, text="Load Image", command=self.load_image)
        self.load_button.pack(side=tk.LEFT, padx=5)
        
        self.save_button = tk.Button(self.button_frame, text="Save Sketch", command=self.save_sketch)
        self.save_button.pack(side=tk.LEFT, padx=5)
        
        self.original_image = None
        self.sketch_image = None
        
    def load_image(self):
        """Load an image from the user's computer"""
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
        )
        
        if file_path:
            try:
                # Read the image
                self.original_image = cv2.imread(file_path)
                if self.original_image is None:
                    raise Exception("Failed to load image")
                
                # Convert to sketch
                self.sketch_image = self.convert_to_sketch(self.original_image)
                
                # Display images
                self.display_images()
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to process image: {str(e)}")
    
    def convert_to_sketch(self, image):
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
    
    def display_images(self):
        """Display the original and sketch images side by side"""
        if self.original_image is None or self.sketch_image is None:
            return
        
        # Resize images to fit the window
        height = 400
        width = int(height * self.original_image.shape[1] / self.original_image.shape[0])
        
        # Resize original image
        original_resized = cv2.resize(self.original_image, (width, height))
        original_rgb = cv2.cvtColor(original_resized, cv2.COLOR_BGR2RGB)
        original_pil = Image.fromarray(original_rgb)
        original_tk = ImageTk.PhotoImage(original_pil)
        
        # Resize sketch image
        sketch_resized = cv2.resize(self.sketch_image, (width, height))
        sketch_rgb = cv2.cvtColor(sketch_resized, cv2.COLOR_GRAY2RGB)
        sketch_pil = Image.fromarray(sketch_rgb)
        sketch_tk = ImageTk.PhotoImage(sketch_pil)
        
        # Update labels
        self.original_label.configure(image=original_tk)
        self.original_label.image = original_tk
        
        self.sketch_label.configure(image=sketch_tk)
        self.sketch_label.image = sketch_tk
    
    def save_sketch(self):
        """Save the sketch image to a file"""
        if self.sketch_image is None:
            messagebox.showwarning("Warning", "No sketch to save. Please load an image first.")
            return
        
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                cv2.imwrite(file_path, self.sketch_image)
                messagebox.showinfo("Success", "Sketch saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save sketch: {str(e)}")
    
    def run(self):
        """Run the application"""
        self.window.mainloop()

if __name__ == "__main__":
    app = ImageToSketchConverter()
    app.run() 