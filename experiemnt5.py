n = int(input("Enter number of values: "))

count = [0, 0, 0, 0]

print("Enter the values (0 to 3):")
for i in range(n):
    x = int(input())
    if 0 <= x <= 3:
        count[x] += 1
    else:
        print("Invalid value ignored")

print("Occurrences:")
for i in range(4):
    print(i, "occurs", count[i], "times")
