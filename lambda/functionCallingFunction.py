# we care calling a function fun1 which will return another function which we used a lambda
def fun1(num):
    return lambda x: x * num;

res =fun1(2)(5)  #at this position when we called fun1 it returns lambda
print(res)

fun2 = fun1(2) # previously there is no refernce for lambda now we are giving refernce so we can call now lambda

res = fun2(5)
print("With refernce to lambda:",res)