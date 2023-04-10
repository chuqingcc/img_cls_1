import torch
from PIL import Image
from torch.utils.data import Dataset

class FlowerDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform

        self.img_info = []                  #[(path, label), ... ,]

        pass

    def __getitem__(self, index):
        pass

    def __len__(self):
        pass

    def _get_img_info(self):
        pass