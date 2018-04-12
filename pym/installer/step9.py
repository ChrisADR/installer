#Copyright (C) Christopher Díaz Riveros <chrisadr@gentoo.org>
#
#step9.py is part of Installer.
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
import pym.installer.step10 as step10

welcome_msg="""\
                         Step 9 - Configuring the kernel
================================================================================
Configuring the kernel is one of the most important tasks during installation,
since you are in the beginner section, we highly recommend you to install
genkernel-next. If you want or need to do it manually, please refer to:

https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Kernel

First of all, download Gentoo's kernel and if you need special drivers (e.g. an
extra driver for a wifi card) download linux-firmware too.

    emerge --ask sys-kernel/gentoo-sources sys-kernel/linux-firmware

After that, emerge genkernel-next:

    emerge --ask sys-kernel/genkernel-next

Exit the shell for the next message.
"""

fstab_msg="""\
Before to begin kernel configuration and installation, you need to edit your
/etc/fstab file because genkernel will read it to place initramfs in /boot
partition. This is a good time to leave your /etc/fstab file ready.

    nano -w /etc/fstab

You have to write all your partitions as stated in /etc/fstab itself, once you
are finish, save your changes and execute:

    genkernel --menuconfig all

This will prompt a interactive menu where you have to enable your desired
options, usually default is ok, but if you need some extra info, or you want to
use systemd, these links may help you:

https://wiki.gentoo.org/wiki/Systemd/Installing_Gnome3_from_scratch
https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Kernel#Activating_required_options
https://wiki.gentoo.org/wiki/Wifi#Kernel
"""

def init():
    prepare_kernel()
    prepare_fstab()
    step10.init()

def prepare_kernel():
    global welcome_msg
    oshelper.show_msg_open_shell(welcome_msg)

def prepare_fstab():
    global fstab_msg
    oshelper.show_msg_open_shell(fstab_msg)
