def my_name():
    return("My name is Sriram")

name = "Sriram"

print(f'My name is {name}')

#This is the place where I will do my Python practise


#Drawing Shapes

print("   /|")
print("  / |")
print(" /  |")
print("/___|")

#Variables & Data Types

character_name = "Sriram"
character_age = "13"
print("There once was a boy named " + character_name + ". ")
print("He was " + character_age + " years old. ")
character_name = "Tanay"
print("He liked the name " + character_name + ". ")
print("And he was fine with being " + character_age + " years old. ")

#Working With Strings

print("Dog")
print("Cat")
print("Giraffe")
#instead what you could do is:
print("Dog\nCat\nGiraffe")
phrase = "Dog, Cat & Giraffe"
print(phrase + " are all cool animals")
#Good things to do with functions that are useful
print(phrase)
#To make into upper case, simply
print(phrase.upper())
#To make into lower case, simply
print(phrase.lower())
#To check if it is upper case, simply
print(phrase.isupper())
#To checck if it is lower case, simply
print(phrase.islower())
#Which will both return True or False values
#To check if this works
print(phrase.upper().isupper())
#Which will return True and
print(phrase.lower().islower())
#Which will return False
#To check the length of a Strings
print(len(phrase))
#Which will return the length of my Variable
#You can also return specific letters of the Strings like this:
print(phrase[0])
#Which will return the first letter. PYTHON INDEX STARTS ON 0 FOR Strings
#Similarly, you can use the index function to return how many of a letter there is in a Strings
pritn(phrase.index(a))
#Which would return how many a's are in the Strings
#You can also replace words like so:
print(phrase.replace("Dog", "Donkey"))
#Which would change the strings
