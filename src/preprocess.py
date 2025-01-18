from PIL import Image
import requests

def load_image_from_url(url: str):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    return Image.open(response.raw).convert("RGB")

def load_image_from_path(path: str):
    return Image.open(path).convert("RGB")
