import pym.stager.oshelper as oshelper
import pym.stager.step7 as step7

welcome_msg="""\
                            Step 6 - Entering the chroot
================================================================================
Congratulations!! Your are about to enter into your brand new Gentoo system.
Please keep in mind that if you are at this point, you should check that all
the necessary filesystems are linked (step 6) and if for some reason something
goes wrong, you can resume from here (in most cases and if you don't need to
change your partition table or filesystems and still have internet connection).

I'll execute the following command, and after that you'll need to execute the
following two:

    chroot /mnt/gentoo /bin/bash

    source /etc/profile         #(this will set all the ENV variables)
    export PS1="(chroot) PS1"   #(this will help you to recognize the terminal)

If you created some extra partitions like home or boot, now is a good time to
mount them as well.

    mkdir /{boot,home}
    mount /dev/sdXy /{boot,home}

"""

def init(args):
    if args.tui:
        pass
    else:
        prepare_chroot()

def prepare_chroot():
    global welcome_msg
    oshelper.show_msg_open_chroot(welcome_msg)
