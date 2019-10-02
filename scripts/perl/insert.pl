#!/usr/bin/perl

use strict;
use warnings;

my @array;
my @ips;

open (IN, "/tmp/list") or die "could not open file $!\n";
while (<IN>) {
  chomp;
  my @val = split (/	/);
  push (@array, $val[0]);
}

foreach (@array) {
  print "ip: $_\n";
}
