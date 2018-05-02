# -*- coding: UTF-8 -*-
#Copyright (C) Christopher Díaz Riveros <chrisadr@gentoo.org>
#
#step1.py is part of Installer.
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

import pym.installer.step2 as step2
import pym.installer.oshelper as oshelper

welcome_msg=_('''\
                        Welcome to Gentoo installer!
================================================================================
Before begin we need to make sure that you reach www.gentoo.org to be able to
download stage3 tarball. You can check with: 

    ping -c 2 www.gentoo.org

For more detailed information refer to:
https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Networking
''')


def init():
    '''Init function begins the installation process, Here we check if
    we need to show output in TUI or CLI
    '''
    print_welcome_msg()
    process_connectivity(test_connectivity())
    step2.init()
        
def print_welcome_msg():
    global welcome_msg
    oshelper.show_msg_open_shell(welcome_msg)


def test_connectivity():
    print(_('Verifying connectivity with www.gentoo.org...'))
    response = oshelper.test_connection('www.gentoo.org')
    if response==0:
        return True
    else:
        return False


def process_connectivity(test):
    if test:
        oshelper.print_and_wait(_('We have connection!Now you can proceed to step 2'))
    else:
        process_problem()

def process_problem():
    oshelper.finish_prototype(_("This prototype was not capable to resolve the issue, please refer \n\
to Gentoo Handbook, section 'Configuring the network', for more info."))
