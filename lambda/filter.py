# general syntax for filter
# filter(function,sequence)
# filter return an object so we need to typecast

# traditional approach
lst = [10.15, 20, 30]


def fun(x):
    if x % 2 == 0:
        return True
    else:
        return False


res = list(filter(fun, lst))
print("Using function:", res)

# lambda approach
res1 = list(filter(lambda x: x % 2 == 0, lst))
print("Using Lamnda: ", res1)
