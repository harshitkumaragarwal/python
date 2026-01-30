#Write a program to create a list and an integer, and pass both to a function.
#Inside the function:
#Modify the list
#Attempt to modify the integer
#Finally, display the values to observe the changes.

def modify_values(my_list, my_int):
    my_list.append(100)
    my_list[0] = 999

    my_int = my_int + 10

    print("Inside function:")
    print("List:", my_list)
    print("Integer:", my_int)


lst = [1, 2, 3]
num = 10

print("Before function call:")
print("List:", lst)
print("Integer:", num)

modify_values(lst, num)

print("\nAfter function call:")
print("List:", lst)
print("Integer:", num)

