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
    print(_("I'm going to open a new terminal inside installer,you need to exit with 'exit'"))
    res = subprocess.call('/bin/bash')
    if res!=0:
        raise ChildProcessError()

def open_chroot():
    print(_("Chrooting into the new Gentoo system, use `exit` to exit"))
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

def bootstrap_in_chroot():
    tag=config.version
    res_download = download_installer(tag)
    if res_download==0:
        res_extract = extract_installer(tag)
        if res_extract==0:
            install_installer(tag)
        else:
            raise ChildProcessError
    else:
        raise ConnectionError

def download_installer(tag):
    return subprocess.call(['/usr/bin/wget','-qP','/tmp','https://github.com/ChrisADR/installer/archive/v%s.tar.gz'%(tag)])

def extract_installer(tag):
    return subprocess.call(['/bin/tar','xf','/tmp/v%s.tar.gz'%(tag),'-C','/tmp'])

def install_installer(tag):
    subprocess.call(['/usr/bin/python','/tmp/installer-%s/setup.py'%(tag),'install','--prefix=/mnt/gentoo/usr','--record','/tmp/installer_files.txt'],cwd='/tmp/installer-%s'%(tag))

def test_connection(host):
    res = subprocess.call(['/bin/ping','-c','2','%s'%(host)],stdout=subprocess.DEVNULL)
    return res

def finish_prototype(msg):
    print(msg)
    print(_('Thank you for trying installer'))
    sys.exit(0)

def check_repos_conf_dir():
    return os.path.isdir('/mnt/gentoo/etc/portage/repos.conf')

def check_gentoo_conf_repo():
    return os.path.exists('/mnt/gentoo/etc/portage/repos.conf/gentoo.conf')

def check_resolv_conf():
    return os.path.exists('/mnt/gentoo/etc/resolv.conf')

def check_shm():
    return os.path.islink('/dev/shm')

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
