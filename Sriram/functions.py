#Here is a simple function:

def say_hi():
    print("Hello User")

#Always remember to put the colon after defining or creating a function
#If I left it like this nothing would happen. To call it back however, I can do so

print("Top")
say_hi()
print("Bottom")

#If you want you can add code in between the function and when you call it back like so

#You can also add code after the function is called back
#The above will print, Top, the function which is hello user and then bottom
def say_hello(name, age):
    print("Hello " + name + ", you are " + age)

say_hello("Sriram", "14")
say_hello("Sairam", "12")

#This will print hello sriram you are 14 and hello sairam you are 12
