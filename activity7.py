gold = 0
miner = input("Hi, What is your name : ")

isGold = input("Is the mineral Gold? ") #yes

if isGold.lower() == "yes" :
	gold += 1
	print(f"Hi {miner}, Your total number of gold is {gold}")
else : 
	print(f"Hi {miner}, Your total number of gold is {gold}")
