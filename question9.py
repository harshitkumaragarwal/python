number1=int(input("enter a number"))
number2=int(input("enter a number"))

sum=number1+number2
minus=number1-number2
multiply=number1*number2

if sum%2==0:
    print("the sum is even")
else:
    print("the sum is odd")

    if minus%2==0:
        print("the minus is even")
    else:
        print("the minus is odd")


print("the sum of two number is ",sum)
print("the minus of two number is ",minus)
print("the multiply of two number is ",multiply)

