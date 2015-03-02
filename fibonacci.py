#!/usr/bin/python

"""
Take an argument and check if it's an integer and greater than zero.
From there, generate the fibonacci sequence until it hits the argument
E.g fibonacci.py 5 will output 0, 1, 1, 2, 3
"""

import sys
def getInput():
    userType = False
    userInput = input("Enter a number to add up the fib sequence: ")
    try:
        int(userInput)
        userType = True
    except ValueError:
        print "Your Input: ", userInput, "is not an integer. Exiting!!"
        userType = False

    return (userType, userInput)


def main():
    fibArray = []
    inUser = getInput()
    if inUser[0] is True:
        for num in range(inUser[1]):
            if num == 0 or num == 1:
                fibArray.append(num)
            else:
                newNum = fibArray[-1] + fibArray[-2]
                fibArray.append(newNum)

        print "FibArray: ", fibArray

        print "Total of all numbers in Array: ", sum(fibArray)

if __name__ == "__main__":
    main()
