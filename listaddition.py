#add the elements of one list to the other
# if one list is larger than the other, add 0s to the left of the smaller list equal to difference in length

m = [9, 9, 9]
n = [4, 5, 6, 7, 8]

def add_elements(a,b):
  difference = 0
  lst = []
  if len(b) > len (a):
    difference = len(b) - len(a)
    lst = [0] * difference 
    #print(lst)
    lst = lst + a
    a = lst
    print (a)
  
  elif len(a) > len (b):
    difference = len(a) - len(b)
    lst = [0] * difference 
    #print(lst)
    lst = lst + b
    b = lst
    print (b)
  
  for i in range(len(b)):
    b[i] = b[i] + a[i]
  return b

print(add_elements(m,n))
