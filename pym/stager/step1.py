import sys
import os

import pym.stager.step2 as step2
import pym.stager.oshelper as oshelper

welcome_msg="\n\
                        Welcome to stager!! \n\
==================================================================\n\
Before begin we need to make sure that you reach www.gentoo.org to\n\
be able to download stage3 tarball. You can check with a simple \n\n\
\tping -c 2 www.gentoo.org                                      \n\n\
Otherwhise I can try to do it for you. Please type one of these   \n\
options:\n\
\n\
\t[a]: try automatically\n\
\t[s]: spawn a shell to do it manually\n\
\t[e]: exit stager\n\
"

def init(args):
    """Init function begins the installation process, Here we check if 
    we need to show output in TUI or CLI
    """
    if args.tui:
        #TODO: Launch TUI interface
        pass
    else:
        oshelper.clear_screen()
        global welcome_msg 
        selection = input(welcome_msg)
        try:
            process_selection(selection)
        except ConnectionError:
            print("Cannot connect with www.gentoo.org")
            process_problem()

        step2.init(args)
        

def process_selection(selection):
    if selection=="a":
        test = test_connectivity()
        process_connectivity(test)
    elif selection=="s":
        try:
            oshelper.open_shell()
        except ChildProcessError:
            print("Something happended to your shell, please verify it.")
            sys.exit(1)
        test = test_connectivity()
        process_connectivity(test)
    elif selection=="e":
        print("Bye")
        sys.exit(0)
    else:
        selection = input("Not valid option. Select [a],[s] or [e]")
        process_selection(selection)


def test_connectivity():
    print("Verifying connectivity with www.gentoo.org")
    hostname = "www.gentoo.org"
    response = os.system("ping -c 2 %s > /dev/null" %(hostname))
    if response == 0:
        return True
    else:
        return False


def process_connectivity(test):
    if test:
        print("We have connection!Now you can proceed to step 2")
    else:
        raise ConnectionError()

def process_problem():
    print("This prototype was not capable to resolve the issue, please refer \n\
to Gentoo Handbook, section 'Configuring the network', for more info.")
    print("Thank you for trying stager")
    sys.exit(0)

