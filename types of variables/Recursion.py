def fatcorial(n):
    if n==1:
        return 1
    else:
        return n*fatcorial(n-1)

n = int(input("Enter a number\n"))
print(fatcorial(n))