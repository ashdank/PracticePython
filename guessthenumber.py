'''Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
then tell them whether they guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)'''

import random

number = random.randint(1,9)

guess = 0
count = 0

while True:
    guess = int(input("Guess a number: "))
    count = count + 1

    if number > guess:
        print "Too low"
        continue
    elif number < guess:
        print "Too high"
        continue
    else:
        print "You got it"
        print "You got it in", count, "tries"
        break
