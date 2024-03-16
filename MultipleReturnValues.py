def return_multiple():
    a = 10
    b =20
    c = 3.05
    return a

def return_multiple1():
    a = 10
    b =20
    c = 3.05
    return a,b

def return_multiple2():
    a = 10
    b =20
    c = 3.05
    return a,b,c

# python fiunction can return multiple values also
# which store in tuple

print(return_multiple())
print(return_multiple1())
print(return_multiple2())

# we can assign the values with some ref also

res1,res2,res3=return_multiple2()
print(res1)
print(res2)
print(res3)

