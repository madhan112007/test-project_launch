from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name="projectlaunch",
    version="1.0.5",
    description="Simple GitHub Push Tool for Students & Developers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Madhan",
    author_email="codethetrend@gmail.com",
    url="https://github.com/madhan112007/test-project_launch",
    packages=find_packages(),
    install_requires=[
        "click>=8.0.0",
        "rich>=13.0.0",
    ],
    entry_points={
        "console_scripts": [
            "projectlaunch=projectlaunch.cli:main",
            "pl=projectlaunch.cli:main",
        ],
    },
    py_modules=["projectlaunch.__main__"],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
