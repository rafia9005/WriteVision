# WriteVision: Handwriting Recognition using TrOCR

**WriteVision** is a project that uses the pre-trained model **TrOCR (Transformer-based Optical Character Recognition)** from Microsoft to recognize handwritten text from images. The model is based on the Transformer architecture, which excels at handling complex image-to-text tasks like handwriting recognition.

## Features
- Recognizes handwritten text from images (supports both URLs and local images).
- Uses the TrOCR model from Hugging Face to accurately recognize text.
- Can be easily extended or adapted for different handwriting datasets.

## Model Used
This project utilizes the [**microsoft/trocr-base-handwritten**](https://huggingface.co/microsoft/trocr-base-handwritten) model, which is trained on the IAM Handwriting dataset to recognize handwritten text.

## Requirements

- Python 3.8 or later
- Install dependencies using the command:
  ```bash
  pip install -r requirements.txt

