#Copyright (C) Christopher Díaz Riveros <chrisadr@gentoo.org>
#
#begin.py is part of Stager.
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

import pym.stager.walkthrough as walkthrough 


def init(args):
    """The init function takes args from main program and parses them.

    Possible args:
    
    @step: wheter to select a specific installation step
    """
    if args.step != 0:
        walkthrough.resume(args.step,args)
    else:
        walkthrough.begin(args)
