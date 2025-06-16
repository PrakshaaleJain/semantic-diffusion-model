from PIL import Image
import os
import shutil

input_dir = 'data/facades_raw/base'  # Replace if files are in a different folder
output_image_dir = 'data/facades/images'
output_label_dir = 'data/facades/labels'

os.makedirs(output_image_dir, exist_ok=True)
os.makedirs(output_label_dir, exist_ok=True)

for fname in os.listdir(input_dir):
    if fname.endswith('.jpg'):
        base = os.path.splitext(fname)[0]
        jpg_path = os.path.join(input_dir, fname)
        png_path = os.path.join(input_dir, base + '.png')

        if os.path.exists(png_path):
            shutil.copy(jpg_path, os.path.join(output_image_dir, fname))
            shutil.copy(png_path, os.path.join(output_label_dir, base + '.png'))
