dic = {
    "sam":"english",
    "sundar":"physics",
    "chinchan":"science"
}
print(dic)
print(type(dic))

dic["super"] = "hrithik"
print(dic)

dic.pop("super")
print(dic)

print(dic.values())
# we can access using key
print(dic.get("sam"))



# dictionary is a key value pair and we can add and remove elements
# we cannot access elemets using indexing
