#!/bin/sh


usage () {
  echo "usage: $0"
  echo "	-e add server(s) to the exclusion list"
  echo "	-f list of server name(s) to action"
  echo "	-g blacklist in G2 only"
  echo "	-h this message"
  echo "	-p close in platform only"
  echo "	-s server(s) to action"
}

while getopts ":ef:ghps:" option
do
  case "$option" in
    e) exclude=1;;
    f) file="$OPTARG";;
    g) gtwo=1;;
    h) usage
       exit 0
       ;;
    p) plat=1;;
    s) server="$OPTARG";;
    *) echo "Error: unknown option -$OPTARG"
       usage
       exit 1
       ;;
  esac
done

if [ $file ]; then
  # chk if file exists
  if [ 
  echo "-file was selected"
fi
