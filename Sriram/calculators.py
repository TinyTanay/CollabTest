#Building a Basic Calculator
print("This is a Calculator that will add your 2 numbers")
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
answer = float(num1) + float(num2)
print(answer)

#Building an Advanced Calculator
print("This is a Calculator that will do most things but only with 2 numbers")
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
symbol = input("Enter the symbol for what you want to do: ")
if symbol is "+":
    print(float(num1) + float(num2))
elif symbol is "-":
    print(float(num1) - float(num2))
elif symbol is "x":
    print(float(num1) x float(num2))
else:
    print(float(num1) / float(num2))
