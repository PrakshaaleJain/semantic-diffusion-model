import os
from PIL import Image
import numpy as np

data_dir = "./datasets/facades/annotations/training"
output_dir = "./datasets/facades/annotations/training_preprocessed"
os.makedirs(output_dir, exist_ok=True)

max_valid_label = 63  # num_classes - 1

for filename in os.listdir(data_dir):
    if filename.endswith(".png"):
        label_path = os.path.join(data_dir, filename)
        label = np.array(Image.open(label_path))
        print(f"Processing {filename} - Max label: {label.max()}")  # Debugging statement
        label[label > max_valid_label] = 0  # Replace invalid labels with 0
        output_path = os.path.join(output_dir, filename)
        print(f"Saving processed file to {output_path}")  # Debugging statement
        Image.fromarray(label).save(output_path)