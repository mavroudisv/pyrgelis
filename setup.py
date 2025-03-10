"""
Setup script for PyRgelis package.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pyrgelis",
    version="0.1.0",
    author="Vasilios Mavroudis",
    author_email="mavroudisv@gmail.com",
    description="Rgelis floating in a surreal space. You can only win.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/username/pyrgelis",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Games/Entertainment :: Simulation",
        "Topic :: Artistic Software",
    ],
    python_requires=">=3.6",
    install_requires=[
        "numpy>=1.19.0",
        "matplotlib>=3.3.0",
    ],
    entry_points={
        "console_scripts": [
            "pyrgelis=pyrgelis.cli:main",
        ],
    },
)