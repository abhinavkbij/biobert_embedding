import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="biobert-embedding",
    packages=['biobert_embedding'],
    version="0.1.2",
    author="Jitendra Jangid",
    author_email="jitujangid38@gmail.com",
    description="Embeddings from BioBERT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/overfitter/biobert_embedding",
    download_url="https://github.com/overfitter/biobert_embedding/archive/v0.1.2.tar.gz",
    install_requires=[
          'pytorch-pretrained-bert'
      ],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
