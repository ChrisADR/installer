#Copyright (C) Christopher Díaz Riveros <chrisadr@gentoo.org>
#
#step8.py is part of Installer.
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
import pym.installer.step9 as step9

welcome_msg="""\
                         Step 8 - Configuring the system
================================================================================
Now we need to configure some system-wide settings, first of all timezone. Run:
    
    ls /usr/share/zoneinfo

Choose the right timezone and echo it in /etc/timezone, example:

    echo "America/Lima" > /etc/timezone

Note: Please avoid /usr/share/zoneinfo/Etc/GMT* timezones, they may cause some
strange behaviour.

Once you are finish, please execute:

    emerge --config sys-libs/timezone-data

This will reconfigure timezone-data package and update /etc/localtime
"""

locales_msg="""\
Now you need to set your locales, for that you'll have to edit /etc/locale.gen:
    
    nano -w /etc/locale.gen

Warning: we strongly suggest to use at least one UTF-8 locale, as example:

    en_US.UTF-8 UTF-8
    es_PE.UTF-8 UTF-8
    en_US ISO-8859-1
    de_DE ISO-8859-1

Once you have all the desired locales, generate them running:

    locale-gen

Finally, set your desired locale (if you have more than one) with `eselect` and
reload the environment:

    eselect locale list
    eselect locale set <number>
    env-update && source /etc/profile && export PS1="(chroot) $PS1"
"""

def init():
    prepare_timezone()
    prepare_locales()
    step9.init()


def prepare_timezone():
    global welcome_msg
    oshelper.show_msg_open_shell(welcome_msg)

def prepare_locales():
    global locales_msg
    oshelper.show_msg_open_shell(locales_msg)
