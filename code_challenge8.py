total = 0  

for x in range(1, 11):
    number = eval(input(f"Enter number {x} : "))  
    total += number  

print(f"The summation of all provided numbers is: {total}")