# !/usr/bin/env python
# -*- coding:utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="curl_http",
    version="0.1.1",
    keywords=("curl", "http", "HTTP", "curl_http", "PyCUrl"),
    description="curl_http is a wrapper for PyCUrl",
    long_description="curl_http is a wrapper for PyCUrl,which we use PyCURL more convenient and easy",
    license="MIT Licence",

    url="https://github.com/LDouble/curl_http",
    author="DoubleL",
    author_email="2943200389@qq.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=["pycurl","chardet"]

)