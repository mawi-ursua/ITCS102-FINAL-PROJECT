triangle = eval(input("Please enter a number of triangle --->"))

for x in range(1,5):
    for r in range(1,triangle + 1):
        for y in range(1,x + 1):
            print("*", end=" ")
        for z in range(5,x,-1):
            print(" ", end=" ")
        print(end=" ")
    print()