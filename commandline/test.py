# we can take the inputs before the program starts execution
# python test.py 10 20
# we can pass n number of argumets in th command line
# this command line is stored in list
# python test.py 10 20 do in command line

import sys

print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])

# by default the values passed from command line will be treated as String

a = int(sys.argv[1])
b = int(sys.argv[2])
c = a / b
print(c)
