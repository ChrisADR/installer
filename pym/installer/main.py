# -*- coding: UTF-8 -*-
#Copyright (C) Christopher Díaz Riveros <chrisadr@gentoo.org>
#
#main.py is part of installer.
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

import argparse
import os

import pym.installer.beginner as beginner
import pym.installer.generate as generate
import pym.installer.cleanup as cleanup
import pym.installer.config as config

def main():
    try:
        check_permission()
        parser = generate_parser()
        args = parser.parse_args()
        if args.action=="beginner":
            beginner.init(args)
        elif args.action=="generate":
            generate.init(args)
        elif args.action=="cleanup":
            cleanup.init(args)
        else:
            raise ValueError()
    except ValueError:
        print(_("You need to provide an action, see installer --help or -h for more info"))
    except PermissionError:
        print(_("You need to be root for using installer"))


def check_permission():
    if os.geteuid() != 0:
        raise PermissionError()


def generate_parser():
    parser = argparse.ArgumentParser(
            description=config.long_description,
            epilog=_("If you find this useful or find a bug please contact to: {}").format(config.author_email))
    parser.add_argument("-v", "--version",
            action="version",
            version="%(prog)s {}".format(config.version))
    subparsers = parser.add_subparsers(
            title=_("available subcommands"),
            description=_("Installer implements two ways of installing Gentoo Linux,\
            from scratch and from an existing system."),
            help=_("for specific info use installer <command> --help"),
            metavar=_("<command>"),
            dest="action")
    beginner_parser = subparsers.add_parser("beginner",
            help=_("begin a new Gentoo Linux installation"))
    beginner_exclusive_group = beginner_parser.add_mutually_exclusive_group()
    beginner_exclusive_group.add_argument("-s", "--step",
            metavar="N",
            default=0,
            choices=[1,2,3,4,5,6,7,8,9,10,11],
            type=int,
            help=_("begin on a specific step of installation"))
    beginner_exclusive_group.add_argument("-t", "--tui",
            action="store_true",
            dest='tui',
            help=_("launch Terminal User Interface"))
    generate_parser = subparsers.add_parser("generate",
            help=_("generate a stageX tarball from current system"))
    generate_parser.add_argument("-k","--include-kernel",
            action='store_true',
            dest='kernel',
            help=_("include /usr/src/ directory in stageX"))
    cleanup_parser = subparsers.add_parser("cleanup",
            help=_("clean installer from /mnt/gentoo"))
    return parser
