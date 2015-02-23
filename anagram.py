#!/usr/bin/python

""" This script takes two command line arguments.
It will then compare if the two qualifies as anagrams.
Two criterias have to meet. They have the exact amount of characters.
The letters are case insensitive.
"""
import sys
anagramDict1 = {}
anagramDict2 = {}

def errorMsg():
    print "Boo!! The anagram Police says you shall not pass GO!!"

def main():
    if len(sys.argv) < 3:
        print "You need to give two arguments to compare anagrams. Exiting!! \n"
        sys.exit(2)

    if len(sys.argv[1]) !=  len(sys.argv[2]):
        print "The number of characters in the arguments given are different"
        print "first argument has count of: ", len(sys.argv[1])
        print "second argument has count of: ", len(sys.argv[2])
        errorMsg()
        print "exiting!!"
        sys.exit(2)

    firstArg = list(sys.argv[1].lower())
    secondArg = list(sys.argv[2].lower())

    print "First and second Arg", firstArg, secondArg

    for letter1 in firstArg:
        print "letter", letter1

        for letter2 in secondArg:
            if letter1 == letter2:
                secondArg.remove(letter2)

    print "First and second Arg", firstArg, secondArg
    if len(secondArg) == 0:
        print "Yes, your arguments qualifies as an anagram"
    else:
        errorMsg()

if __name__ == "__main__":
    main()
