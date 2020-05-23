import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CodeMonitor",
    version="1.0.2",
    author="Lucas Frota",
    author_email="lucv.frota@gmail.com",
    description="Code Monitor is a simples way to send feedback about your code to your smartphone",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Lucasfrota/CodeMonitor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
