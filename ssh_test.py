#!/usr/bin/python

import os
import sys
import pexpect
import base64

def diff_func(set1, set2, lines2, lines1):
  
 
  file2_added = set2 - set1
  file2_removed = set1 - set2
 
  results = []
  results.append('Lines added to') 
  count = 1
  for line in lines2:
    if line in file2_added:
      text = str(count) + ': ' + line 
      results.append(text)
    count += 1

  results.append('Lines removed from')
  count = 1
  for line in lines1:
    if line in file2_removed:
      text = str(count) + ': ' + line
      results.append(text)
    count += 1 
  return results


def ssh_func(hostname, user, password, command):
  
  prompt="\#"
  child = pexpect.spawn ("ssh %s" %(hostname))
  child.expect("assword: ",timeout=120)
  child.sendline(password)
  child.expect(prompt)
  child.sendline(command)
  child.expect(prompt)
  response = child.before
  child.close()
  lines=response.split('\r\n')
  del  lines[0]
  del  lines[-1]
  return lines

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
  
    remote_lines = ssh_func(hostname, user, password, command)
    remote_set = set(remote_lines)

    local_lines = file(filename).read().split('\n')
    local_set = set(local_lines)

    results = diff_func (local_set, remote_set, remote_lines, local_lines)
    print hostname
    for line in results:
      print line

if __name__ == "__main__":
  main()
