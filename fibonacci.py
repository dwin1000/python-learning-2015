#!/usr/bin/python

"""
Take an argument and check if it's an integer and greater than zero.
From there, generate the fibonacci sequence until it hits the argument
E.g fibonacci.py 5 will output 0, 1, 1, 2, 3
"""

import sys

def fib(x):
    fibList = [0, 1]
    x = int(x) - 2
    for key in range(x):
        a = int(fibList[-1])
        b = int(fibList[-2])
        x = a + b
        fibList.append(x)
    return fibList



def main():
    if len(sys.argv) < 2 :
        print "No arguments given! Exiting! \n"
        sys.exit(1)
    elif int(sys.argv[1]) == 0:
        print "[0]"
    else:
        x = int(sys.argv[1])
        print fib(x)

if __name__ == "__main__":
    main()
