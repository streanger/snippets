import numpy as np
from PIL import Image


def rgb2gray(rgb):
    """convert rgb image to greyscale"""
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])
    
    
def open_image(filename):
    """open image file"""
    img = Image.open(filename)
    return img
    
    
if __name__ == "__main__":
    pass
    