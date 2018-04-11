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

import pym.installer.step1 as step1
import pym.installer.step2 as step2
import pym.installer.step3 as step3
import pym.installer.step4 as step4
import pym.installer.step5 as step5
import pym.installer.step6 as step6
import pym.installer.step7 as step7
import pym.installer.step8 as step8
import pym.installer.step9 as step9
import pym.installer.step10 as step10
import pym.installer.step11 as step11


def begin(index):
    """Begin function starts the interactive tutorial for installing Gentoo Linux.
    Possible arguments:

    @index: defines in which step begin.
    """
    if not index or index == 1:
        step1.init()
    elif index==2:
        step2.init()
    elif index==3:
        step3.init()
    elif index==4:
        step4.init()
    elif index==5:
        step5.init()
    elif index==6:
        step6.init()
    elif index==7:
        step7.init()
    elif index==8:
        step8.init()
    elif index==9:
        step9.init()
    elif index==10:
        step10.init()
    elif index==11:
        step11.init()
