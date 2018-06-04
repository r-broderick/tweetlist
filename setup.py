import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tweetlist",
    version="1.0",
    author="Ryan Broderick",
    author_email="ryanbr44@gmail.com",
    description="A package for searching for, aggregating, and analyzing tweets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/example-project",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests_oauthlib',
        'sklearn',
        'numpy',
        'pandas',
        'scipy',
        'matplotlib',
        'plotly',
        'keras',
        'tensorflow'
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)