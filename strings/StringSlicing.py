# genaral syntax for slicing
# string(firstindex: lastindex+1: step) by default step value is 1 we can change step value aslo

s= "Guido Van Rossum" #for strings also indexing is available
#   123456789101112131415
for i in s:
    print(i)

# slicing
print(s[::]) #here it takes default values

print(s[0:16]) # this is similar to print(s[0:15:1])

print(s[0:16:2]) # to print alternate values

print(s[-1:-16:-1]) #to print string in reverse order

print(s[-1:-16:-2]) # to print alternate values