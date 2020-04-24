import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nepali-stemmer",
    version="0.0.1",
    author="Oyesh Mann Singh",
    author_email="osingh1@umbc.edu",
    description="A simple Nepali stemmer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oya163/nepali-stemmer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    python_requires='>=3.6',
)
