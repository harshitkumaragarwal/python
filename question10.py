#take variable as input print it valid python identifier of not

var = input("Enter a variable name: ")

if var.isidentifier():
    print(var, "is a valid Python identifier")
else:
    print(var, "is not a valid Python identifier")
