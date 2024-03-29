# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os.path

readme = ""
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, "README.rst")
if os.path.exists(readme_path):
    with open(readme_path, "rb") as stream:
        readme = stream.read().decode("utf8")

setup(
    long_description=readme,
    name="dbvirus-searcher",
    version="0.1.0",
    description="SRA data searcher w/ local caching for the DBVirus project",
    python_requires="==3.*,>=3.7.0",
    author="Felipe Rodrigues",
    author_email="felipe@felipevr.com",
    license="MIT",
    packages=["dbvirus_searcher"],
    package_data={},
    install_requires=[
        "biopython==1.*,>=1.74.0",
        "dbvirus-cacher==0.*,>=0.0.2",
        "fire==0.*,>=0.2.1",
        "pytz==2019.*,>=2019.2.0",
        "tqdm==4.*,>=4.36.0",
        "xmltodict==0.*,>=0.12.0",
    ],
    extras_require={
        "dev": [
            "black==18.*,>=18.3.0",
            "ipython==7.*,>=7.7.0",
            "jsonschema==3.*,>=3.0.0",
            "pylint==2.*,>=2.3.0",
            "pytest==5.*,>=5.0.0",
            "pytest-mock==1.*,>=1.10.0",
        ]
    },
)
