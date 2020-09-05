import setuptools

with open("README.md", "r") as fileObj:
  longDescription = fileObj.read()

setuptools.setup(name="PyProfane",
  packages=setuptools.find_packages(),
  version="1.0.1",
  author="Ieshaan Saxena",
  author_email="ieshaan1999@gmail.com",
  description="A library to censor and detect offensive words in strings.",
  long_description=longDescription,
  long_description_content_type="text/markdown",
  license="MIT",
  url="https://github.com/ieshaan12/PyProfane",
  download_url="https://github.com/ieshaan12/PyProfane/archive/PyProfane-v1.0.1.tar.gz",
  package_data={'PyProfane': ['data/swearWords.txt', 'data/comments.txt']},
  classifiers=[
    "Development Status :: 3 - Alpha",
    "Natural Language :: English",
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],)