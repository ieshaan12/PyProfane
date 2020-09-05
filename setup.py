import setuptools

with open("README.md", "r") as fileObj:
  longDescription = fileObj.read()

setuptools.setup(name="PyProfane-v1.0.0",
  packages=['PyProfane-v1.0.0'],
  version="1.0.0",
  author="Ieshaan Saxena",
  author_email="ieshaan1999@gmail.com",
  description="A library to censor and detect offensive words in strings.",
  long_description=longDescription,
  long_description_content_type="text/markdown",
  license="MIT",
  url="https://github.com/ieshaan12/PyProfane",
  download_url="https://github.com/ieshaan12/PyProfane/archive/v1.0.0.tar.gz",
  classifiers=[
    "Development Status :: 3 - Alpha",
    "Natural Language :: English",
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],)