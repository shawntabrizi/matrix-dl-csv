import sys

from setuptools import setup

setup_requires = []
if "upload" in sys.argv:
    setup_requires = ['setuptools-markdown'],

setup(
    name="matrix-dl",
    version="0.0.1",
    author="Thibault Saunier",
    author_email="tsaunier@igalia.com",
    description=("Download logs from Matrix servers as raw text"),
    license="GPL",
    keywords="matrix",
    url="http://packages.python.org/matrix-dl",
    long_description_markdown_filename='README.md',
    setup_requires=setup_requires,
    classifiers=[
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License (GPL)"
    ],
    install_requires=['matrix_client'],
    scripts=['matrix-dl'],
)
