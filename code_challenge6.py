prelim = eval(input("Enter your Prelim Grade --> "))
midterm = eval(input("Enter your Midterm Grade --> "))
semifinal = eval(input("Enter your Semi-Final Grade --> "))
final = eval(input("Enter your Final Grade --> "))
quiz = eval(input("Enter your Quiz Grade --> "))
project = eval(input("Enter your Project Grade --> "))


if (prelim >= 65 and prelim <= 100) and (midterm >= 65 and midterm <= 100) and (semifinal >= 65 and semifinal <= 100) and (final >= 65 and final <= 100) and (quiz >= 65 and quiz <= 100) and (project >= 65 and project <= 100):
	fg = (prelim * 0.15) + (midterm * 0.15) + (semifinal * 0.15) + (final * 0.25) + (quiz * 0.15) + (project * 0.15)
	print("Your final grade is", fg ,".")
	if fg >= 75:
		print("Congratulations you passed the course")
	else:
		print("Sorry you failed")
else:
	print("Invalid Grades")
