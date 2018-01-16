#Copyright (C) Christopher Díaz Riveros <chrisadr@gentoo.org>
#
#step6.py is part of Installer.
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
import pym.installer.step7 as step7

welcome_msg="""\
                            Step 6 - Entering the chroot
================================================================================
Congratulations!! Your are about to enter into your brand new Gentoo system.
Please keep in mind that if you are at this point, you should check that all
the necessary filesystems are linked (step 5) and if for some reason something
goes wrong, you can resume from here (in most cases and if you don't need to
change your partition table or filesystems and still have internet connection).

I'll execute the following command, and after that you'll need to execute the
following two:

    chroot /mnt/gentoo /bin/bash
    source /etc/profile         #(this will set all the ENV variables)
    export PS1="(chroot) $PS1"   #(this will help you to recognize the terminal)

If you created some extra partitions like home or boot, now is a good time to
mount them as well.

    mkdir /{boot,home}
    mount /dev/sdXy /{boot,home}

Finally, run `installer beginner -s 7` to continue with the installation.
"""

def init(args):
    if args.tui:
        pass
    else:
        prepare_chroot()

def prepare_chroot():
    global welcome_msg
    oshelper.show_msg_open_chroot(welcome_msg)
