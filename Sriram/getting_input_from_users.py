
#Getting input from users

#Basic prompt
name = input("Enter your name: ")
age = input("Enter your age: ")
height = input("Enter your height: ")
weight = input("Enter your weight: ")
print("Hello " + name + "!")
if age >= "13":
    print("You are allowed to use this")
else:
    print("Sad life mate. You are not old enough for this. ")
if height >= "145":
    print("Wow your a good height")
else:
    print("Lmao you midget. You are so short!")
if weight >= "45":
    print("You are pretty fat, not gonna lie")
elif weight <= "45":
    print("Noice one mate. You are not fat!")
else:
    print("I don't know what to say man!")
