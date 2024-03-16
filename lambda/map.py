# general syntax for map
# map(function,sequence)
# map return an object so we need to typecast

# traditional approach
lst = [1, 2, 3, 4]


def fun(x):
    return x ** 2


sqr_lst = list(map(fun, lst))
print("Using function:", sqr_lst)

# lambda approach
sqr_lst = list(map(lambda x: x ** 2, lst))
print("Using Lamnda: ", sqr_lst)
