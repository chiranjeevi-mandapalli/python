# we have to make vowels as capitals and remove digits
# maketrans()--> gives us dict where we specify our requirement in that table where all ascii values present
# translate()
s = "page not found 404 error"
table = s.maketrans("aeiou", "AEIOU", "0123456789")
s_translate = s.translate(table)
print(s_translate)
