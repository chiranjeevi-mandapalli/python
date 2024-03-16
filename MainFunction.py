# while we execute scripts internally main gets called
# it checks if --name == __main__
# all those contents gets executed
# for example we have two files test.py and module.py
#if we execute module.py the it check internally  if --name == __main__ then the contents in the file gets executed
# if we dont specify the main and if we import module.py in test.py then the contents in both files gets executed and display the output

def add(a,b):
    '''This function add the given two user inouts'''
    return a+b

def main():
    print("hello")
if __name__ == '__main__':
    main()

