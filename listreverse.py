'''Ask the user for a string and print out whether this string is a palindrome or not.
A palindrome is a string that reads the same forwards and backwards.'''

#string_letters = []
string = raw_input("Enter a word/phrase: ")
string_2 = string[::-1]

if string == string_2:
    print "This is a palindrome"
else:
    print "Not a palindrome"
