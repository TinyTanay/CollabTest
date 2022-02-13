lucky_numbers = [4, 6, 12, 34, 63, 3]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

#We can use the extend function to add the lucky_numbers list to the end of the friends list by doing this

friends.extend(lucky_numbers)
print(friends)

#We can also add things to the list using the append function like so

friends.append("Creed")
print(friends)

#We can also choose the position in which we put a new item of the list like so

friends.insert(1, "Lucy")
print(friends)

#Which adds the name Lucy in position 1 which is after Kevin.
#Removing is another thing we can do like so

friends.remove("Kevin")
print(friends)

#Which removes Kevin from the list
#You can also just remove the whole list using this function.

friends.clear()
print(friends)

#Which has now emptied the list
#We can also use the 'Pop' function to remove a random element from the list like so

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.pop()
print(friends)

#I have reset the list and now it will take out on of the items inside the list
#We can also see if an item is in the list and where it is like so

print(friends.index("Kevin"))

#Which will return 0 the postition of Kevin
#However if I print

#print(friends.index("Mike"))

#It will give an error code and say Mike is not in the list because he is not
#We can also count how many times something occurs in a list like so

fruits = ["apple", "apple", "banana", "orange"]
print(fruits.count("apple"))

#This counts how many apples there are in fruits
#We can also sort into alphabetical or numerical order like so

fruits.sort()
print(fruits)

#Which will print fruits in alphabetical order
#Same with the lucky_numbers

lucky_numbers.sort()
print(lucky_numbers)

#Which will print them from smallest to biggest
#We can also reverse a list like so

fruits.reverse()
print(fruits)

#Which will print fruits in backwards order
#Finally, we can copy a list like so

fruits_2 = fruits.copy()
print(fruits_2)

#Which will print a copy of fruits
