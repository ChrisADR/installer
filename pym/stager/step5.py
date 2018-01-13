import pym.stager.oshelper as oshelper
import pym.stager.step6 as step6

welcome_msg='''\
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

    cp --deference /etc/resolv.conf /mnt/gentoo/etc
'''

prepare_mount_msg='''\
Before to enter the brand new Gentoo system, you need to mount certain
filesystems to be capable to change the Linux root. Use the following commands:

    mount --types proc  /proc   /mnt/gentoo/proc
    mount --rbind       /sys    /mnt/gentoo/sys
    mount --make-rslave         /mnt/gentoo/sys
    mount --rbind       /dev    /mnt/gentoo/dev
    mount --make-rslave         /mnt/gentoo/dev

Note: --make-rslave is needed for systemd support later in installation.
'''

def init(args):
    if args.tui:
        pass
    else:
        prepare_ebuild_repo()
        verify_files()
        verify_shm()
        prepare_mount_fs()
        step6.init(args)

def prepare_ebuild_repo():
    global welcome_msg
    oshelper.show_msg_open_shell(welcome_msg)

def prepare_mount_fs():
    global prepare_mount_msg
    oshelper.show_msg_open_shell(prepare_mount_msg)

def verify_shm():
    if oshelper.check_shm():
        err_msg="""\
Your /dev/shm directory is a symbolic link, please run:
    rm /dev/shm && mkdif /dev/shm
    mount --types tmpfs --options nosuid,nodev,noexec shm /dev/shm
Also ensure that mode 1777 is set:
    chmod 1777 /dev/shm
"""
        oshelper.show_msg_open_shell(err_msg)
        verify_shm()

def verify_files():
    if oshelper.check_repos_conf_dir():
        pass
    else:
        oshelper.show_msg_open_shell("Please review your repos.conf directory, something is wrong")
        verify_files()
    if oshelper.check_gentoo_conf_repo():
        pass
    else:
        oshelper.show_msg_open_shell("Please review your gentoo.conf file, something is wrong")
        verify_files()
    if oshelper.check_resolv_conf():
        pass
    else:
        oshelper.show_msg_open_shell("Please review your resolv.conf file, something is wrong")
        verify_files()
