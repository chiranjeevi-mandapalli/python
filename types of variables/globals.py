# x is global y is local
x = 10
def fun():
    y =90
    print(y)
fun()
print(x)

x = 20
def fun():
    y =90
    print(x)
    print(y)
fun()
print(x)
# in python there are default globa;l variables present we can chec by using global keyword
x = 20
def fun():
    y =90
    print(x)
    print(y)
    print(globals())
fun()
print(x)
print(globals())

# we can also have same variable name in global and local aslo

x = 20
def fun():
    x =90
    print(x)

fun()

# if we want to consider the global x as the main thing then use global keyword
x = 20
def fun():
    global x # here x is the global and x values is assigned in the next step instead of considering local variable
    x = 90
    print(x)
fun()
print(x)