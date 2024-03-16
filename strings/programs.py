# print all the substrings of length 3 for a given String
#        python
#       012345
def print_substrings(name):
    length = 3
    for i in range(0, (len(name) - length) + 1):
        print(name[i:i + 3])


# print all the character except the first and last character
def middle_characters(name):
    print("middle character:", name[1:len(name) - 1])


# print all the charecter except the first and last character in reverse order
def middle_characters_reverse(name):
    print("reverse_middle_character:", name[len(name) - 2:0:-1])


# write a program to reverse a string
def reverse_String(name):
    print("reverse:", name[::-1])


# check given String is plaindrome or not
def palindrome(s1):
    if s1 == s1[::-1]:
        print(s1, "is a palindrome")
    else:
        print(s1, "is not a palindrome")


# reverse the last half ex : python --> pytnoh
def reverse_last_half(name):
    first_half = name[0:len(name) // 2]
    last_half = name[len(name) - 1:(len(name) // 2) - 1:-1]
    print("reversed_last_half:", first_half + last_half)


# floor division is represented by //

# convert smaller case to capitalcase there is  built in function ord(letter) gives values ineteger to character chr(value)
# to convert small case to capital case subtract 32 whci gives ascii and to convert to character use chr

# samll letters values are from 97 and end with 122 and capital case starts from 65
def convert_to_capitalcase(name):
    s = ""
    for i in name:
        if ord(i) >= 97 and ord(i) <= 122:
            s += chr(ord(i) - 32)
        else:
            s += i
    print("capital_case:",s)

def to_upper_case(name):
    print("Built in uppercase",name.upper())

def to_lower_case(name):
    print("Built in lowercase",name.lower())

name = input("Enter the String\n")
print_substrings(name)
middle_characters(name)
middle_characters_reverse(name)
reverse_String(name)
palindrome(name)
reverse_last_half(name)
convert_to_capitalcase(name)
to_upper_case(name)
to_lower_case(name)
