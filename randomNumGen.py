#!/usr/bin/env python
import random

""" 2nd attempt at writing a random number guessing game
D. Nguyen 2015-02-15
"""

def main():
    print "Guess a number between 1 and 100"
    randomNum = random.randint(1,100)
    count = 0

    flag = False

    while not flag:
        guessNum = input("guess a number %s", count)

        if guessNum == randomNum:
            print "Hooray, you guessed right"
            flag = True
        elif guessNum < randomNum:
            print "Guess higher"
        else:
            print "Guess lower"

        count = count + 1

if __name__ == "__main__":
    main()
