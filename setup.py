from setuptools import setup
import os

PACKAGE_NAME = "refgenie_nfcore"

# Ordinary dependencies
DEPENDENCIES = []
with open("requirements/requirements-all.txt", "r") as reqs_file:
    for line in reqs_file:
        if not line.strip():
            continue
        DEPENDENCIES.append(line)


with open(os.path.join(PACKAGE_NAME, "_version.py"), 'r') as versionfile:
    version = versionfile.readline().split()[-1].strip("\"'\n")

# Handle the pypi README formatting.
try:
    import pypandoc
    long_description = pypandoc.convert_file('README.md', 'rst')
    msg = "\033[032mPandoc conversion succeeded.\033[0m"
except(IOError, ImportError, OSError):
    msg = "\033[0;31mWarning: pandoc conversion failed!\033[0m"
    long_description = open('README.md').read()


setup(
    name=PACKAGE_NAME,
    packages=[PACKAGE_NAME],
    version=version,
    description='A standardized configuration object for reference genome assemblies',
    long_description=long_description, 
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2.7", 
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering :: Bio-Informatics"
    ],    
    license="BSD2",
    keywords="bioinformatics, sequencing, ngs",
    url='https://refgenie.databio.org',
    author=u'Nathan Sheffield',
    entry_points={
        'refgenie.hooks.post_update': 'nfcore=refgenie_nfcore:update_nfcore_config'
    }
)

print(msg)