#!/usr/bin/python

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-arg1", "--arg1", help="Enter an argument value", action="store_true")
args = parser.parse_args()
if args.arg1:
  print("option was selected")

