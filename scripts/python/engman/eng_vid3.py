#!/usr/bin/python


if True:
    print "hello"
    print "other"
    # single line comment

    """
    multi-line comment
    more comments here
    this scirpts rocks
    """
    print "world"
    name = 'engineer man'
    num1 = 5
    num2 = 8
    num3 = num1 + num2
    print num3
    num4 = 12; num5 = 3; num6 = num4 + num5; print num6

    # continuance
    long_name = \
        'this is something' + \
        'more text' + \
        'still more text'
print long_name
print 'try this', # the ',' avoids an automatic new line on the end???

# Vid4 - strings and numbers
# single line string
text = 'testing'
multi = """first""" \
    """next""" \
    """third"""
print multi

# substring
name = 'engineer man'
first_name = name[0:8] # foo[value:value]
print first_name

# integer
num1 = 6
print num1
print "num1\n\n"

# float
dec1 = 5.4
print dec1

# conversion to string
to_string = str(num1)
print to_string
what = type(to_string)
print what

# conversion to int / float
num_string = '5' # '' gives you text version of 5 vs a numbers
to_int = int(num_string)
print to_int
whatB = type(to_int)
print whatB
