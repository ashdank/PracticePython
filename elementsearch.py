a = [1, 3, 5, 30, 42, 43, 500]
b = 5

def match(x,y):
    for element in x:
        if element == y:
            print "True"
        else:
            print "False"

print match(a,b)
