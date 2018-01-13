import os
import sys
import subprocess
import time

def clear_screen():
    os.system('clear')

def open_shell():
    print("I'm going to open a new terminal inside stager,you need to exit with 'exit'")
    res = subprocess.run('/bin/bash')
    if res.returncode!=0:
        raise ChildProcessError()

def open_chroot():
    print("Chrooting into the new Gentoo system, use `exit` to exit")
    res = subprocess.run(['/bin/chroot','/mnt/gentoo','/bin/bash'])
    if res.returncode!=0:
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

def show_initial_msg(msg):
    clear_screen()
    print(msg)

def check_mnt_gentoo():
    res = subprocess.run(['/bin/findmnt','/mnt/gentoo'],stdout=subprocess.PIPE)
    if res.returncode!=0:
        return False
    else:
        return True

def check_makeconf_march():
    res = subprocess.run(['/bin/grep','march','/mnt/gentoo/etc/portage/make.conf'],stdout=subprocess.DEVNULL)
    if res.returncode!=0:
        return False
    else:
        return True

def print_and_wait(msg):
    print(msg)
    time.sleep(5)

def test_connection(host):
    res = subprocess.run(['/bin/ping','-c','2','%s'%(host)],stdout=subprocess.DEVNULL)
    return res

def finish_prototype(msg):
    print(msg)
    print('Thank you for trying stager')
    sys.exit(0)

def check_repos_conf_dir():
    return os.path.isdir('/mnt/gentoo/etc/portage/repos.conf')

def check_gentoo_conf_repo():
    return os.path.exists('/mnt/gentoo/etc/portage/repos.conf/gentoo.conf')

def check_resolv_conf():
    return os.path.exists('/mnt/gentoo/etc/resolv.conf')

def check_shm():
    return os.path.islink('/dev/shm')
