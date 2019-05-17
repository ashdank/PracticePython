'''Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list.
For practice, write this code inside a function.'''

a = [5, 10, 15, 20, 25]

def list(m):
    new = []
    x = m[0]
    y = m[-1]
    new.append(x)
    new.append(y)
    print new

print list(a)
