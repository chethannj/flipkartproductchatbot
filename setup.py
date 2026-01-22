from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="FLIPKART CHATBOT",
    version="1.0.0",
    author="Chethan N J",
    packages=find_packages(),
    install_requires=requirements,
)