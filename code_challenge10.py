for x in range(6, 1, -1):
    for m in range(0, x):
        print(" ", end=" ")
    for j in range(6, x, -1):
        print("*", end=" ")
    for u in range(6, x, -1):
        print("*", end=" ")
    print()

for x in range(1, 6):
    for m in range(1, x+1):
        print(" ", end=" ")
    for j in range(6, x, -1):
        print("*", end=" ")
    for u in range(6, x, -1):
        print("*", end=" ")
    print()