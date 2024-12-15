<<<<<<< HEAD
isContinue = True
no = 0

while isContinue == True:
    ask = input("Would you like to add another triangle [Yes / No]: ").strip().upper()

    if ask == "no":
        print("PROGRAM TERMINATED")
        break
        isContinue = False

    else:
        no += 1
        for x in range(1,5):
            for r in range(1,no + 1):
                for y in range(1,x + 1):
                    print(" ", end= " ")
                              
                    for z in range(1, x, -1):
                        print("*", end= " ")
                    print()    
=======
isContinue = True
no = 0

while isContinue == True:
    ask = input("Would you like to add another triangle [Yes / No]: ").strip().upper()

    if ask == "no":
        print("PROGRAM TERMINATED")
        break
        isContinue = False

    else:
        no += 1
        for x in range(1,5):
            for r in range(1,no + 1):
                for y in range(1,x + 1):
                    print(" ", end= " ")
                              
                    for z in range(1, x, -1):
                        print("*", end= " ")
                    print()    
>>>>>>> d494c08166ff08200a3bbf605b8f7e6992f329e8
                continue