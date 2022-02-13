#Lists are basically like variables, but unlike them, it can store multiple pieces of data.

sports = ["cricket", "soccer", "basketball"]

#Each of those has an index.
#Cricket being 0, Soccer being 1 and Basketball being 2
#If you want to print a specific one, you can do this

print(sports[2])

#Which would print Basketball

#You can also use negative numbers, for example like this.

print(sports[-3])

#Which would print Cricket
#REMEMBER THAT FROM THE FRONT IT STARTS ON ZERO BUT FROM THE BACK IT STARTS AT -1
#You can also grab certain elements from after a certain time like so

print(sports[1:])

#Which would print everything after and including Soccer at position 1
#Here is another list to demonstrate the next thing

games = ["minecraft", "brawl stars", "roblox", "clash royale", "venge"]

print(games[1:4])

#Which would print everything after 1 up to but not including 4
#You can also modify values inside the list like so
games[0] = "crossy road"

#Which will now change minecraft to crossy road and then we can print that

print(games[0])
