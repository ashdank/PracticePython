'''Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4 to help you.
Take this opportunity to practice using functions, described below.'''
import sys
number = input("Pick a number:  ")
number = int(number)
if number > 0:
    for x in range (2, number - 1):
        if number%x == 0:
            print "This is not prime"
            break
        else:
            print "This is prime"
