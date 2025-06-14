from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import os

# --- Configuration ---
image_filename = "image.jpg" # Replace with actual name of your image file
output_directory = "output_images"
n_colours_to_reduce_to = 8 # Experiment with this number. Min = 1

# --- Ensure output directory exists ---
if not os.path.exists(output_directory):
    os.makedirs(output_directory)
    print(f"Created output directory: {output_directory}/")

# --- Step 1: Load the Image ---
try:
    image_path = os.path.join(image_filename)
    img = Image.open(image_path)
    img = img.convert('RGB')
    print(f"Loaded image: {image_filename} (Size: {img.size[0]}x{img.size[1]})")
except FileNotFoundError:
    print(f"Error: Image file '{image_filename}' not found in the project directory.")
    print("Please make sure your image is in the same folder as main.py and the name is correct.")
    exit()

# Convert the image to a NumPy array for processing
img_array = np.array(img)

# --- Step 2: Reshape the Image Data for K-Means ---
# We need a 2D array where each row is a pixel and columns are R, G, B values
# Original shape is (height, width, 3)
# Reshaped to (number_of_pixels, 3)
original_height, original_width, channels = img_array.shape
pixels_reshaped = img_array.reshape(-1, channels) # -1 automatically calculates the first dimension
print(f"Image reshaped to {pixels_reshaped.shape[0]} pixels, each with {pixels_reshaped.shape[1]} colour channels.")

# --- Step 3: Apply K-Means Clustering ---
print(f"Applying K-Means clustering to reduce to {n_colours_to_reduce_to} colours...")
# n_init="auto" is recommended for newer scikit-learn versions
kmeans = KMeans(n_clusters=n_colours_to_reduce_to, random_state=42, n_init="auto")
kmeans.fit(pixels_reshaped)

# --- Step 4: Get the Cluster Colours (the new, representative colours) ---
# These are the average colours of each cluster
new_colours = kmeans.cluster_centers_
print(f"Found {len(new_colours)} cluster colours.")

# --- Step 5: Assign New Colours to Pixels ---
# Assign each original pixel to its closest cluster colour
# kmeans.labels_ contains the cluster ID for each pixel
# new_colours[kmeans.labels_] maps these IDs back to the actual RGB colours
clustered_pixels = new_colours[kmeans.labels_]

# Reshape back to the original image dimensions
compressed_image_array = clustered_pixels.reshape(original_height, original_width, channels)

# Flip image vertically
# compressed_image_array = np.flipud(compressed_image_array)

# Convert to unsigned 8-bit integers (0-255 range for image pixels)
compressed_image_array = np.rint(compressed_image_array).astype(np.uint8)
print("Image colours compressed.")

# --- Step 6: Create and Save the New Image ---
output_image_filename = os.path.join(output_directory, f"compressed_{image_filename.split('.')[0]}_{n_colours_to_reduce_to}_colours.png")
compressed_img = Image.fromarray(compressed_image_array)
compressed_img.save(output_image_filename)
print(f"Compressed image saved as: {output_image_filename}")
