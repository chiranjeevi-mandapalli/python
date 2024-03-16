# general syntax for reduce
# reduce(function,sequence)
from functools import reduce

# traditional approach
lst = [1, 2, 3, 4, 5]


def fun(x, y):
    return x + y


res = reduce(fun, lst)
print("Using function:", res)

# using lambda

res = reduce(lambda x, y: x * y, lst)
print("Using Lambda:", res)
