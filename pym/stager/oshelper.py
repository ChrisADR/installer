import os
import subprocess

def clear_screen():
    os.system('clear')


def open_shell():
    print("I'm going to open a new terminal inside stager,\n\
you need to exit with the 'exit' command ")
    res = subprocess.run("/bin/bash")
    if res.returncode!=0:
        raise ChildProcessError()
