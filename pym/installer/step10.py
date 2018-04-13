# -*- coding: UTF-8 -*-
#Copyright (C) Christopher Díaz Riveros <chrisadr@gentoo.org>
#
#step10.py is part of Installer.
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
import pym.installer.step11 as step11

welcome_msg=_("""\
                         Step 10 - Configuring the system
================================================================================
We are almost there, now you need to set the root password, execute:

    passwd

After that you may want to set your host name, you'll need to refer to your init
system's documentation, some examples include:

    nano -w /etc/conf.d/hostname    (OpenRC)
    hostnamectl COMMAND             (SystemD)

This is a good moment to download all the required or desired software that does
not come with the base stage3 tarball, specially networking related software:

    emerge --ask net-misc/networkmanager
    emerge --ask net-misc/dhcpcd
    emerge --ask net-wireless/iw net-wireless/wpa_supplicant

If you need more detailed info, refer to:

https://wiki.gentoo.org/wiki/Handbook:AMD64/Full/Networking
""")

logger_msg=_("""\
If you are not using systemd as your init system, you need to install a logger:
(You only need ONE from these)
 
    emerge --ask app-admin/sysklogd (recommended for beginners)
    emerge --ask app-admin/syslog-ng
    emerge --ask app-admin/metalog

You may want to read the next section for other optional tools:

https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Tools
""")

def init():
    prepare_host()
    prepare_logger()
    step11.init()

def prepare_logger():
    global logger_msg
    oshelper.show_msg_open_shell(logger_msg)

def prepare_host():
    global welcome_msg
    oshelper.show_msg_open_shell(welcome_msg)
