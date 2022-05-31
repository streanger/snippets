import sys
import os
import requests
import lxml
from bs4 import BeautifulSoup as bs


def save_img_from_url(url, path):
    """save image from specified url, to specified local path"""
    response = requests.get(url)
    if response.status_code != 200:
        return False
    with open(path, 'wb') as f:
        f.write(response.content)
    return True
    
    
def url_image_to_bytes(url):
    """read url image as bytes"""
    response = requests.get(url)
    if response.status_code != 200:
        return False
    return response.content
    
    
if __name__ == "__main__":
    url = 'https://unsplash.com/photos/4DW0D3CK9B4/download?force=true'
    