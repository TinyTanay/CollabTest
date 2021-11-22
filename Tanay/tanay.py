class Pet():
    def __init__(self, age, name):
        self.age = age
        self.name = name


class Cat(Pet):
    def __init__(self, age, name, colour, breed):
        super().__init__(age, name)
        self.colour = colour
        self.breed = breed

    @staticmethod
    def speak():
        print("MEOW")

    @classmethod
    def show():
        print(f"I am a {self.breed} and {self.age} years old")


class Dog():
    pass


c = Cat(36, "Simmons", "Green", "Tabby")

c.speak
c.show
