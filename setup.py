import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pelletics",
    version="0.0.1",
    author="Ales Daniel",
    author_email="ales.daniel@gmail.com",
    description="A pellet consumption statistics tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adpro/pelletics",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
