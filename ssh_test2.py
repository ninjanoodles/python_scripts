#!/usr/bin/python


import pssh


hostname='csdev2vm3'
user = 'root'
password = 'w0rk=-=0rd3r'
command = 'ls'

lines = pssh.ssh_func(hostname, user, password, command)

for line in lines:
  print line
