"""
Codebase for "Improved Denoising Diffusion Probabilistic Models".
"""

from .facades_dataset import FacadesDataset 
DATASETS = {
    "facades" : FacadesDataset,
}