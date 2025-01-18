from setuptools import setup, find_packages

setup(
    name="writevision",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "torch",
        "transformers",
        "Pillow",
        "requests",
        "argparse"
    ],
    entry_points={
        "console_scripts": [
            "writevision=src.main:main",
        ],
    },
)
