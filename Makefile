install:
    pip install -r requirements.txt

run:
    python src/main.py --input path --source data/sample_image.jpg

test:
    pytest tests/

clean:
    find . -type d -name "__pycache__" -exec rm -r {} +
