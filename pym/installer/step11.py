# -*- coding: UTF-8 -*-
#Copyright (C) Christopher Díaz Riveros <chrisadr@gentoo.org>
#
#step11.py is part of Installer.
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
                       Step 11 - Configuring the bootloader
================================================================================
Last step in the list! You are about to finish the Gentoo installation process!!
Now we need a bootloader, we'll recommend grub, but feel free to install other
if you want to.

Note: UEFI users, please make sure that you have GRUB_PLATFORMS=\"efi-64\" in
your /etc/portage/make.conf file before emerging grub, not doing so may cause
unexpected results.

    echo 'GRUB_PLATFORMS=\"efi-64\"' >> /etc/portage/make.conf

    emerge --ask sys-boot/grub

Then install the bootloader with:

    grub-install /dev/sda

WARNING: UEFI users are highly encouraged to read following section before 
installing grub:
https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Bootloader#Install
""")

config_msg=_("""\
Now you need to configure grub, this way it'll be able to find your partitions
and initramfs. Execute:

    grub-mkconfig -o /boot/grub/grub.cfg

If you have no error messages, CONGRATULATIONS! you have now a fully installed
Gentoo system. But before finishing this tutorial, you need to check a couple
things:

-Start/enable all the needed services: e.g. if you installed NetworkManager:

    systemctl enable NetworkManager         (SystemD)
    rc-update add NetworkManager default    (OpenRC)
-Install your Window Manager or Desktop Environment: e.g. GNOME or Plasma
    
    emerge --ask [gnome|plasma|i3]
-Create a new user:

    useradd -m -G users,wheel,audio -s /bin/bash larry
    passwd larry
""")

finish_msg=_("""\
To clean installer from your new Gentoo system; exit the chroot with 'exit',
then execute:

    installer cleanup

Finally, you need to umount all the linked directories:

    umount -l /mnt/gentoo/dev{/shm,/pts,}
    umount -R /mnt/gentoo

We recommend you to read these sections to work with Gentoo and Portage:

https://wiki.gentoo.org/wiki/Handbook:AMD64/Full/Working
https://wiki.gentoo.org/wiki/Handbook:AMD64/Full/Portage

If you are reading this message this could mean that now you have your own
Gentoo system, thank your for trying installer and if you find any bug or error,
even if you have enhancement ideas, feel free to email me:

    chrisadr@gentoo.org

Thank you :) and enjoy Gentoo!
""")

def init():
    prepare_bootloader()
    prepare_config()
    prepare_finish()

def prepare_bootloader():
    global welcome_msg
    oshelper.show_msg_open_shell(welcome_msg)

def prepare_config():
    global config_msg
    oshelper.show_msg_open_shell(config_msg)

def prepare_finish():
    global finish_msg
    oshelper.show_msg(finish_msg)
