def plus_one(n):
    return n + 1 

add_one = plus_one 
print(add_one(5))


# Functions in functions 
def plus_one(n):
    def add_one(n):
        return n + 1


    result = add_one(n)
    return result

print(plus_one(4))


#### Decorators #### 

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

def say_hello(): ##  We have a function that returns 'hello there'
    return 'hello there'

decorate = uppercase_decorator(say_hello) # Decorate it
print(decorate())

# better way to do it 

@uppercase_decorator
def say_hii():
    return 'hii'

print(say_hii())


def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print("My arguments are: {0}, {1}".format(arg1,arg2))
        function(arg1, arg2)
    return wrapper_accepting_arguments


@decorator_with_arguments
def cities(city_one, city_two):
    print("Cities I love are {0} and {1}".format(city_one, city_two))

cities("Nairobi", "Accra")
