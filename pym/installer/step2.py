# -*- coding: UTF-8 -*-
#Copyright (C) Christopher Díaz Riveros <chrisadr@gentoo.org>
#
#step2.py is part of Installer.
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
import pym.installer.step3 as step3

welcome_msg=_("""\
                         Step 2 - Preparing the disks
===============================================================================

Now we are going to prepare your block device and make a partition table to be
able to store your filesystems, you have two options:

    MBR (Master Boot Record), you'll need to use fdisk.
    GPT (GUID Partition Table), you'll need to use parted.

Althought this prototype is not designed to generate a partition table, you may
find interesting the next suggestion:

    - You must have a root (/) partition.
    - You'll probably like a /boot partition.
    - You may want a swap partition.
    - You may want a separate /home partition.

For more detailed info, please refer to:
https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Disks
""")

post_partition_msg=_("""\
Now that you have a partition table, you need to create a filesystem on each
partition to be able to store data. This prototype assumes that you'll create
ext4 filesystems, some useful commands include:

    mkfs.ext4 /dev/sdXy
where:
    -X is the device letter
    -y is the partition number

To be able to create a swap partition, you can use:

    mkswap /dev/sdXy
    swapon /dev/sdXy

For more detailed info please refer to:
https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Disks#Creating_file_systems
""")

mounting_root_msg=_("""\
Finally, we need you to mount your root partition (/) into /mnt/gentoo. If you
don't have a /mnt/gentoo directory, you can create one with:

    mkdir -p /mnt/gentoo

Then you need to mount it with:

    mount /dev/sdXy /mnt/gentoo
""")

def init():
    prepare_disks()
    prepare_fs()
    mount_root()
        
    if(oshelper.check_mnt_gentoo()):
        oshelper.print_and_wait(_("Great, we'll continue with step 3 in a few seconds!"))
        step3.init()
    else:
        oshelper.die_with_msg(_("Error: /mnt/gentoo not mounted, please verify."))


def prepare_disks():
    global welcome_msg
    oshelper.show_msg_open_shell(welcome_msg)

def prepare_fs():
    global post_partition_msg
    oshelper.show_msg_open_shell(post_partition_msg)

def mount_root():
    global mounting_root_msg
    oshelper.show_msg_open_shell(mounting_root_msg)
