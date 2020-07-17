import setuptools

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setuptools.setup(
    name="affability",
    version="1.0.1",
    author="Aaron de los Santos",
    author_email="hansaaron_d@yahoo.com",
    description="A simple package for interfacing with Dialogflow",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aarondls/affability",
    keywords= ['Dialogflow', 'DialogFlow'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires = [
        'dialogflow'
    ],
)