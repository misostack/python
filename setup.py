import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="local-library-misostaack", # Replace with your own username
    version="0.0.1",
    author="misostack",
    author_email="misostack.com@gmail.com",
    description="Local Library API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/misostack/cs1-headfirst-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)