# in order to find what is present in the module with description
# help(modulename) ex: help(math)
# if we want to find only name of the functions present in the module use
# dir(modulename) ex: dir(math)
# individual function also we can find out
# help(math.factorial())
import math

def get_factorial(x):
    return math.factorial(x)

def power_of(a,b):
    return math.pow(a,b)

def get_ceil(number):
    return math.ceil(number)

def get_floor(number):
    return math.floor(number)

print(get_factorial(5))
print(power_of(2,5))
print(get_ceil(5.5))
print(get_floor(10.2))

# print(help(math))
# print(dir(math))