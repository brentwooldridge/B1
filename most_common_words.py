# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 14:22:04 2020

@author: Gamer
"""

import sys
from collections import Counter


try:
    num_words = int(sys.argv[1])
except:
    print "usage: most_common _words.py num words"
    sys.exit(1)

counter = Counter(word.lower()
                 for line in sys.stdin
                 for word in line.strip().split()
                 if word)

for word, count in counter.most_common(num_words):
    sys.stdout.write(str(count))  
    sys.stdout.write("\t")
    sys.stdout.write(word)
    sys.stdout.write("\n")                