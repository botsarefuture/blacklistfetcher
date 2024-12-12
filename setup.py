from setuptools import setup, find_packages
import os

# Read the README file for the long description
long_description = ''
if os.path.exists('README.md'):
    with open('README.md', encoding='utf-8') as f:
        long_description = f.read()

setup(
    name='blacklistfetcher',
    version='1.0.1',
    description='A Python module for fetching and parsing a blacklist of IP addresses.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Verso Vuorenmaa',
    author_email='verso@luova.club',
    url='https://github.com/botsarefuture/blacklistfetcher',
    packages=find_packages(),
    install_requires=[
        'aiohttp>=3.8.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    license='MIT',  # Define the license to prevent warnings on some systems
    include_package_data=True,  # Include non-Python files (like README.md) in the package
)
