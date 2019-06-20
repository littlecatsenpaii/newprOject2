print("This program is a calculator, you can make simple operations with two numbers")

operation = input("Which operation do you want to do? (Multiplication, Division, Add or Subtraction): ")
number_one = int(input("Tell me a number: "))
number_two = int(input("Tell me other number: "))
result = 0

if operation == "Multiplication":
    result = number_one * number_two
elif operation == "Division":
    result = number_one / number_two
elif operation == "Add":
    result = number_one + number_two
elif operation == "Subtraction":
    operation = number_one - number_two
print("Your result is {}".format(result))
print("Bye~ bye~")