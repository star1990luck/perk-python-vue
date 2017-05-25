#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
python-vuejs
-------------
Gluing Python and Vue.js with a set of scripts in order to automate project and app builds
"""

try:
    from setuptools import setup
except:
    from distutils.core import setup

import codecs

requirements = [
    'Click>=6.0',
    'colorama',
]

test_requirements = []

setup(
    name='python_vuejs',
    version='0.0.7',
    description="Gluing Python and Vue.js with a set of scripts in order to automate project and app builds",
    long_description=codecs.open('README.rst', 'r', 'utf-8').read(),
    author="Christian Strappazzon",
    author_email='lab@strap.it',
    url='https://github.com/cstrap/python-vuejs',
    packages=[
        'python_vuejs',
    ],
    package_dir={'python_vuejs':
                 'python_vuejs'},
    entry_points={
        'console_scripts': [
            'pyvue=python_vuejs.cli:cli',
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='python_vuejs',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
