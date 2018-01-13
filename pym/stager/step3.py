import pym.stager.oshelper as oshelper
import pym.stager.step4 as step4

welcome_msg="""\
                            Step 3 - Installing Stage3
===============================================================================

Before to be able to download a stage3 tarball, you need to check wheter your
date and time is correct, not doing so could produce unexpected results or it
may be impossible to download it from a trusted mirror.

You can use `date` command to verify. Official Gentoo Installation media
includes `ntpd` command, which may help you in the syncronization. Using ntpd
requires that you send your IP adrress to the time server, if that's a problem
you can set it manually with the `date` command itself.

For more detailed info, please refer to:
https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Stage
"""

stage3_download_msg="""\
Now you need the download a stage3 tarball. Stage3 contains all the required
data to be able to build your system. Check the next URL for a mirror list:

https://www.gentoo.org/downloads/mirrors/

Once you find the perfect mirror, you need to download a stage3 for your
specific architecture. Usually you'll find a URL like:

protocol://mirror/releases/amd64/autobuilds/stage3_dir/stage3*.{bz2|xz}

Move to /mnt/gentoo and use one of the following commands:
    wget <URL>
    links <URL> and choose the tarball in the cli-browser

Remember to download .DIGEST or .DIGEST.asc if you want to verify and validate
the stage3 tarball.

More information about validation and verification please refer to:
https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Stage#Verifying_and_validating
"""

unpack_msg="""\
Now that stage3 is located in /mnt/gentoo you can unpack the contents. Please
use the exact command:

    tar xpf stage3-*.tar.{bz2,xz} --xattrs-include='*.*' --numeric-owner

Explanation:
    x: stands for extract
    p: stands for preserve permissions
    f: stands for file
    --xattrs-include='*.*': preserves extended attributes
    --numeric-owner: keep UID and GID from tarball
"""

def init(args):
    if args.tui:
        pass
    else:
        prepare_date()
        prepare_stage3_download()
        prepare_unpack()
        step4.init(args)


def prepare_date():
    global welcome_msg
    oshelper.show_msg_open_shell(welcome_msg)

def prepare_stage3_download():
    global stage3_download_msg
    oshelper.show_msg_open_shell(stage3_download_msg)

def prepare_unpack():
    global unpack_msg
    oshelper.show_msg_open_shell(unpack_msg)
