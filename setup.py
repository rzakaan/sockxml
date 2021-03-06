from setuptools import find_packages, setup
import subprocess, os

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

version= subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE).stdout.decode("utf-8").strip()
assert "." in version

assert os.path.isfile('sockxml/version.py')
with open('sockxml/VERSION', 'w') as f:
    f.write(f"{version}\n")

setup(
    version = version,
    name = 'sockxml',
    packages = find_packages(),
    description = 'XML Reader for Socket Code Generator',
    long_description = long_description,
    long_description_content_type="text/markdown",
    url = 'https://github.com/rzakaan/sockxml',
    author = 'Riza Kaan Ucak',
    author_email = 'rzakaan@gmail.com',
    license = 'MIT',
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