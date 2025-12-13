"""Setup configuration for STDF Parser package"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
readme_file = Path(__file__).parent / "stdf" / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="stdf-parser",
    version="1.0.0",
    author="Lucas Wang",
    author_email="lucas@example.com",
    description="STDF (Standard Test Data Format) parser for semiconductor test data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Lucas-Wang-YL/Test_CI",
    packages=find_packages(include=["stdf", "stdf.*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Manufacturing",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.7",
    install_requires=[
        # No external dependencies required for basic functionality
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.3",
            "pytest-cov>=4.1.0",
        ],
        "analysis": [
            "pandas>=1.3.0",
            "matplotlib>=3.4.0",
            "numpy>=1.21.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "stdf=stdf.cli:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
