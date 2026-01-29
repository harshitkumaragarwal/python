number1=float(input("enter a number"))
number2=float(input("enter a number"))
number3=float(input("enter a number"))
number4=float(input("enter a number"))
number5=float(input("enter a number"))
percentage=((number1)+(number2)+(number3)+(number4)+(number5))/5
print("the percentage is ",percentage)

cgpa=percentage//10

if cgpa >= 0 and cgpa <= 3.4:
    print("your grade is F and poor performance")
elif cgpa >= 3.5 and cgpa <= 4.4:
    print("your grade is D and below average performance")
elif cgpa >= 4.5 and cgpa <= 5.4:
    print("your grade is C and average performance")
elif cgpa >= 5.5 and cgpa <= 6.4:
    print("your grade is B and good performance")
elif cgpa >= 6.5 and cgpa <= 7.4:
    print("your grade is A and very good performance")
elif cgpa >= 7.5 and cgpa <= 8.4:
    print("your grade is A+ and excellent performance")
elif cgpa >= 8.5 and cgpa <= 10:
    print("your grade is O and outstanding performance")


