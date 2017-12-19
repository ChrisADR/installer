#!/usr/bin/python3

from distutils.core import setup

setup(name='stager',
    version='0.1.0dev',
    description='Gentoo Installer Prototype',
    author='Christopher Díaz Riveros',
    author_email='chrisadr@gentoo.org',
    url='https://github.com/ChrisADR/stager',
    license='GPLv2',
    packages=[
        'pym/stager',
        ],
    scripts=[
        'bin/stager',
        ],
    classifiers=[
        "Development Status :: 1 -Planning",
        "Environment :: Console",
        ],
    )
