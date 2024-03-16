# split()
from functools import reduce

s = "Guido Van Rossum"
print(s.split())

n = input("Enter numers to whcih we need to find avg\n")
str_array = n.split()
int_array = list(map(int, str_array))
print(int_array)
print(reduce(lambda x, y: x + y, int_array))
