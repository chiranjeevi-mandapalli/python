list = [24,25,26,27]
print(list)
print(list[0])
print(list[-4])
print(type(list))

list1 = [25,28.8,29.5,50,60]
print(list1)
print(list1[2])
print(list[-3])
print(type(list1))

list2 = [25,36,45.5,"SAM","SUNDAR"]
print(list2)
print(list2[3])
print(list2[-2])
print(type(list2))

# list should be specified in square brackets
# we can accss elements also and there is negative indexing available
# positive indexing 0 1 2 3
# negative indexing -4 -3 -2 -1
# we can add and remove elements
list2.append(50)
print(list2)
list2.remove(50)
print(list2)

