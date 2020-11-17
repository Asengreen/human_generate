import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="human_generate-Asen", # Replace with your own username
    version="0.0.6",
    author="Asen",
    author_email="asengreenfire@gmail.com",
    description="Create fullname and birthday",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Asengreen/human_generate",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)