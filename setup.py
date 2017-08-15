# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

__version__ = '3.0.0'
__description__ = 'Pagar.me Python'
__long_description__ = 'Python library for Pagar.me API'

__author__ = 'Murilo Henrique, Victor Messina'
__author_email__ = 'suporte@pagar.me'
__special_things__ = 'Derek Stavis, Rodrigo Amaral'

requires = [i.strip() for i in open("requirements.txt").readlines()]

testing_extras = [
    'pytest',
    'pytest-cov',
]

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
    install_requires=requires,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: MIT License',
    ],
    tests_require=['pytest'],
    extras_require={
        'testing': testing_extras,
    },
)
