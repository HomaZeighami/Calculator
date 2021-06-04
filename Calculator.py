# The user's inputs for the numbers and the operator.
num1 = float(input("Enter your first number: "))
operator = input("Enter operator: ")
num2 = float(input("Enter your second number: "))

str1 = str("Result:")

# If operator is (+ , - , * , /), then print out number 1 (+ , - , * , /) number 2.
if operator == "+":
    print(str1, (num1 + num2))
elif operator == "-":
    print(str1, (num1 - num2))
elif operator == "/":
    print(str1, (num1 / num2))
elif operator == "*":
    print(str1, (num1 * num2))

# If the user didn't put an operator, then print out "Invalid operator".
else:
    print("Invalid operator")
