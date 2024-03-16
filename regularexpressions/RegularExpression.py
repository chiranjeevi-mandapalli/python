# regular expression should contaion raw string
# match is such a function it will check only starting if it is not present in starting then it will not search
# if we want to find the string irrespective of position then use search
import re

text = "Python is best language"
regex = r"Python"
match = re.match(regex, text)
print(text[match.start():match.end()])  # this can aslo be written start,end = match.start(),match.end()

# using search
text = "Python is best language"
regex = r"bests"
match = re.search(regex, text)
if match == None:
    print("Not found")
else:
    print(text[match.start():match.end()])
