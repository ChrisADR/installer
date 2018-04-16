# -*- coding: UTF-8 -*-
#Copyright (C) Christopher Díaz Riveros <chrisadr@gentoo.org>
#
#step5.py is part of Installer.
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
import pym.installer.step6 as step6

welcome_msg=_('''\
                    Step 5 - Installing the Gentoo base system
================================================================================
If you are using a Official Gentoo Installation media, you may want to select a
mirror to be able to download the source code faster, use the next command:

    mirrorselect -i -o >> /mnt/gentoo/etc/portage/make.conf

After that, you need to create a directory for your ebuild repository, execute:

    mkdir --parents /mnt/gentoo/etc/portage/repos.conf

And then copy the Gentoo repository configuration file provided by Portage in
the newly created repos.conf directory:

    cp /mnt/gentoo/usr/share/portage/config/repos.conf \\
        /mnt/gentoo/etc/portage/repos.conf/gentoo.conf

Finally, copy the DNS info before entering the new environment:

    cp --dereference /etc/resolv.conf /mnt/gentoo/etc
''')

prepare_mount_msg=_('''\
Before to enter the brand new Gentoo system, you need to mount certain
filesystems to be capable to change the Linux root. Use the following commands:

    mount --types proc  /proc   /mnt/gentoo/proc
    mount --rbind       /sys    /mnt/gentoo/sys
    mount --make-rslave         /mnt/gentoo/sys
    mount --rbind       /dev    /mnt/gentoo/dev
    mount --make-rslave         /mnt/gentoo/dev

Note: --make-rslave is needed for systemd support later in installation.

I'll install myself inside the chroot so you'll be able to continue the tutorial
directly.
''')

def init():
    verify_mounts()
    prepare_ebuild_repo()
    verify_files()
    verify_shm()
    prepare_mount_fs()
    bootstrap_in_chroot()
    step6.init()

def prepare_ebuild_repo():
    global welcome_msg
    oshelper.show_msg_open_shell(welcome_msg)

def prepare_mount_fs():
    global prepare_mount_msg
    oshelper.show_msg_open_shell(prepare_mount_msg)

def bootstrap_in_chroot():
    installing_msg=_('''\
Downloading and installing in the chroot, please wait
''')
    oshelper.show_msg(installing_msg)
    try:
        oshelper.bootstrap_in_chroot()
    except ChildProcessError:
        err_msg=_('''\
I had problems to extract/install in the chroot, please do
it manually:

    wget -qP /tmp https://github.com/ChrisADR/installer/releases/<desired_release>.tar.gz
    tar xf /tmp/<desired_release>.tar.gz -C /tmp
    cd /tmp/<extracted_dir>
    python setup.py install --prefix=/mnt/gentoo/usr
    python setup.py install_data --root=/mnt/gentoo
''')
        oshelper.show_msg_open_shell(err_msg)
    except ConnectionError:
        err_msg=_('''\
I couldn't download installer, please download it manually:

    wget -qP /tmp https://github.com/ChrisADR/installer/releases/<desired_release>.tar.gz
    tar xf /tmp/<desired_release>.tar.gz -C /tmp
    cd /tmp/<extracted_dir>
    python setup.py install --prefix=/mnt/gentoo/usr
    python setup.py install_data --root=/mnt/gentoo
''')
        oshelper.show_msg_open_shell(err_msg)

def verify_shm():
    if oshelper.check_shm():
        err_msg=_("""\
Your /dev/shm directory is a symbolic link, please run:
    rm /dev/shm && mkdif /dev/shm
    mount --types tmpfs --options nosuid,nodev,noexec shm /dev/shm
Also ensure that mode 1777 is set:
    chmod 1777 /dev/shm
""")
        oshelper.show_msg_open_shell(err_msg)
        verify_shm()

def verify_files():
    if oshelper.check_repos_conf_dir():
        pass
    else:
        oshelper.show_msg_open_shell(_("Please review your repos.conf directory, something is wrong"))
        verify_files()
    if oshelper.check_gentoo_conf_repo():
        pass
    else:
        oshelper.show_msg_open_shell(_("Please review your gentoo.conf file, something is wrong"))
        verify_files()
    if oshelper.check_resolv_conf():
        pass
    else:
        oshelper.show_msg_open_shell(_("Please review your resolv.conf file, something is wrong"))
        verify_files()

def verify_mounts():
    oshelper.verify_root()
