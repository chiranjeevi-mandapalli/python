lst = ["python", "Java", "Ruby"]
# for loop using + this makes inefficient in memeory aspect as it creates a brand new object everytime
s = ""
for i in lst:
    s += i
print(s)
# join method creates the refernce for all the String present in the list,
# this is an efficient method compared to concatination(+)
s1 = "".join(lst)
print(s1)
