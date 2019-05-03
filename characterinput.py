'''Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)'''

a = raw_input("What's your name?")
b = int(input("How old are you?"))

current_year = 2019
target = 100
years_to_hundred = target - b
year_100 = 2019 + years_to_hundred


print ("Hey " + a + "," + "You will turn 100 in the year: " + str(year_100))
