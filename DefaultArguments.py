def power_of(a,b): # b=0 will be used as default argument when no value is specified for b
    c = a**b
    print("Power:",c)

def power_of_1(a,b):
    print(a,b)

# b=0 will be used as default argument when no value is specified for b
# after a default argument we cannot use a non default argument
# we can default argument after default argument
def power_of_2(a,b=0):
    print(a,b)

def power_of_3(a,b=0,c=0):
    print(a,b,c)

power_of(2,5)
power_of_1(2,5)
power_of_2(2,5)
power_of_3(2,5)
