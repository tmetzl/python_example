# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='python_example',
    version='0.0.1',
    license='GNU',
    url='https://github.com/tmetzl/python_example',
    description='Example Python project with Github Actions and test',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Tim Metzler',
    author_email='tim.metzler@h-brs.de',
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[],
    include_package_data = True,
    zip_safe=False,
    test_suite='tests',
    tests_require=['pytest-cov']
)
