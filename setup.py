#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

with open('README.rst', 'r', encoding='utf-8') as f:
    long_description = f.read()
setup(
    name='humanhash3',
    version='0.0.6',
    description='Human-readable representations of digests.',
    long_description=long_description,
    author='Zachary Voase',
    author_email='z@zacharyvoase.com',
    url='https://github.com/blag/humanhash',
    py_modules=['humanhash'],
    license='Public Domain',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Security',
        'Topic :: Utilities',

        # Pick your license as you wish (should match "license" above)
        'License :: Public Domain',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.2',  # Not tested
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
