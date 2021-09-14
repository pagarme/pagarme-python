# -*- coding: utf-8 -*-
import os
import re
from setuptools import setup, find_packages

__description__ = 'Pagar.me Python'
__long_description__ = 'Python library for Pagar.me API'

__author__ = 'Murilo Henrique, Victor Messina'
__author_email__ = 'suporte@pagar.me'
__special_things__ = 'Derek Stavis, Rodrigo Amaral'


testing_extras = [
    'pytest',
    'pytest-cov',
]


def _find_version():
    filename = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'pagarme/sdk.py'
    )
    with open(filename) as f:
        data = f.read()

    match = re.search(r"VERSION = '(.+)'", data)
    return match.groups()[0]


__version__ = _find_version()

setup(
    name='pagarme-python',
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    packages=find_packages(),
    license='MIT',
    description=__description__,
    long_description=__long_description__,
    special_things=__special_things__,
    url='https://github.com/pagarme/pagarme-python',
    keywords='Payment, pagarme',
    include_package_data=True,
    zip_safe=False,
    install_requires=['requests>=2.20.0'],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
    ],
    tests_require=['pytest'],
    extras_require={
        'testing': testing_extras,
    },
)
