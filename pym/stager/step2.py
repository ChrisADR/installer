import pym.stager.oshelper as oshelper
import pym.stager.step3 as step3

welcome_msg="""\
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
"""

post_partition_msg="""\
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
"""

mounting_root_msg="""\
Finally, we need you to mount your root partition (/) into /mnt/gentoo. If you
don't have a /mnt/gentoo directory, you can create one with:

    mkdir -p /mnt/gentoo

Then you need to mount it with:

    mount /dev/sdXy /mnt/gentoo
"""

def init(args):
    if args.tui:
        #TODO: Launch TUI interface
        pass
    else:
        prepare_disks()
        prepare_fs()
        mount_root()
        
    if(oshelper.check_mnt_gentoo()):
        oshelper.print_and_wait("Great, we'll continue with step 3 in a few seconds!")
        step3.init(args)
    else:
        oshelper.die_with_msg("Error: /mnt/gentoo not mounted, please verify.")


def prepare_disks():
    global welcome_msg
    oshelper.show_msg_open_shell(welcome_msg)

def prepare_fs():
    global post_partition_msg
    oshelper.show_msg_open_shell(post_partition_msg)

def mount_root():
    global mounting_root_msg
    oshelper.show_msg_open_shell(mounting_root_msg)
