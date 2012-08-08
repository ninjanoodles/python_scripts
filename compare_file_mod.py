#!/usr/bin/python

import os
import sys

sys.path.append("/root/scripts/cust-packages")

import pexpect
import base64
import pssh
import diff


def main():

  args = sys.argv[1:]
  config_file = args[0]
 
  config_lines = file(config_file).read().split('\n')
  del config_lines [-1]
  for line in config_lines:
    config_args = line.split(',')
    hostname = config_args[0]
    filename = config_args[1]
    remote_dir = config_args[2]
    command = 'cat ' + remote_dir + filename
  
    user = 'root'
    password = base64.b64decode("dzByaz0tPTByZDNy")
  
    remote_lines = pssh.ssh_func(hostname, user, password, command)
    remote_set = set(remote_lines)

    local_lines = file(filename).read().split('\n')
    local_set = set(local_lines)

    results = diff.diff_func (local_set, remote_set, remote_lines, local_lines)
    print hostname
    for line in results:
      print line

if __name__ == "__main__":
  main()
