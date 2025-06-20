import os
from PIL import Image
import numpy as np

data_dir = "./datasets/facades/annotations/training_preprocessed"
max_valid_label = 63  # num_classes - 1

for filename in os.listdir(data_dir):
    if filename.endswith(".png"):
        label_path = os.path.join(data_dir, filename)
        label = np.array(Image.open(label_path))
        invalid_labels = label[label > max_valid_label]
        if invalid_labels.size > 0:
            print(f"Invalid labels in {filename}: {np.unique(invalid_labels)}")