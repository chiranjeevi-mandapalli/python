from _cffi_backend import string

if __name__ == '__main__':
    n = 5
    s = ""
    for i in range(1, n):
        s += string(i)

    print(s)
