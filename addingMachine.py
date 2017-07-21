

def add(x,y):
	return x + y

def main():
	print("Please enter the first number:" )

	num1 = int(input(">>"))


	print("Please enter the second numner:")

	num2 =int(input(">>"))

	print(num1, " + ", num2, " = ", add(num1,num2))

	userInput = input("Again? y/n\n>>")
	if userInput == "y" or userInput == "Y":
		main()
	else:
		exit()


main()
