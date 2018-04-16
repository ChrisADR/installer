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

import pym.installer.config as config

setup(name='installer',
    version=config.version,
    description=config.description,
    long_description=config.long_description,
    author=config.author,
    author_email=config.author_email,
    url=config.url,
    license=config.license,
    packages=[
        'pym/installer',
        ],
    scripts=[
        'bin/installer',
        ],
    classifiers=[
        config.development_status,
        config.environment,
        ],
    data_files=[
        ('/usr/share/man/man1/',['man/installer.1']),
        ('/usr/share/locale/es/LC_MESSAGES/',['po/es/LC_MESSAGES/installer.mo']),
        ],
    )
