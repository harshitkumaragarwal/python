number=int(input("enter a number"))

if number<0:
    print("the factorial dose not exit")
else:
    fact=1
    for i in range(1,number+1):
        fact=fact*i
        print("the factorial of",number,"is",fact)
    else:
        number==1
        print("the factorial is 1")

        
