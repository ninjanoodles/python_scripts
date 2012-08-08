#!/usr/bin/python

import fnmatch
import os
import sys

args = sys.argv[1:]
src = args[0]
pattern = args[1]
matches = []
for root, dirnames, filenames in os.walk(src):
  for filename in fnmatch.filter(filenames, pattern):
    matches.append(os.path.join(root,filename))
for match in matches:
  print match
