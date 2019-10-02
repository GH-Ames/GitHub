#!/usr/bin/python

dict = {}
file = open('testinfo.txt','r')

for line in file:
    line = line.strip()
    line = line.translate(None, '!"#$%&\'()*+,-/:;<=>?@[\\]^_`{|}~')
    line = line.lower()
    list = line.split(' ')

    for word in list:
        if word in dict:
            count = dict[word]
            count += 1
            dict[word] = count
        else:
            dict[word] = 1

for word,count in dict.iteritems():
    print word + ": " + str(count)

