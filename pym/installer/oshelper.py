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

def clear_screen():
    os.system('clear')

def open_shell():
    print("I'm going to open a new terminal inside installer,you need to exit with 'exit'")
    res = subprocess.call('/bin/bash')
    if res!=0:
        raise ChildProcessError()

def open_chroot():
    print("Chrooting into the new Gentoo system, use `exit` to exit")
    res = subprocess.call(['/bin/chroot','/mnt/gentoo','/bin/bash'])
    if res!=0:
        raise ChildProcessError()

def handle_error():
    print('Something went wrong with the terminal, please verify it.')
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

def check_mnt_gentoo():
    res = subprocess.call(['/bin/findmnt','/mnt/gentoo'],stdout=subprocess.PIPE)
    if res!=0:
        return False
    else:
        return True

def check_makeconf_march():
    res = subprocess.call(['/bin/grep','march','/mnt/gentoo/etc/portage/make.conf'],stdout=subprocess.DEVNULL)
    if res!=0:
        return False
    else:
        return True

def print_and_wait(msg):
    print(msg)
    time.sleep(5)

def test_connection(host):
    res = subprocess.call(['/bin/ping','-c','2','%s'%(host)],stdout=subprocess.DEVNULL)
    return res

def finish_prototype(msg):
    print(msg)
    print('Thank you for trying installer')
    sys.exit(0)

def check_repos_conf_dir():
    return os.path.isdir('/mnt/gentoo/etc/portage/repos.conf')

def check_gentoo_conf_repo():
    return os.path.exists('/mnt/gentoo/etc/portage/repos.conf/gentoo.conf')

def check_resolv_conf():
    return os.path.exists('/mnt/gentoo/etc/resolv.conf')

def check_shm():
    return os.path.islink('/dev/shm')
