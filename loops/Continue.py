# check if given complete list is even
n = int(input("enter number \n"))
even_sum,odd_sum = 0,0

for i in range(1,n+1):
    if  i % 2 == 0:
        even_sum += i
        continue
    else:
        odd_sum += i

print(even_sum)
print(odd_sum)



