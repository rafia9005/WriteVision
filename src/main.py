import os
import argparse
from preprocess import load_image
from model import load_model
from utils import print_result, validate_generated_text
from logger import setup_logger

logger = setup_logger()

def main():
    parser = argparse.ArgumentParser(description="Handwritten Text Recognition using TrOCR")
    parser.add_argument("--input", type=str, required=True, help="Input type: 'url', 'path', or 'base64'")
    parser.add_argument("--source", type=str, required=True, help="Source of the image (URL, file path, or base64 string)")
    args = parser.parse_args()

    try:
        logger.info("Loading image...")
        image = load_image(args.input, args.source)

        logger.info("Loading model...")
        processor, model = load_model()

        logger.info("Processing image...")
        pixel_values = processor(images=image, return_tensors="pt").pixel_values
        generated_ids = model.generate(pixel_values)
        generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

        if validate_generated_text(generated_text):
            print_result(generated_text)
        else:
            logger.warning("Generated text failed validation.")
    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

