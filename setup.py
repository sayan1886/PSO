from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pso',
    version='1.0.0',
    description='A PSO implementation using binary chromosome',
    long_description='A PSO implementation',
    url='https://github.com/sayan1886/PSO',
    author='Sayan Chatterjee',
    author_email='sayan1886@gmail.com',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    package_data = {
        # If any package contains *.json or *.rst files, include them:
        '': ['*.json'],
    },
    # include_package_data=True,
    keywords='pso ga single-objective',
    license='MIT',
    install_requires=['numpy', 'tqdm', 'matplotlib'],
)