#!/usr/bin/python

import sys
import os
import random


def bah(bob):
    for idx in range(1,len(bob)):
        x = bob[idx]
        y = bob[idx - 1]
        print "Orig: ", idx, " x: ", x
        while idx > 0:
            storedVal = bob[idx]
            if bob[idx] < bob[idx - 1]:
                bob[idx] = bob[idx - 1]
                bob[idx - 1]  = storedVal
                #swap #s
                idx = idx - 1
                print "temp: ", bob, " idx: ", idx, " x: ", bob[idx], " y: ", bob[idx - 1], "\n"
            else:
                print "\n"
                idx = -1

    print bob

a = [8,4,2,9,2,0,1]
bah(a)
