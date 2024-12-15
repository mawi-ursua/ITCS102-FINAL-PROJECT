for x in range(1, 5):
    for m in range (6, x, -1):
       print(" ", end=" ")
    for j in range (1, x+1):
        print("*", end=" ")
    for u in range (2, x+1):
        print("*", end=" ")
    print()

for x in range(1, 4):
    for m in range (1, x+3):
       print(" ", end=" ")
    for j in range (4,x,-1):
        print("*", end=" ")
    for u in range (3, x, -1):
        print("*", end=" ")
    print()