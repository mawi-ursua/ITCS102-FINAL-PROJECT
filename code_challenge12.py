for x in range(6, 1, -1):
    for m in range(0, x):
        print(" ", end=" ")
    for j in range(6, x, -1):
        print("*", end=" ")
    for u in range(6, x, -1):
        print("*", end=" ")
    print()

for x in range(3, -1, -1):
    for m in range(4,-1, -1):
        print(" ", end=" ")
    for j in range(2, 0, -1):
        print("*", end=" ")
    for u in range(0, x, -1):
        print("*", end=" ")
    print()