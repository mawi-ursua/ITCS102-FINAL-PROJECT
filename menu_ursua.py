def act1():
    print("Hello World")

def act2():
            num1 = int(input("Enter a number: "))
            num2 = int(input("Enter another number: "))

            print(num1, "\nFloor Divided to", num2 ,"=", num1 // num2)

def act3():
            fullname = input("Please input your Full name: ")
            age = input("Please input your Age: ")
            birthdate = input("Please input your Birthday: ")
            birthplace = input("Please input your Birthplace: ")
            nationality = input("Please input your Nationality: ")
            gender = input("Please input your Gender: ")
            province = input("Please input your Province: ")
            city = input("Please input your City: ")
            barangay = input("Please input your Barangay: ")
            civilstatus = input("Please input your Civil status: ")
            religion = input("Please input your Religion: ")
            emailaddress = input("Please input your emailaddress: ")
            phonenumber = input("Please input your Phone number: ")
            skills = input("Please input your skills: ")
            talent = input("Please input your talents: ")
            fathersfullname = input("Please input your Father's Full name: ")
            fathersage = input("Please input your Father's age: " )
            fathersoccupation = input("Please input your Father's occupation: ")
            mothersfullname = input("Please input your Mother's Full name: ")
            mothersage = input("Please input your Mother's age:" )
            mothersoccupation = input("Please input your Mother's occupation: ")

            print("\nBiodata"
            "\n\nPersonal Information:"
            "\n\nHi, my name is " + fullname + 
            "\nand I am " + age + " years old."
            "\nMy birthday is on " + birthdate + 
            ",\nand my birthplace is in " + birthplace +
            ".\nI am a " + nationality +
            ",\nand my gender is " + gender + 
            ".\nI live in the province of " + province + ", in the city of " + city + ", at the barangay " + barangay +  
            ".\nMy civil status is " + civilstatus + 
            ".\nMy religion is " + religion +
            ".\nMy skills are " + skills +
            ", and\nMy talents are " + talent +
            ".\nYou can contact me at my email, " + emailaddress + " and my phone number, " + phonenumber +
            ".\n\nParents Information:\n\nMy Father's name is " + fathersfullname + 
            ".\nHe is " + fathersage + "years old.\nHis occupation is " + fathersoccupation + 
            ", and\nMy Mother's name is " + mothersfullname +
            ".\nShe is " + mothersage + " years old.\nHer occupation is " + mothersoccupation + ".")

def act4():
            number1 = eval(input("\n\n\t\t\bEnter A Number: "))
            number2 = eval(input("\t\t\bEnter Another Number: "))

            add = number1 + number2
            sub = number1 - number2
            mul = number1 * number2
            div = number1 / number2
            flr_div = number1 // number2
            exp = number1 ** number2
            mod = number1 % number2


            print("\n\n\t\t\t\tThe sum of",number1,"and",number2,"is",add,
            "\n\t\t\t\tThe difference of",number1,"and",number2,"is",sub,"\n\t\t\t\tThe product of",number1,
            "and",number2,"is",mul,"\n\t\t\t\tThe quotient of",number1,"and",number2,"is",div,
            "\n\t\t\t\tThe floor division of",number1,"and",number2,"is",flr_div,"\n\t\t\t\tThe exponent of",number1,"and",number2,
            "is",exp,"\n\t\t\t\tThe modulus of",number1,"and",number2,"is",mod,"\n\n ")

def act5():
            temp = float(input("Enter Temperature in Farenheit: "))

            cel = (temp - 32) * 5/9

            print(f"The conversion of {temp} degrees Farenheit is {round(cel, 2)} degrees Celcius.")

def act6():
            x = 5
            print(x)

            x += 10
            print(x)

            x += 15
            print(x)

            x+= 10
            print(x)

def act7():
            gold = 0
            min = input("Hi, What is your name: ")

            isgold = input("Is the mineral Gold? [Yes / No]: ").upper().strip()

            if isgold == "YES":
                  gold += 1
                  print(f"Hi {min}, Your total number of Gold is: {gold}")

            elif isgold == "NO":
                  print("Please input a Gold")

            else:
                  print("Wrong Input")

def act8():
            pre = int(input("\n\n\tPrelim Score: "))
            mid = int(input("\n\tMidterm Score: "))
            semi = int(input("\n\tSemi-Final Score: "))
            final = int(input("\n\tFinal Score: "))
            quiz = int(input("\n\tQuiz Score: "))
            proj = int(input("\n\tProject Score: " ))

            fg = (pre * 0.15) + (mid * 0.15) + (semi * 0.15) + (final * 0.15) + (quiz * 0.25) + (proj * 0.15)


            print(f"\n\n\tYour grade is {fg}")

            if pre > 100:
                  print("\n\tError. Wrong input")
            elif fg >= 65:
                  print("\n\tCongratulations! You have passed the course")
            else:
                  print("\n\tUnfortunately You Have Failed")

def act9():
            age = int(input("Enter your Age: "))

            if age > 130:
                  print("Enter your Real Age")
            elif age >= 60 and age <= 130:
                  print("You are a senior")
            elif age >= 46 and age <= 59:
                  print("You are at Post Adulthood")
            elif age >= 32 and age <= 45:
                  print("You are at Mid Adulthood")
            elif age >= 19 and age <= 31:
                  print("You are at an Early Adulthood")
            elif age >= 14 and age <= 18:
                  print("You are a Teenager")
            elif age >= 8 and age <= 13:
                  print("You are at Pre-Teen")
            elif age >= 1 and age <= 7:
                  print("You are a Todler")
            else:
                  print("Enter a your Real Age")

def act10():
            name= input("Enter your name here:  ")
            isStud = input ("Are you currently enrolled in DLL? [Yes or No]:  ").upper().strip()


            if isStud == "YES":
                  yearLev =input("What year are you currently enrolled? \nF- Freshmen \nS-Sophomore"
                              "\nJ-Junior  \nR-Senior: \nPlease enter your answer here: ").upper().strip()
                  
                  if yearLev == "F":
                        print(f"Hello Freshie {name}, and Welcome to DLL") 
                  elif yearLev == "S":
                        print(f"Hello Sophomore {name}, and Welcome to DLL") 
                  elif yearLev == "J":
                        print(f"Hello Junior {name}, and Welcome to DLL, konti na lang") 
                  elif yearLev == "R":
                        print(f"Hello Senior {name}, Welcome to DLL and congrats pwede kanang humimlay")

            elif isStud == "NO":
                  print("Thank you, Next")

            else:
                  print("Wrong Input")

def act11():
            for i in range(1, 11):
                  print("Hello World!")
                  print("Happy Foundation")
                  
                  single = False

                  print(f"{single}, That I'm Single")

def act12():
    print("Enter 10 number \n------------------\n ")

    n1 = 0
    odd = 0
    even = 0 
    for i in range(1, 11):
        n2 = eval(input(f"Enter a number {i}: "))
        n1 += n2
        if n2 % 2 == 0:
            even += n2
        else:
            odd += n2

    print(f"The total of the number you entered is {n1} ")
    print(f"The total of the EVEN number you entered is {even} ")
    print(f"The total of the ODD you entered is {odd} ")

def act13():
            sum = 0 

            for i in range(4, 0, -1):
                  i *= i
                  sum += i


            print(i)
            print(sum)

def act14():
    for x in range(1, 11, -1):
        print(x)

def act15():
        for x in range(0, 11):
            print(x, end=" ")
            for y in range(0, x):
                print("*", end = " ")
            print()  

def act16():
    for x in range(1, 9, 2):
        for y in range(7, x-1, -1):
            print(" ", end=" ")
        for z in range(x, 0, -1):
            print(" * ", end=" ")  
        print()    

    for x in range(1, 9, 2):
        for y in range(x+2):
            print(" ", end=" ")
        for z in range(6, x, -1):
            print(" * ", end=" ")  
        print()  

def act17():
    col = eval(input("Enter number of colums: "))

    for x in range(1, 11):
        for y in range(1, col + 1):
            print(f"{x} x {y} = {x * y}", end = "\t")
        print()    

def act18():
            num = int(input("Enter a number of right triangle: ")) 

            for i in range(1, 6):
                  for r in range(1, num + 1):
                        print(" ", end= " ")
                        for j in range(1, i + 1):
                              print("*", end= " ")
                        for k in range(5, i, -1):
                              print(" ", end= " ") 

                  print()

def act19():
            contin = True
            count = 0

            while contin == True:
                  name = input("Enter a name: ").upper().strip()

                  if name == "STOP":
                        print("The loop has now stopped")
                        print(f"You have entered {count} number of names")
                        break

                  else:
                        count += 1
                        continue

def act20():
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
                        continue

def act21():

            def Hallo(name):
                  print(f"Hello {name}")

            def act2():
                  num1 = int(input("Please enter a number:  "))
                  num2 = int(input("Please enter another number:  "))
                  answer = num1 + num2
                  print(f"The sun of {num1} and {num2} is: {answer}")

            while True:
                  ask = input("Please provide a name: ").upper().strip()
                  if ask =="STOP":
                        Hallo(ask)

def act23():

            def add(num1, num2):
                  """This function adds the first number and second number returnig sum value"""
                  return print(f"The sum of the numbers are: {num1 + num2}")    

            add()

def act24():
            
            from Activity23 import add
            import Activity1

            add(21,21)
            Activity1

def act25():

    def list():

        courses = ["BSIT", "BSA", "BSAIS", "BTVTED", "BSSW", "BSPA", "Delete w/o index", "Delete with index"]

        courses.remove("Delete w/o index")
        courses.pop()
        courses.append("DHRS")
        courses.insert(0, "ABELS")

        print(courses)

def code1():
      print("\t\t\t\t\t\t\t\t\t\t  * \n\t\t\t\t\t\t\t\t\t\t* * * \n\t\t\t\t\t\t\t\t\t      * * * * *\n\t\t\t\t\t\t\t\t\t    * * * * * * *\n\t\t\t\t\t\t\t\t\t      * * * * *\n\t\t\t\t\t\t\t\t\t\t* * * \n\t\t\t\t\t\t\t\t\t\t  *")

def code2():
    name = input( "What is your name?") 
    print("\t\t\t\t\t\t\t\t\t\t  * \n\t\t\t\t\t\t\t\t\t\t* * * \n\t\t\t\t\t\t\t\t\t      * * * * *\n\t\t\t\t\t\t\t\t\t    * Hi, " + name ,"* \n\t\t\t\t\t\t\t\t\t      * * * * *\n\t\t\t\t\t\t\t\t\t\t* * * \n\t\t\t\t\t\t\t\t\t\t  *")

def code4():
    number1 = eval(input("enter a number --> "))
    number2 = eval(input("enter a number --> "))

    answer1 = number1 + number2 
    answer2 = number1 - number2 
    answer3 = number1 * number2 
    answer4 = number1 / number2 
    answer5 = number1 % number2 
    answer6 = number1 ** number2 
    answer7 = number1 // number2 

    print("\nThe sum of", number1 , "and", number2 , "is" , answer1 ,)
    print("The difference of" , number1 , "and" , number2 , "is" , answer2 ,)
    print("The product of" , number1 , "and" , number2 , "is" , answer3 ,)
    print("The quotient of" , number1 , "and" , number2 , "is" , answer4 ,)
    print("The modulo of" , number1 , "and" , number2 , "is" , answer5 ,)
    print("The exponent of" , number1 , "and" , number2 , "is" , answer6 ,)
    print("The floordivision of" , number1 , "and" , number2 , "is" , answer7 ,)

def code5():
    print("FARENHEIT TO CELCIUS CONVERTR PROGRAM")
    print("\n ====================================")
    fahrenheit = eval(input("Enter a temparature in Fahrenheit --> :   "))

    celcius = ((fahrenheit - 32 ) * 5 ) / 9

    print(f"{fahrenheit} degrees Fahrenheit converted to celcius is equal to {celcius} degrees")

def code6():
    try:
        prelim = eval(input("Enter your Prelim Grade --> "))
        midterm = eval(input("Enter your Midterm Grade --> "))
        semifinal = eval(input("Enter your Semi-Final Grade --> "))
        final = eval(input("Enter your Final Grade --> "))
        quiz = eval(input("Enter your Quiz Grade --> "))
        project = eval(input("Enter your Project Grade --> "))
        if (65 <= prelim <= 100) and (65 <= midterm <= 100) and (65 <= semifinal <= 100) and \
           (65 <= final <= 100) and (65 <= quiz <= 100) and (65 <= project <= 100):
            
            fg = (prelim * 0.15) + (midterm * 0.15) + (semifinal * 0.15) + \
                 (final * 0.25) + (quiz * 0.15) + (project * 0.15)
            print(f"Your final grade is {fg:.2f}.")
            
            if fg >= 75:
                print("Congratulations, you passed the course!")
            else:
                print("Sorry, you failed.")
        else:
            print("Invalid Grades: Grades must be between 65 and 100.")

    except:
        print("Invalid Input: Please enter numeric values for grades.")

def code7():
    isbuy = input("Will you buy a grocery (yes/no): ").lower()

    if isbuy == "yes":
        nameitem = input("Name of the Item: ")
        try:
            priceitem = float(input("Price of the Item: "))
            age = int(input("Age: "))
            givenAmount = float(input("Amount given: "))
        except ValueError:
            print("Invalid input! Please enter numeric values for price, age, and amount given.")
            return

        discount = round(priceitem * 0.052, 2)  
        discountPrice = round(priceitem - discount, 2)  
        tax = round(priceitem * 0.123, 2)  
        taxPrice = round(priceitem + tax, 2) 

        if age >= 60:  
            print(f"\nHi consumer, you purchased a '{nameitem}', with a price of {priceitem} PHP.")
            print(f"A 5.2% discount ({discount} PHP) was applied to your total purchase.")
            print(f"Total: {discountPrice} PHP")
            print(f"Change: {round(givenAmount - discountPrice, 2)} PHP")
        elif age >= 18: 
            print(f"\nHi consumer, you purchased a '{nameitem}', with a price of {priceitem} PHP.")
            print(f"A 12.3% tax ({tax} PHP) was added to your total purchase.")
            print(f"Total: {taxPrice} PHP")
            print(f"Change: {round(givenAmount - taxPrice, 2)} PHP")
        else: 
            print(f"\nHi consumer, you purchased a '{nameitem}', with a price of {priceitem} PHP.")
            print(f"Minors are exempt from tax or discounts. Total: {priceitem} PHP")
            print(f"Change: {round(givenAmount - priceitem, 2)} PHP")

        print("\nThank you for shopping, please come again next time!")
    else:
        print("\nThank you for dropping by. See you again later!")

def code8():
    total = 0  

    for x in range(1, 11):
        number = eval(input(f"Enter number {x} : "))  
    total += number  

    print(f"The summation of all provided numbers is: {total}")

def code9():
    for x in range(10):
        for space in range(x):
            print(" ", end= " ")
        for y in range(10-x):
            print("*", end= " ")
        print()  

def code10():
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

def code11():
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

def code12():
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

def code13():
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

def code14():
    tuloy = True
    total = 0
    while tuloy == True:
        num = input("Please enter a number --> ")

        if num == "0":
            print("Loop has terminated")
            print(f"The sum of all the numbers given is {total}")
            break
            tuloy = False
        else:
            num=eval(num)
            total += num
            continue
def code15():
    tuloy = True
    no = 0
    while tuloy == True:
        ask = input("Do you wish to create a new triangle (yes or no) --> ")

        if ask.lower() == "no":
            print("Loop has terminated")
            break
        elif ask.lower() == "yes":
            no += 1
            for x in range(1, 6):
                for r in range(1,no + 1):
                    for y in range(1,x + 1):
                        print("^", end=" ")
                    for z in range(6, x, -1):
                        print(" ", end=" ")
                print()
            continue
        else:
            print("Invalid number, please only answer 'yes' or 'no'")
            continue     

def code16():
    
    def breakdown_filipino_denomination(amount):
        libo = amount // 1000
        libo_sukli = amount % 1000

        five_h = libo_sukli // 500
        five_sukli = libo_sukli % 500

        two_h = five_sukli // 200
        two_sukli = five_sukli % 200

        one_h = two_sukli // 100
        one_sukli = two_sukli % 100

        fifthy = one_sukli // 50
        fifthy_sukli = one_sukli % 50

        twenty = fifthy_sukli // 20
        twenty_sukli = fifthy_sukli % 20

        ten = twenty_sukli // 10
        ten_sukli = twenty_sukli % 10

        five = ten_sukli // 5
        five_sukli = ten_sukli % 5

        one = five_sukli // 1

        return {
            1000: libo,
            500: five_h,
            200: two_h,
            100: one_h,
            50: fifthy,
            20: twenty,
            10: ten,
            5: five,
            1: one, }

    def create_account(accounts, name, initial_deposit):
        accounts[name] = {"balance": initial_deposit}
        print(f"Account created for {name} with balance ₱{initial_deposit}")

    def deposit(accounts, name, amount):
        accounts[name]["balance"] += amount
        print(f"\nDeposited: ₱{amount}")
        print(f"New Balance: ₱{accounts[name]['balance']}")

    def withdraw(accounts, name, amount):
        if amount > accounts[name]["balance"]:
            print("\nInsufficient funds.")
        else:
            accounts[name]["balance"] -= amount
            print(f"\nWithdrew: ₱{amount}")
            print(f"New Balance: ₱{accounts[name]['balance']}")

    def display_balance(accounts, name):
        balance = accounts[name]["balance"]
        print(f"\nCurrent Balance: ₱{balance}")
        print("Denomination Breakdown:")
        breakdown = breakdown_filipino_denomination(balance)
        for denom, count in breakdown.items():
            print(f"₱{denom}: {count}")

    def main():
        accounts = {}
        while True:
            print("\nAccount Banking System")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Check Balance and Denomination Breakdown")
            print("5. Terminate Program")
            ask = input("Choose a Program: ")

            if ask == "1":
                name = input("Enter your name: ")
                initial_deposit = eval(input("Enter initial deposit: "))
                if name in accounts:
                    print("Account already exists.")
                else:
                    create_account(accounts, name, initial_deposit)

            elif ask == "2":
                name = input("Enter your name: ")
                if name in accounts:
                    amount = eval(input("Enter deposit amount: "))
                    deposit(accounts, name, amount)
                else:
                    print("Account not found.")

            elif ask == "3":
                name = input("Enter your name: ")
                if name in accounts:
                    amount = eval(input("Enter withdrawal amount: "))
                    withdraw(accounts, name, amount)
                else:
                    print("Account not found.")

            elif ask == "4":
                name = input("Enter your name: ")
                if name in accounts:
                    display_balance(accounts, name)
                else:
                    print("Account not found.")

            elif ask == "5":
                print("Program terminated.")
                break
            else:
                print("Invalid choice. Please try again.")

    if __name__ == "__main__":
        main()

def act22():
    while True:
        print("\n\tSELECT FROM THE FOLLOWING PROGRAMS BELOW \n\t"
            "\n\tActivity 1 - [1]", "\tActivity 9 - [9]", "\tActivity 17 - [17]"
            "\n\tActivity 2 - [2]", "\tActivity 10 - [10]", "\tActivity 18 - [18]"
            "\n\tActivity 3 - [3]", "\tActivity 11 - [11]", "\tActivity 20 - [20]"
            "\n\tActivity 4 - [4]", "\tActivity 12 - [12]", "\tActivity 21 - [21]"
            "\n\tActivity 5 - [5]", "\tActivity 13 - [13]", "\tActivity 23 - [23]"
            "\n\tActivity 6 - [6]", "\tActivity 14 - [14]", "\tActivity 24 - [24]"
            "\n\tActivity 7 - [7]", "\tActivity 15 - [15]", "\tActivity 25 - [25]"
            "\n\tActivity 8 - [8]", "\tActivity 16 - [16]", "\tExit - [0]")

        
        try:
            choice = int(input("Select a Program: "))
            
            if choice == 1:
                act1()
            elif choice == 2:
                act2()  
            elif choice == 3:
                act3()  
            elif choice == 4:
                act4()
            elif choice == 5:
                act5()
            elif choice == 6:
                act6()
            elif choice == 7:
                act7()
            elif choice == 8:
                act8()
            elif choice == 9:
                act9()
            elif choice == 10:
                act10()
            elif choice == 11:
                act11()
            elif choice == 12:
                act12()
            elif choice == 13:
                act13()   
            elif choice == 14:
                act14()   
            elif choice == 15:
                act15()   
            elif choice == 16:
                act16()   
            elif choice == 17:
                act17()   
            elif choice == 18:
                act18()   
            elif choice == 19:
                act19()   
            elif choice == 20:
                act20() 
            elif choice == 21:
                act21()   
            elif choice == 22:
                act22()  
            elif choice == 23:
                act23()   
            elif choice == 24:
                act24()   
            elif choice == 25:
                act25()                                     
            elif choice == 0:
                print("Exiting program. Thank you!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def code_challenge():
    while True:
        print("\n\t\tSELECT FROM THE FOLLOWING CODE CHALLENGES BELOW: \n\t"
            "\n\t\t\tCode Challenge 1 - [1]", "\t\t\tCode Challenge 5  - [5]",  "\t\tCode Challenge 9  -  [9]",    "\t\tCode Challenge 13 - [13]" 
            "\n\t\t\tCode Challenge 2 - [2]", "\t\t\tCode Challenge 6  - [6]",  "\t\tCode Challenge 10 - [10]",    "\t\tCode Challenge 14 - [14]" 
            "\n\t\t\tCode Challenge 3 - [3]", "\t\t\tCode Challenge 7  - [7]",  "\t\tCode Challenge 11 - [11]",    "\t\tCode Challenge 15 - [15]" 
            "\n\t\t\tCode Challenge 4 - [4]", "\t\t\tCode Challenge 8  - [8]",  "\t\tCode Challenge 12 - [12]",    "\t\tCode Challenge 16 - [16]" 
            
            "\n\t\t\t\t\t\t\t\t\t EXIT  - [0]")

        
        try:
            choice = int(input("Select a Program: "))
            
            if choice == 1:
                code1()
            elif choice == 2:
                code2()  
            elif choice == 3:
                act3()  
            elif choice == 4:
                code4()
            elif choice == 5:
                code5()
            elif choice == 6:
                code6()
            elif choice == 7:
                code7()
            elif choice == 8:
                code8()
            elif choice == 9:
                code9()
            elif choice == 10:
                code10()
            elif choice == 11:
                code11()
            elif choice == 12:
                code12()
            elif choice == 13:
                code13()   
            elif choice == 14:
                code14()   
            elif choice == 15:
                code15()        
            elif choice == 16:
                code16()            
            elif choice == 0:
                print("Back to Main Menu")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def print_statements():
    while True:
        print("\n\t\tSELECT FROM THE FOLLOWING PROGRAMS BELOW \n\t"
            "\n\t\t\tActivity 1 - [1]"
            "\n\t\t\tActivity 2 - [2]"
            "\n\t\t\tActivity 3 - [3]"
            "\n\t\t\tRETURN     - [0]")
            
        statements = int(input("Select a Program: "))
        if statements == 1:
                act1()
        elif statements == 2:
                act2()
        elif statements == 3:
                act3()
        elif statements == 0:
                main_menu()    
        else:
                print("Invalid choice. Please try again.")

def variables():
    while True:
        print("\n\t\tSELECT FROM THE FOLLOWING PROGRAMS BELOW \n\t"
            "\n\t\t\tActivity 2 - [1]"
            "\n\t\t\tActivity 3 - [2]"
            "\n\t\t\tRETURN     - [0]")
        varia = int(input("Select a Program: "))
        if varia == 1:
                act2()
        elif varia == 2:
                act3()
        elif varia == 0:
                main_menu()
        else:
                print("Invalid choice. Please try again.")

def operators():
    while True:
        print("\n\t\tSELECT FROM THE FOLLOWING PROGRAMS BELOW \n\t"
            "\n\t\t\tActivity 2 - [1]"
            "\n\t\t\tActivity 4 - [2]"
            "\n\t\t\tActivity 5 - [3]"
            "\n\t\t\tActivity 6 - [4]"
            "\n\t\t\tRETURN     - [0]")

        oper = int(input("Select a Program: "))
        if oper == 1:
                act2()
        elif oper == 2:
                act4()
        elif oper == 3:
                act5()    
        elif oper == 4:
                act6()
        elif oper == 0:
                main_menu()
        else:
                print("Invalid choice. Please try again.")

def conditional():
    while True:
        print("\n\t\tSELECT FROM THE FOLLOWING PROGRAMS BELOW \n\t"
            "\n\t\t\tActivity 7  - [1]"
            "\n\t\t\tActivity 8  - [2]"
            "\n\t\t\tActivity 9  - [3]"
            "\n\t\t\tActivity 10 - [4]"
            "\n\t\t\tRETURN      - [0]")

        condi = int(input("Select a Program: "))
        if condi == 1:
                act7()
        elif condi == 2:
                act8()
        elif condi == 3:
                act9()    
        elif condi == 4:
                act10()
        elif condi == 0:
                main_menu() 
        else:
                print("Invalid choice. Please try again.")

def loops():
    while True:
        print("\n\t\tSELECT FROM THE FOLLOWING PROGRAMS BELOW \n\t"
            "\n\t\t\tActivity 11 - [1]"
            "\n\t\t\tActivity 12 - [2]"
            "\n\t\t\tActivity 13 - [3]"
            "\n\t\t\tActivity 14 - [4]"
            "\n\t\t\tActivity 15 - [5]"
            "\n\t\t\tActivity 16 - [6]"
            "\n\t\t\tActivity 17 - [7]"
            "\n\t\t\tActivity 18 - [8]"
            "\n\t\t\tActivity 19 - [9]"
            "\n\t\t\tActivity 20 - [10]"
            "\n\t\t\tRETURN      - [0]")


        loop = int(input("Select a Program: "))
        if loop == 1:
            act11()
        elif loop == 2:
            act12()
        elif loop == 3:
            act13()          
        elif loop == 4:
            act14()
        elif loop == 5:
            act15()
        elif loop == 6:
            act16()  
        elif loop == 7:
            act17()
        elif loop == 8:
            act18()
        elif loop == 9:
            act19()  
        elif loop == 10:
            act20()
        elif loop == 0:
            main_menu()
        else:
                print("Invalid choice. Please try again.")

def lists():
    while True:
        print("\n\t\tSELECT FROM THE FOLLOWING PROGRAMS BELOW \n\t"
            "\n\t\t\tActivity 25 - [1]"
            "\n\t\t\tRETURN      - [0]")


        list = int(input("Select a Program: "))
        if list == 1:
            act25()
        elif list == 0:
            main_menu()
        else:
                print("Invalid choice. Please try again.")

def functions():
    while True:
        print("\n\t\tSELECT FROM THE FOLLOWING PROGRAMS BELOW \n\t"
            "\n\t\t\tActivity 21 - [1]"
            "\n\t\t\tActivity 23 - [2]"
            "\n\t\t\tActivity 24 - [3]"
            "\n\t\t\tRETURN      - [0]")

        funct = int(input("Select a Program: "))
        if funct == 1:
            act21()
        elif funct == 2:
            act23()
        elif funct == 3:
            act24()
        elif funct == 0:
            main_menu()
        else:
                print("Invalid choice. Please try again.")
          
    
def main_menu():
    while True:
        print("\n\t\t\t\t\t\t\t\t\t\t\tMAIN MENU:")
        print("\t\t\t\t\t\t\t\t[1] Print Statements")
        print("\t\t\t\t\t\t\t\t[2] Variables")
        print("\t\t\t\t\t\t\t\t[3] Operators")
        print("\t\t\t\t\t\t\t\t[4] Conditionals")
        print("\t\t\t\t\t\t\t\t[5] Loops")
        print("\t\t\t\t\t\t\t\t[6] Lists")
        print("\t\t\t\t\t\t\t\t[7] Function")
        print("\t\t\t\t\t\t\t\t[8] All Activities")
        print("\t\t\t\t\t\t\t\t[9] All Code Challenges")
        print("\t\t\t\t\t\t\t\t[0] Exit")
        
        try:
            menu_choice = int(input("Select a Topic: "))   
            if menu_choice == 1:
                print_statements()
            elif menu_choice == 2:
                variables()
            elif menu_choice == 3:
                operators()
            elif menu_choice == 4:
                conditional()
            elif menu_choice == 5:
                loops()
            elif menu_choice == 6:
                lists()
            elif menu_choice == 7:
                functions()
            elif menu_choice == 8:
                act22()
            elif menu_choice == 9:
                code_challenge()
            elif menu_choice == 0:
                print("Exiting main menu.")
                break
            else:  
                print("Topic not implemented yet.")
        except ValueError:
            print("Invalid input. Please enter a number.")

main_menu()
