# -*- coding: UTF-8 -*-
#Copyright (C) Christopher Díaz Riveros <chrisadr@gentoo.org>
#
#curseshelper.py is part of Installer.
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

import curses
from curses import wrapper

import pym.installer.walkthrough as walkthrough

def launch_tui():
    stdscr = curses.initscr()
    wrapper(generate_tui)

def generate_tui(stdscr):
    stdscr.clear()
    prepare_curses(stdscr)
    stdscr.refresh()
    generate_title_window(stdscr)
    generate_info_window(stdscr)
    generate_arrow_window(stdscr)


def finish_windows():
    curses.endwin()

def prepare_curses(stdscr):
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)

def generate_title_window(stdscr):
    title_win = curses.newwin(4,curses.COLS-2,0,10)
    title_win.addstr(1,12,_("Welcome to installer TUI."))
    title_win.addstr(3,2,_("Use the arrow to select the step and press ENTER"))
    title_win.refresh()

def generate_info_window(stdscr):
    info_win = curses.newwin(13,60,5,12)
    info_win.box()
    info_win.addstr(1,2,_("Step 1: Welcome to Gentoo installer!"))
    info_win.addstr(2,2,_("Step 2: Preparing the disks"))
    info_win.addstr(3,2,_("Step 3: Installing Stage3"))
    info_win.addstr(4,2,_("Step 4: Configuring compile options"))
    info_win.addstr(5,2,_("Step 5: Installing the Gentoo base system"))
    info_win.addstr(6,2,_("Step 6: Entering the chroot"))
    info_win.addstr(7,2,_("Step 7: Configuring Portage"))
    info_win.addstr(8,2,_("Step 8: Configuring the system"))
    info_win.addstr(9,2,_("Step 9: Configuring the kernel"))
    info_win.addstr(10,2,_("Step 10: Configuring the system"))
    info_win.addstr(11,2,_("Step 11: Configuring the bootloader"))
    info_win.refresh()

def generate_arrow_window(stdscr):
    select_win = curses.newwin(13,5,5,7)
    select_win.box()
    select_win.keypad(True)
    index = 1
    print_arrow(select_win,index)
    while True:
        key = select_win.getch()
        if key == curses.KEY_UP:
            if (index-1) <= 0:
                index = 11
            else:
                index-=1
            print_arrow(select_win, index)
        elif key == curses.KEY_DOWN:
            if (index+1) >= 12:
                index = 1
            else:
                index+=1
            print_arrow(select_win,index)
        elif key in [curses.KEY_ENTER, ord('\n')]:
            break
    launch_step(index)

def print_arrow(select_win,index):
    for value in range(1,12):
        select_win.addstr(value,1,"   ")
    select_win.addstr(index,1," =>")
    select_win.refresh()

def launch_step(index):
    finish_windows()
    walkthrough.begin(index)
