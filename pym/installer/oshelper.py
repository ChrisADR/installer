# -*- coding: UTF-8 -*-
#Copyright (C) Christopher Díaz Riveros <chrisadr@gentoo.org>
#
#oshelper.py is part of Installer.
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

import os
import sys
import subprocess
import time

import pym.installer.config as config

def clear_screen():
    os.system('/usr/bin/clear')

def open_shell():
    print(_("Opening new shell inside installer, use 'exit' to close and show next message:"))
    res = subprocess.call('/bin/bash')
    if res!=0:
        raise ChildProcessError()

def open_chroot():
    print(_("Chrooting into the new Gentoo system, run `installer beginner -s 7`"))
    res = subprocess.call(['/bin/chroot','/mnt/gentoo','/bin/bash'])
    if res!=0:
        raise ChildProcessError()

def handle_error():
    print(_('Something went wrong with the terminal, please verify it.'))
    sys.exit(1)

def die_with_msg(msg):
    print(msg)
    sys.exit(1)

def show_msg_open_shell(msg):
    clear_screen()
    print(msg)
    try:
        open_shell()
    except ChildProcessError:
        handle_error()

def show_msg_open_chroot(msg):
    clear_screen()
    print(msg)
    try:
        open_chroot()
    except ChildProcessError:
        handle_error()

def show_msg(msg):
    clear_screen()
    print(msg)

def print_and_wait(msg):
    print(msg)
    time.sleep(5)

"""

Misc checks

"""

def check_makeconf_march():
    res = subprocess.call(['/bin/grep','march','/mnt/gentoo/etc/portage/make.conf'],stdout=subprocess.DEVNULL)
    if res!=0:
        return False
    else:
        return True

def check_repos_conf_dir():
    return os.path.isdir('/mnt/gentoo/etc/portage/repos.conf')

def check_gentoo_conf_repo():
    if (os.path.exists('/mnt/gentoo/etc/portage/repos.conf/gentoo.conf') or os.path.exists('/mnt/gentoo/etc/portage/repos.conf/repos.conf')):
        return True
    else:
        return False

def check_resolv_conf():
    return os.path.exists('/mnt/gentoo/etc/resolv.conf')

def check_shm():
    return os.path.islink('/dev/shm')

def test_connection(host):
    res = subprocess.call(['/bin/ping','-c','2','%s'%(host)],stdout=subprocess.DEVNULL)
    return res


"""

installer self instalation inside the new system.

"""


def download_installer():
    return subprocess.call(['/usr/bin/wget','-qP','/tmp','https://github.com/ChrisADR/installer/archive/v%s.tar.gz'%(config.version)])

def extract_installer():
    return subprocess.call(['/bin/tar','xf','/tmp/v%s.tar.gz'%(config.version),'-C','/tmp'])

def install_installer():
    subprocess.call(['/usr/bin/python','/tmp/installer-%s/setup.py'%(config.version),'install','--prefix=/mnt/gentoo/usr','--record','/tmp/installer_files.txt'],cwd='/tmp/installer-%s'%(config.version))
    subprocess.call(['/usr/bin/python','/tmp/installer-%s/setup.py'%(config.version),'install_data','--root=/mnt/gentoo'],cwd='/tmp/installer-%s'%(config.version))


def bootstrap_in_chroot():
    res_download = download_installer()
    if res_download==0:
        res_extract = extract_installer()
        if res_extract==0:
            install_installer()
        else:
            raise ChildProcessError
    else:
        raise ConnectionError


"""

Mounting functions:

mount_* is designed to mount filesystems.
check_* is designed to check if filesystems are mounted.
verify_* is designed as abstraction layer for step*.py

"""

def mount_proc_fs():
    return subprocess.call(['/bin/mount','--types','proc','/proc', '/mnt/gentoo/proc'])

def mount_rbind_sys():
    return subprocess.call(['/bin/mount','--rbind','/sys', '/mnt/gentoo/sys'])

def mount_rslave_sys():
    return subprocess.call(['/bin/mount','--make-rslave', '/mnt/gentoo/sys'])

def mount_rbind_dev():
    return subprocess.call(['/bin/mount','--rbind', '/dev', '/mnt/gentoo/dev'])

def mount_rslave_dev():
    return subprocess.call(['/bin/mount','--make-rslave', '/mnt/gentoo/dev'])

def check_mnt_gentoo():
    res = subprocess.call(['/bin/findmnt','/mnt/gentoo'],stdout=subprocess.PIPE)
    if res!=0:
        return False
    else:
        return True

def check_mount_proc():
    res = subprocess.call(['/bin/findmnt','/mnt/gentoo/proc'],stdout=subprocess.PIPE)
    if res!=0:
        return False
    else:
        return True


def check_mount_sys():
    res = subprocess.call(['/bin/findmnt','/mnt/gentoo/sys'],stdout=subprocess.PIPE)
    if res!=0:
        return False
    else:
        return True

def check_mount_dev():
    res = subprocess.call(['/bin/findmnt','/mnt/gentoo/dev'],stdout=subprocess.PIPE)
    if res!=0:
        return False
    else:
        return True

def verify_root():
    if(check_mnt_gentoo()):
        pass
    else:
        die_with_msg(_("Error: /mnt/gentoo not mounted, please verify."))

def verify_proc():
    if(check_mount_proc()):
        pass
    else:
        mount_proc_fs()

def verify_sys():
    if(check_mount_sys()):
        pass
    else:
        mount_rbind_sys()
        mount_rslave_sys()

def verify_dev():
    if(check_mount_dev()):
        pass
    else:
        mount_rbind_dev()
        mount_rslave_dev()

"""
generate command

"""


def generate_stagex(args):
    cur_date=time.strftime("%Y%m%d")
    stageX_name="stageX-%s.tar.xz"%(cur_date)
    tar_cmd=[]
    tar_cmd.append('/bin/tar')
    tar_cmd.append('cpf')
    tar_cmd.append(stageX_name)
    tar_cmd.append("--xattrs-include='*.*'")
    tar_cmd.append('--numeric-owner')

    if args.kernel:
        tar_cmd.append('/usr/src/')

    tar_cmd.append('/etc/portage')
    tar_cmd.append('/etc/timezone')
    tar_cmd.append('/etc/locale.gen')
    tar_cmd.append('/var/lib/portage/world')

    subprocess.call(tar_cmd,stderr=subprocess.DEVNULL)


"""
cleanup command

"""

def clean_installer():
    if(check_installed_txt()):
        remove_installed_files()
    else:
        if os.path.isdir('/mnt/gentoo/tmp/installer-%s'%(config.version)):
            install_installer()
        else:
            download_installer()
            install_installer()
        remove_installed_files()

def check_installed_txt():
    if os.path.exists('/mnt/gentoo/tmp/installer_files.txt'):
        return True
    else:
        return False

def remove_installed_files():
    with open('/mnt/gentoo/tmp/installer_files.txt') as installer_files:
        files_list = installer_files.readlines()
        for element in files_list:
            element=element.rstrip()
            if element.startswith("/mnt/gentoo/"):
                if os.path.exists(element):
                    subprocess.call(["/bin/rm",element])
            else:
                element="/mnt/gentoo"+element
                if os.path.exists(element):
                    subprocess.call(["/bin/rm",element])


"""
Finelize the prototype

"""

def finish_prototype(msg):
    print(msg)
    print(_('Thank you for trying installer'))
    sys.exit(0)

