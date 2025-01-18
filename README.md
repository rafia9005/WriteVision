# WriteVision: Handwriting Recognition using TrOCR
<p align="center">
  <img src="https://github.com/user-attachments/assets/076785f9-08ab-4616-aedb-1bdf37cf78e8" alt="WriteVision" width="50%">
</p>
WriteVision is a project that leverages the TrOCR (Transformer-based Optical Character Recognition) model from Microsoft to recognize handwritten text from images. Built on the powerful Transformer architecture, TrOCR excels at complex image-to-text tasks, making it ideal for handwriting recognition.

Features
Handwritten Text Recognition: Accurately extracts text from images (supports URLs, local files, and Base64 strings).

Pre-trained Model: Utilizes the microsoft/trocr-base-handwritten model from Hugging Face, trained on the IAM Handwriting dataset.

Extensible: Easily adaptable for different handwriting datasets or use cases.

Model Used
This project uses the microsoft/trocr-base-handwritten model, fine-tuned for handwritten text recognition.

Requirements
Python 3.8 or later

Install dependencies:

bash
Copy
pip install -r requirements.txt
Usage
1. Clone the Repository
bash
Copy
git clone https://github.com/rafia9005/WriteVision.git
cd WriteVision
2. Install Dependencies
bash
Copy
pip install -r requirements.txt
3. Run the Program
From URL
To recognize text from an image URL:

bash
Copy
python src/main.py --input url --source "https://fki.tic.heia-fr.ch/static/img/a01-122-02-00.jpg"
From Local Path
To recognize text from a local image file:

bash
Copy
python src/main.py --input path --source "data/sample_image.jpg"
From Base64
To recognize text from a Base64-encoded image string:

bash
Copy
python src/main.py --input base64 --source "<base64-string>"
Replace <base64-string> with your actual Base64-encoded image data.

Example
bash
Copy
# From URL
python src/main.py --input url --source "https://fki.tic.heia-fr.ch/static/img/a01-122-02-00.jpg"

# From Local Path
python src/main.py --input path --source "data/sample_image.jpg"

# From Base64
python src/main.py --input base64 --source "iVBORw0KGgoAAAANSUhEUgAA..."
License
This project is licensed under the MIT License. See LICENSE for details.

Feel free to contribute or adapt this project for your needs! 🚀

