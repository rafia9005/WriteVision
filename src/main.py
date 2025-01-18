import os
from preprocess import load_image_from_url, load_image_from_path
from model import load_model
from utils import print_result

def main():
    use_url = True

    if use_url:
        url = 'https://fki.tic.heia-fr.ch/static/img/a01-122-02-00.jpg'
        image = load_image_from_url(url)
    else:
        path = os.path.join("data", "sample_image.jpg")
        image = load_image_from_path(path)

    processor, model = load_model()

    pixel_values = processor(images=image, return_tensors="pt").pixel_values
    generated_ids = model.generate(pixel_values)
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

    print_result(generated_text)

if __name__ == "__main__":
    main()
