#!/usr/bin/python

import os
import sys
#import filecmp

def diff_func(file1, file2):

  args = sys.argv[1:]
  file1 = args[0]
  file2 = args[1]

  file1_lines = file(file1).read().split('\n') 
  file2_lines = file(file2).read().split('\n')

  file1_lines_set = set(file1_lines)
  file2_lines_set = set(file2_lines)

  file2_added = file2_lines_set - file1_lines_set
  file2_removed = file1_lines_set - file2_lines_set

  print "Lines added to",file2 
  count = 1
  for line in file2_lines:
    if line in file2_added:
      text = str(count) + ': ' + line 
      print text
    count += 1

  print "Lines removed from",file1
  count = 1
  for line in file1_lines:
    if line in file2_removed:
      text = str(count) + ': ' + line
      print text
    count += 1 

def main():
 
  args = sys.argv[1:]
  file1 = args[0]
  file2 = args[1]
 
  diff_func(file1, file2)

if __name__ == "__main__":
  main()
