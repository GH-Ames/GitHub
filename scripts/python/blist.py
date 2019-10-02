#!/usr/bin/python

#
# manage the blacklist, close and exclude operations for one or more servers
# g2 = blacklist
# platform = close
# exclude file (hosts.exclude.txt) = used by dht, g2, skfs, platform, ...
#

import argparse
import sys
parser = argparse.ArgumentParser()
parser.add_argument("-exclude", "--exlude", help="add server(s) to the exclusion list")
parser.add_argument("-file", "--file", help="file containing one or more servers")
parser.add_argument("-g", "--g", help="blacklist in g2")
parser.add_argument("-platform", "--platform", help="close in platform")
parser.add_argument("-s", "--server", nargs='+', help="server(s) to action")
if len(sys.argv)==1: # prints help when no args are provided
  parser.print_help()
  sys.exit(1)
args = parser.parse_args() # method. Returns a Namespace containing the arg(s)

def chkval (a): # function that checks contents of a file
  allint = None # no value to start with
  lista = a.split('.')
  num = len(lista)
  if num == 4: # nice. odds are we have a host ip or igrid hostname
    for item in lista: # check for ip or hostname
      if not type(item) == int:
        allint = 'no'
        break # no need to check further
    if allint is None: # all values of item passed the int test
      print 'IP = ', a
    else: # we likely have an igrid hostname
      print 'HOSTNAME =', a
  else: # something is not right with the data
    print '"{}"'.format(a), 'is not in #.#.#.# or text#.text#.ms.com format'

if args.file:
  print("\'--file\' option was selected")
  line = open(args.file,'r')
  for text in line:
    val = text.strip('\n')
    chkval(val)

if args.server:
    print("\'--server\' option was selected")
    print 'Value entered was:', args.server
    foo = args.server
    for stuff in foo:
        chkval(stuff)
