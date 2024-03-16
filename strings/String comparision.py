s1 = "python"
s2 = "PYTHON"


def compare(s1, s2):
    if s1 == s2:
        print("values are same")
    else:
        print("values are not same")


def check_refernce(s1, s2):
    if id(s1) == id(s2):
        print("references are same")
    else:
        print("references are not same")


def equal_ignore_case(s1, s2):
    if s1.lower() == s2.lower():
        print("values are same")
    else:
        print("values are not same")


compare(s1, s2)
check_refernce(s1, s2)
equal_ignore_case(s1, s2)
