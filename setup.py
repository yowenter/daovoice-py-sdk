#
# Copyright 2017 Wenter
#
# https://yowenter.github.io
#

import os
import re

from setuptools import find_packages
from setuptools import setup

with open(os.path.join('daovoice', '__init__.py'), "r") as f:
    source = f.read()
    m = re.search("__version__ = '(.*)'", source, re.M)
    __version__ = m.groups()[0]

with open('README.rst', 'r') as readme:
    long_description = readme.read()

setup(
    name="daovoice-sdk",
    version=__version__,
    description="DaoVoice Open API Python Sdk",
    long_description=long_description,
    author="Wenter W",
    author_email="wenter.wu@gmail.com",
    license="MIT License",
    url="https://github.com/yowenter/daovoice-py-sdk",
    keywords="DaoVoice Customer Management Python",
    classifiers=[
        'Programming Language :: Python :: 2.7'
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["requests","six"],
    zip_safe=False

)
