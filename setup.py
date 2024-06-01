from setuptools import setup, find_packages

setup(
    name='Edge_Detection_Image',
    version='0.1.0',
    packages=find_packages(),
    description="Edge Detection is a method of segmenting an image into regions of discontinuity",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="zahra jafari",
    author_email="mzahrajafari94@gmail.com",
    url="https://github.com/Zahra-jafari-2024/Edge_Detection_Image",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'click',
    ],
    
    python_requires='>=3.6',
)
