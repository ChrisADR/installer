#!/usr/bin/python3
#
#Copyright (C) Christopher Díaz Riveros <chrisadr@gentoo.org>
#
#setup.py is part of Installer.
#
#Installer is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License v2 as published by
#the Free Software Foundation, either version 2 of the License, or
#(at your option) any later version.
#
#Installer is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License v2 for more details.
#
#You should have received a copy of the GNU General Public License v2
#along with Installer.  If not, see <http://www.gnu.org/licenses/>.

from distutils.core import setup

setup(name='installer',
    version='0.1.0-pre-alpha',
    description='Gentoo Installer Prototype',
    author='Christopher Díaz Riveros',
    author_email='chrisadr@gentoo.org',
    url='https://github.com/ChrisADR/installer',
    license='GPLv2',
    packages=[
        'pym/installer',
        ],
    scripts=[
        'bin/installer',
        ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        ],
    )
