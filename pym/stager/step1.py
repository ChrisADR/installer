#Copyright (C) Christopher Díaz Riveros <chrisadr@gentoo.org>
#
#step1.py is part of Stager.
#
#Stager is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License v2 as published by
#the Free Software Foundation, either version 2 of the License, or
#(at your option) any later version.
#
#Stager is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License v2 for more details.
#
#You should have received a copy of the GNU General Public License v2
#along with Stager.  If not, see <http://www.gnu.org/licenses/>.

import pym.stager.step2 as step2
import pym.stager.oshelper as oshelper

welcome_msg='''\
                                Welcome to stager!
===============================================================================
Before begin we need to make sure that you reach www.gentoo.org to be able to
download stage3 tarball. You can check with: 

    ping -c 2 www.gentoo.org

Otherwhise I can try to do it for you. Please type one of these options:
'''

input_msg='''\
    [a]: try automatically
    [s]: spawn a shell to do it manually
    [e]: exit stager
'''

def init(args):
    '''Init function begins the installation process, Here we check if
    we need to show output in TUI or CLI
    '''
    if args.tui:
        #TODO: Launch TUI interface
        pass
    else:
        print_welcome_msg()
        global input_msg
        selection = input(input_msg)
        try:
            process_selection(selection)
        except ConnectionError:
            print('Cannot connect with www.gentoo.org')
            process_problem()

        step2.init(args)
        
def print_welcome_msg():
    global welcome_msg
    oshelper.show_msg(welcome_msg)

def process_selection(selection):
    if selection=='a':
        test = test_connectivity()
        process_connectivity(test)
    elif selection=='s':
        try:
            oshelper.open_shell()
        except ChildProcessError:
            oshelper.die_with_msg('Error: something happended to your shell, please verify it.')
        test = test_connectivity()
        process_connectivity(test)
    elif selection=='e':
        oshelper.finish_prototype('Bye')
    else:
        selection = input('Not valid option. Select [a],[s] or [e]')
        process_selection(selection)


def test_connectivity():
    print('Verifying connectivity with www.gentoo.org...')
    response = oshelper.test_connection('www.gentoo.org')
    if response==0:
        return True
    else:
        return False


def process_connectivity(test):
    if test:
        oshelper.print_and_wait('We have connection!Now you can proceed to step 2')
    else:
        raise ConnectionError()

def process_problem():
    oshelper.finish_prototype("This prototype was not capable to resolve the issue, please refer \n\
to Gentoo Handbook, section 'Configuring the network', for more info.")

