#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

# with open('requirements_dev.txt') as requirements_file:
#     requirements = requirements_file.read()

requirements = []

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Jannis M. Hoch",
    author_email='j.m.hoch@uu.nl',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="modelling interplay between conflict and climate",
    entry_points={},
    install_requires=requirements,
    license="tba",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='conflict, climate',
    name='conflict_model',
    packages=find_packages(include=['conflict_model', 'conflict_model.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/JannisHoch/conflict_model',
    version='0.0.1',
    zip_safe=False,
)