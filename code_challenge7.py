isbuy = input("Will you buy a grocery (yes/no) : ")
if isbuy.lower() == "yes":
	nameitem = input("Name of the Item : ")
	priceitem = eval(input("Price of the Item : "))
	age = eval(input("Age : "))
	givenAmount = eval(input("Amount give : "))

	discount = round((priceitem * 0.052), 2)
	discountPrice = round((priceitem - discount), 2)
	tax = round((priceitem * 0.123), 2)
	taxPrice = round((priceitem + tax), 2)
	
	if age >= 60:
		print(f"Hi consumer, you purchased a {nameitem}, with a price of {priceitem}php plus a 5.2% discount ({discount}php) to your total purchase. ")
		print(f"Total of : {round((priceitem - discount), 2)} ")
		print(f"Change : {round((givenAmount - discountPrice), 2)} ")
		print("Thank you for shopping, please come again next time")
	elif age >=18 :
		print(f"Hi consumer, you purchased a {nameitem}, with a price of {priceitem}php plus a 12.3% tax ({tax}php) to your total purchase. ")
		print(f"Total of : {round((priceitem + tax), 2)} ")
		print(f"Change : {round((givenAmount - taxPrice), 2)} ")
		print("Thank you for shopping, please come again next time")
else:
	print("Thank you for dropping by. See you again later.")