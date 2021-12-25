#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
from attachtags import script_name, __author__, __email__, __version__


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    "setuptools>=42",
    "wheel"]

test_requirements = ['pytest>=3', ]

setup(
    name=script_name,
    version=__version__,
    author=__author__,
    author_email=__email__,
    description="attachtags is a tool for recording and \
categorizing files in your Windows.",
    long_description=readme + '\n\n' + history,
    url='https://github.com/Gongzi-Yu/attachtags',
    project_urls={
        "Bug Tracker": "https://github.com/Gongzi-Yu/attachtags/issues"
        },
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    license="MIT license",
    packages=find_packages(include=['attachtags', 'attachtags.*']),
    python_requires='>=3.7.3',
    zip_safe=False,
    install_requires=requirements,
    tests_require=test_requirements,
    include_package_data=True,
    keywords='attachtags',
    test_suite='tests',
    entry_points={
        'console_scripts': [
            'attachtags=attachtags.cli:main',
        ],
    },
)
