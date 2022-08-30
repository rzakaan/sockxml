from setuptools import find_packages, setup
import subprocess, os

about = {}
with open("sockxml/__about__.py") as f:
    exec(f.read(), about)

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    version = about['__version__'],
    name = about['__name__'],
    packages = find_packages(),
    description = about['__description__'],
    long_description = long_description,
    long_description_content_type="text/markdown",
    url = about['__url__'],
    author = about['__author__'],
    author_email = about['__email__'],
    license = about['__license__'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
    install_requires = [],
    download_url = 'https://github.com/rzakaan/sockxml/archive/0.0.1.tar.gz',
    keywords = ['xml', 'socket', 'code generator'],
    python_requires='>=3',
)