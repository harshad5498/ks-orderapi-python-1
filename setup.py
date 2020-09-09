# coding: utf-8

from setuptools import setup, find_packages  # noqa: H301

NAME = "kotak"
VERSION = "1.0.5"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="KS Trade API&#39;s",
    author="KS-Trade API",
    author_email="team@xyz.org",
    url="",
    keywords=["KS-Trade API", "KS Trade API's"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    """
)
