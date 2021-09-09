# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 10:42:50 2020

@author: Gamer
"""

import sys
import re

regex = sys.argv[1]

for line in sys.stdin:
    if re.search(regex, line):
        sys.stdout.write(line)


