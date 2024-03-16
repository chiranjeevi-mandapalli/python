def pizza(toppings):
    print(toppings)

# there are some cases where we like pizza they want extra suppliments along with it then we can use * so that
# it collects all arguments passed
def pizza1(*toppings):
    print(toppings)
    print(type(toppings))

# after variable length argument if u want to pass any other value then we should pass like key value
def pizza2(*toppings,crust):
    print(toppings)
    print(crust)

pizza2("pizza","onions","cheese",crust = "thin")


