# //count all the characters
# islower(), isupper(), isnumeric(),
# ex: PyThOn@123
s = "PyThOn@123"
low_count, up_count, sp_count, num_count = 0, 0, 0, 0
for i in s:
    if i.islower():
        low_count += 1
    elif i.isupper():
        up_count += 1
    elif i.isnumeric():
        num_count += 1
    else:
        sp_count += 1

print("LowerCase:", low_count)
print("UpperCase:", up_count)
print("Numbers:", num_count)
print("SpecialCharacters:", sp_count)
