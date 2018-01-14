#Copyright (C) Christopher Díaz Riveros <chrisadr@gentoo.org>
#
#walkthrough.py is part of Installer.
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

def begin(args):
    """Begin function starts the interactive tutorial for installing Gentoo Linux.
    Possible args:

    @tui: wheter to display information in TUI or CLI 
    """
    import pym.installer.step1 as step1
    step1.init(args)


def resume(step,args):
    """Resume function resumes the interactive tutorial from a specific step in tutorial.
    Possible args:

    @tui: wheter to display information in TUI or CLI
    """
    if step==1:
        import pym.installer.step1 as step1
        step1.init(args)
    elif step==2:
        import pym.installer.step2 as step2
        step2.init(args)
    elif step==3:
        import pym.installer.step3 as step3
        step3.init(args)
    elif step==4:
        import pym.installer.step4 as step4
        step4.init(args)
    elif step==5:
        import pym.installer.step5 as step5
        step5.init(args)
    elif step==6:
        import pym.installer.step6 as step6
        step6.init(args)
    elif step==7:
        import pym.installer.step7 as step7
        step7.init(args)
    elif step==8:
        import pym.installer.step8 as step8
        step8.init(args)
    elif step==9:
        import pym.installer.step9 as step9
        step9.init(args)
    elif step==10:
        import pym.installer.step10 as step10
        step10.init(args)
    elif step==11:
        import pym.installer.step11 as step11
        step11.init(args)