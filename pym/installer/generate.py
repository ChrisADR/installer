# -*- coding: UTF-8 -*-
#Copyright (C) Christopher Díaz Riveros <chrisadr@gentoo.org>
#
#generate.py is part of Installer.
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

import pym.installer.oshelper as oshelper

welcome_msg=_("""\
                            Welcome to generate command
================================================================================
I'll prepare a stageX tarball, after extracting a regular stage3 tarball during
installation, you can extract stageX tarball and you'll have most of the files
needed to finish installation, some of these files include:

    /etc/portage/* : All the required files and subdirectories.
    /var/lib/portage/world : List of currently installed programs.
    /etc/timezone : Current timezone
    /etc/locale.gen : Current locales

Once you extract stageX tarball you'll still need to:

    Update your repository (emerge-webrsync)
    Update @world
    Configure timezone and locales
    Update your /etc/fstab file
    Configure your kenrel.
    Configure your bootloader.
""")

def init(args):
    prepare_generate()
    oshelper.generate_stagex(args)


def prepare_generate():
    global welcome_msg
    oshelper.show_msg(welcome_msg)
