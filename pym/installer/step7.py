# -*- coding: UTF-8 -*-
#Copyright (C) Christopher Díaz Riveros <chrisadr@gentoo.org>
#
#step7.py is part of Installer.
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
import pym.installer.step8 as step8

welcome_msg=_("""\
                            Step 7 - Configuring Portage
================================================================================
First of all, welcome to your new Gentoo system! Before you can start enjoying
Gentoo, you need to install your ebuild repository. Please run the following
command:

    emerge-webrsync

Note: Don't worry if Portage complains about missing /usr/portage/ location, the
tool will create the location.

Once sync is done, you'll see a warning about news items in the repository, it's
a good idea to read the news before continue. Use:

    eselect news list
    eselect news read
""")

profile_msg=_("""\
Now you need to select a profile for building your system. you can use `eselect`
for listing available profiles:

    eselect profile list

To set the desired profile execute:

    eselect profile set <number>

Please consider to read the profiles section in Gentoo Handbook for more
detailed info:

https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Choosing_the_right_profile

Once your are done, you need to update your system to the new profile, execute:

    emerge --ask --update --deep --newuse @world

This may be a long process, please be patient.
""")

make_conf_msg=_("""\
USE flags help you to customize the building process, by default, each profile
contains the recommended USE flags to be able to run the base system. If you
need to add or remove some of them, it's highly suggested to read Handbook's
section:

https://wiki.gentoo.org/wiki/Handbook:AMD64/Full/Working

Specially:
https://wiki.gentoo.org/wiki/Handbook:AMD64/Full/Working#When_Portage_is_complaining
https://wiki.gentoo.org/wiki/Handbook:AMD64/Full/Working#Using_USE_flags

If after reading these sections you still find problems, you can contact by IRC
in #gentoo channel.

Edit your /etc/portage/make.conf file in order to set the desired USE flags.
Then save your changes and update your system with:

    emerge --ask --update --deep --newuse @world
""")


def init():
    prepare_ebuild_repo()
    prepare_profile_selection()
    prepare_make_conf()
    step8.init()

def prepare_ebuild_repo():
    global welcome_msg
    oshelper.show_msg_open_shell(welcome_msg)

def prepare_profile_selection():
    global profile_msg
    oshelper.show_msg_open_shell(profile_msg)

def prepare_make_conf():
    global make_conf_msg
    oshelper.show_msg_open_shell(make_conf_msg)
