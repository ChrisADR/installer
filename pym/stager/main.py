import argparse
import os

def main():
    try:
        #if os.geteuid() != 0:
        #    raise PermissionError()

        parser = argparse.ArgumentParser(
                description="Stager is designed to aid users to install Gentoo Linux",
                epilog="If you find this useful or find a bug please contact to chrisadr@gentoo.org")

        parser.add_argument("-t", "--tui",
                action="store_true",
                help="launch Terminal User Interface")

        parser.add_argument("-v", "--version",
                action="version",
                version="%(prog)s 0.1.0dev")
        
        subparsers = parser.add_subparsers(
                title="available subcommands",
                description="Stager implements two ways of installing Gentoo Linux,\
                from scratch and from an existing system.",
                help="for specific info use stager <command> --help",
                metavar="<command>",
                dest="action")

        begin_parser = subparsers.add_parser("begin",
                help="begin a new Gentoo Linux installation")

        begin_parser.add_argument("-s", "--step",
                metavar="N",
                default=0,
                choices=[1,2,3,4,5,6],
                type=int,
                help="begin on a specific step of installation")

        generate_parser = subparsers.add_parser("generate",
                help="generate a stageX tarball from current system")

        args = parser.parse_args()

        if args.action=="begin":
            import pym.stager.begin as begin
            begin.init(args)
        elif args.action=="generate":
            import pym.stager.generate as generate
            generate.init(args)
        else:
            raise ValueError()

    except ValueError:
        print("You need to provide an action, see stager --help or -h for more info")
    except PermissionError:
        print("You need to be root for using stager")
        
