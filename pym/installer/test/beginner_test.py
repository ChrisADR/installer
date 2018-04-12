#Copyright (C) Christopher Díaz Riveros <chrisadr@gentoo.org>
#
#beginner_test.py is part of Installer.
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

import unittest

import pym.installer.walkthrough as walkthrough

class BeginnerTestCase(unittest.TestCase):

    def test_begin_bigger(self):
        with self.assertRaises(ValueError):
            walkthrough.begin(15)

    def test_begin_lower(self):
        with self.assertRaises(ValueError):
            walkthrough.begin(-1)
