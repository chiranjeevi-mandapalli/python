# Types of functions:
# 1) user defined functions
# 2) built in functions
# 3) lambda functions
# 4) Recursive function

## in python main function there is no need to write if we want to write we can write it explicitly
## By default python call main function all the lines except function are kept in main function by default
## python uses python interpreter

def add1():
    a = 10
    b = 20
    c = a + b
    print(c)


def add(x, y):
    d = x + y
    print(d)


def addValue():
    a = 10
    b = 50
    return a + b

def power_of(a,b=0): # b=0 will be used as default argument when no value is specified for b
    c = a**b
    print(c)

add1()
add(10, 20)
res = addValue()
print(res)
power_of(2,5)
