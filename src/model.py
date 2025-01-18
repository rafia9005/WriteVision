from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from logger import setup_logger
import os

logger = setup_logger()

def load_model(model_directory="./model"):
    """
    Load model and processor. If a local model exists in the specified directory, load from there.
    Otherwise, download from Hugging Face and save locally.
    """
    try:
        if os.path.exists(model_directory) and os.path.isdir(model_directory):
            processor = TrOCRProcessor.from_pretrained(model_directory)
            model = VisionEncoderDecoderModel.from_pretrained(model_directory)
            logger.info(f"Model and processor loaded successfully from {model_directory}.")
        else:
            logger.info("Local model not found. Downloading from Hugging Face...")
            processor = TrOCRProcessor.from_pretrained('microsoft/trocr-base-handwritten')
            model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-handwritten')
            logger.info("Model and processor downloaded successfully.")

            os.makedirs(model_directory, exist_ok=True)
            processor.save_pretrained(model_directory)
            model.save_pretrained(model_directory)
            logger.info(f"Model and processor saved locally to {model_directory}.")

        return processor, model
    except Exception as e:
        logger.error(f"Failed to load or save model: {e}")
        raise
