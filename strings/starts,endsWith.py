lst = ["https://localhost:8089.com", "www://google.com", "https://safari.com", "https://java.doc.org"]
lst1 = ["https://localhost:8089.com", "www://google.com", "https://safari.com/", "https://java.doc.org"]

# using built in functions
for i in lst:
    if i.startswith("https"):
        print("Starts:", i)
for i in lst:
    if i.endswith("com"):
        print("Ends:", i)
print("-------------------------------------------------------------------------")
# if we want to pass multiple values to check then we shouls pass in tuple
for i in lst1:
    if i.startswith(("https","http")):
        print("Starts:", i)
for i in lst1:
    if i.endswith(("com","com/")):
        print("Ends:", i)
