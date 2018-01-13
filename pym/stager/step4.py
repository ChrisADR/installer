import pym.stager.oshelper as oshelper
import pym.stager.step5 as step5

welcome_msg='''\
                        Step 4 - Configuring compile options
===============================================================================
Now we need to prepare Portage for the first update. All the env variables used
by Portage are written in /mnt/gentoo/etc/portage/make.conf,for a more detailed
list of all possible variables, refer to:

/mnt/gentoo/usr/share/portage/config/make.conf.example

Since we are going to prepare the first update, we only need to set these
variables:(you can use `nano` or another text editor)

    CFLAGS="-march=native -O2 -pipe"
Explanation:
    -march=native: tells the compiler to select the target
                   architecture of the current system.
    -O2:(capital O letter) gcc optimization class flag, recommended.

    MAKEOPTS="-jX"
Where:
    X: number of CPUs (CPU cores) plus one. Example: -j2
'''

def init(args):
    if args.tui:
        pass
    else:
        prepare_make_conf()
        check_data_saved()
        step5.init(args)

def prepare_make_conf():
    global welcome_msg
    oshelper.show_msg_open_shell(welcome_msg)
    
def check_data_saved():
    if oshelper.check_makeconf_march():
        oshelper.print_and_wait("Great! Now we can start Step 5")
    else:
        oshelper.show_msg_open_shell("Please review your make.conf file, something is wrong")
        check_data_saved()
