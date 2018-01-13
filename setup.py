#!/usr/bin/python3
#
#Copyright (C) Christopher Díaz Riveros <chrisadr@gentoo.org>
#
#setup.py is part of Stager.
#
#Stager is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License v2 as published by
#the Free Software Foundation, either version 2 of the License, or
#(at your option) any later version.
#
#Stager is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License v2 for more details.
#
#You should have received a copy of the GNU General Public License v2
#along with Stager.  If not, see <http://www.gnu.org/licenses/>.

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
