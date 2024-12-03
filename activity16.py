for x in range(1,16):
    for z in range(1, x+1):
        print(" ", end= " ")
    for y in range( 16, x, -1):
        print("*", end=" ")
    print()
