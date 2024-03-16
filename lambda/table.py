def fun1(num):
    return lambda x: x * num;
n= int(input("Enter a number\n"))
math_table =fun1(n)
for i in range(1,11):
    print(n,"x",i,"=",math_table(i))