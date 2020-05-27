import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="base64file", 
    version="0.1",
    author="",
    author_email="",
    license='Apache License 2.0',
    description="A small utility client to either decode or encode a set of files in a folder to or from base64",
    url="",
    packages=setuptools.find_packages(),
    install_requires=[
        'click>=7.1.1',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)