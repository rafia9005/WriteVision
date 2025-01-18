from PIL import Image
import requests
import base64
from io import BytesIO
from logger import setup_logger

logger = setup_logger()

def load_image(input_type: str, source: str):
    if input_type == "url":
        return load_image_from_url(source)
    elif input_type == "path":
        return load_image_from_path(source)
    elif input_type == "base64":
        return load_image_from_base64(source)
    else:
        raise ValueError("Invalid input type. Use 'url', 'path', or 'base64'.")

def load_image_from_url(url: str):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        logger.info(f"Image loaded from URL: {url}")
        return Image.open(response.raw).convert("RGB")
    except Exception as e:
        logger.error(f"Failed to load image from URL: {e}")
        raise

def load_image_from_path(path: str):
    try:
        logger.info(f"Image loaded from path: {path}")
        return Image.open(path).convert("RGB")
    except Exception as e:
        logger.error(f"Failed to load image from path: {e}")
        raise

def load_image_from_base64(base64_str: str):
    try:
        image_data = base64.b64decode(base64_str)
        logger.info("Image loaded from base64 string.")
        return Image.open(BytesIO(image_data)).convert("RGB")
    except Exception as e:
        logger.error(f"Failed to load image from base64: {e}")
        raise

