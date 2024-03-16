def power_of(num, pow):
    return num ** pow


print(power_of(2, 5))

# genaral syntax for lambda
# lambda args: exp
res = (lambda num, pow: num ** pow)(2, 5)
print(res)

quotient = lambda num, den: num / den

res = quotient(100, 2)
print(res)
res1 = quotient(10, 2)
print(res1)
