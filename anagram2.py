#!/usr/bin/python

"""
Parse a file and look for any words that are anagrams to each other
"""

dict = {}

try:
    with open("dictionary", "r+") as f:
        for line in f:
            for x in line.split():
                #print "X: ", x
                #y = ''.join(sorted(list(x)))
                dict.setdefault(''.join(sorted(list(x))),[]).append(x)
                #print "Y: ", y
except:
    print "What hop-pan here?!!!?!"

for key in dict:
    if len(dict[key]) > 1:
        print "-> ", key, " ", dict[key]
