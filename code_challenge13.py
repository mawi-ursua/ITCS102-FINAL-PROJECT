for x in range(1,6):
    for m in range(6,x,-1):
        print(" ", end=" ")
    for j in range(x, 1, -1):
        print(j, end=" ")
    for u in range(1, x+1):
        print(u, end=" ")
    print()

for x in range(4, 0, -1):
    for m in range(6, x, -1):
        print(" ", end=" ")
    for j in range(x, 1, -1):
        print(j, end=" ")
    for u in range(1, x + 1):
        print(u, end=" ")
    print()