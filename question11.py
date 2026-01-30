#Write a program to take marks as input from the user and display the result based on the following conditions:
#Distinction: Marks ≥ 75
#First Class: Marks ≥ 60
#Pass: Marks ≥ 40
#Fail: Marks < 40

marks=float(input("enter a marks"))

if marks >=75:
    print("distinction")
elif marks >=60:
    print("first class")
elif marks >=40:
    print("pass")
else:
    print("fail")
    