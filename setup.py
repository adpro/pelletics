import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="pelletics",
    version="0.0.1.dev1",
    author="Ales Daniel",
    author_email="ales.daniel@gmail.com",
    description="A pellet consumption statistics tool",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/adpro/pelletics",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    python_requires='>=3.9',
    entry_points={
        "console_scripts": [
            "realpython=reader.__main__:main",
        ]
    },
)
