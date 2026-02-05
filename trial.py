n = 5

for i in range(n):
    # left numbers
    for j in range(1, n - i + 1):
        print(j, end="")

    # stars with spaces
    for j in range(i):
        print(" *", end="")

    # space before right numbers if stars exist
    if i > 0:
        print(" ", end="")

    # right numbers
    for j in range(n - i, 0, -1):
        print(j, end="")

    print()
