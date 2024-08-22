x = lambda a: a + 10 
print(x(5))

x = lambda a, b: a + b 
print(x(1,3))

x = lambda a: a[1:]

print(x('hello'))
print(x('h'))



# Creating Anonymous functions

def myfunc(n):
    return lambda a : a * n 

mydoubler = myfunc(2) # This is now equal to the lambda function substituting n 
print(mydoubler(2))

