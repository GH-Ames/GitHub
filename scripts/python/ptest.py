#!/usr/bin/python

# testing out psutil

import psutil
from pprint import pprint as pp

#for proc in psutil.process_iter(attrs=['pid', 'name', 'username', 'cmdline']):
#    print(proc.info)
#    if proc.name == 'xterm':
#        print "hello"

# find specific process
#pp([p.info for p in psutil.process_iter(attrs=['pid', 'name']) if 'emacs' in p.info['name']])

# find user processes
# pull the user with getpass
#import getpass
#pp([(p.pid, p.info['name'])
#    for p in psutil.process_iter(attrs=['name', 'username'])
#    if p.info['username'] == getpass.getuser()])
# root processes
pp([(p.pid, p.info['name'])
    for p in psutil.process_iter(attrs=['name', 'username'])
    if p.info['username'] == 'root'])
