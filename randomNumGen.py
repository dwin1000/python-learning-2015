#!/usr/bin/env python
import random
# bah
"""
Random number generator. You will have unlimited guesses
"""
def main():
    print "Guess a number between 1 and 100"
    randomNum = random.randint(1,100)

    found = False

    while not found:
        userGuess = input("Guess sucker!!! : ")

        if userGuess == randomNum:
            print "You got it sucka!!! Guess it right"
            found = True
        elif userGuess > randomNum:
            print "Guess Lower"
        else:
            print "Guess Higher!!!"


if __name__ == "__main__":
    main()
