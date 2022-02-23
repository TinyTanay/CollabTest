#The return allows us to return info from a function

def cube(num):
    return num*num*num

print(cube(4))

#Whcih will print 4^3 which is 64, however without the return function, it would print none.
#You can also do this

def square(num):
    return num*num*num

result = square(4)
square(result)

#Which will rturn 64
