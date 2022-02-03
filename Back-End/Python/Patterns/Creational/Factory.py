# FACTORY

# IS AN OBjECT SPECIALIZED IN CREATE ANOTHER OBJECTS

# USEFUL

#   1.Uncertainties in types of objects to create
#   2.Decisions to be made at runtime regarding what classes to use

class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says Woof!"


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says Miauu!"


def get_pet(pet="dog"):
    """ The Factory Method"""
    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))
    return pets[pet]


print(get_pet("dog").speak())

print(get_pet("cat").speak())
