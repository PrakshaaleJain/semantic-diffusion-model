import os
from PIL import Image
import numpy as np
import torch
from torch.utils.data import Dataset

class FacadesDataset(Dataset):
    def __init__(self, data_dir, image_size=256, split='training', transform=None):
        self.image_dir = os.path.join(data_dir, 'images', split)
        self.label_dir = os.path.join(data_dir, 'annotations', split)
        self.image_filenames = sorted([
            f for f in os.listdir(self.image_dir) if f.endswith('.jpg') or f.endswith('.png')
        ])
        self.image_size = image_size
        self.transform = transform

    def __len__(self):
        return len(self.image_filenames)

    def __getitem__(self, idx):
        img_path = os.path.join(self.image_dir, self.image_filenames[idx])
        label_filename = self.image_filenames[idx].replace('.jpg', '.png').replace('.jpeg', '.png')
        label_path = os.path.join(self.label_dir, label_filename)

        image = Image.open(img_path).convert("RGB").resize((self.image_size, self.image_size), Image.BICUBIC)
        label = Image.open(label_path).convert("L").resize((self.image_size, self.image_size), Image.NEAREST)

        image = np.array(image).astype(np.float32) / 127.5 - 1.0
        label = np.array(label).astype(np.int64)

        image = torch.from_numpy(image).permute(2, 0, 1)  # [C, H, W]
        label = torch.from_numpy(label)  # [H, W]

        return {
            "image": image,
            "label": label,
        }