for x in range(10):
    for space in range(x):
        print(" ", end= " ")
    for y in range(10-x):
        print("*", end= " ")
    print()  