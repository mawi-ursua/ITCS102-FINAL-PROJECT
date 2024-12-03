age = eval(input("Please Enter your Age --> "))

if age >= 1 and age <= 7 :
	print("Toddler")

elif age >= 8 and age <= 13 :
	print("Your age is considered as Pre teen")

elif age >= 14 and age <= 18 :
	print("Your age is considered as Teenager")

elif age >= 19 and age <= 31 :
	print("Your age is considered as Early Adulthood")

elif age >= 32 and age <= 45 :
	print("Your age is considered as Mid Adulthood")

elif age >= 46 and age <= 59 :
	print("Your age is considered as Post Adulthood")

elif age >= 60 :
	print("Your age is considered as Senior")
