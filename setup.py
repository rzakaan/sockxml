from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    version = '0.0.1',
    name = 'sockxml',
    packages = [],
    description = 'XML Reader for Socket Code Generator',
    long_description = long_description,
    long_description_content_type="text/markdown",
    url = 'https://github.com/rzakaan/sockxml',
    author = 'Riza Kaan Ucak',
    author_email = 'rzakaan@gmail.com',
    license = 'MIT',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    install_requires = [],
    download_url = 'https://github.com/rzakaan/sockxml/archive/0.0.1.tar.gz',
    keywords = ['xml', 'socket', 'code generator'],
    python_requires='>=3',
)