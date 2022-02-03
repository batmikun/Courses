# ABSTRACT FACTORY

# USEFUL

#   1.The user expectation yields multiple, related objects


# Pet Factory -> Cat Factory
#             -> Dog Factory

# Abstract Factory -> Pet Factory

# Concrete Factory -> Dog Factory And Cat Factory -> Oftehn Singleton

# Concrete Product -> Dog and Dog Food, Cat and Cat Food

class Dog:
    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"


class DogFactory:
    def get_pet(self):
        return Dog()

    def get_food(self):
        return "Dog Food!"


class PetStore:
    def __init__(self, pet_factory=None):
        self.pet_factory = pet_factory

    def show_pet(self):

        pet = self.pet_factory.get_pet()

        print("Our pet is {}".format(pet))
        print("our pet says hello by {}".format(pet.speak()))
        print("Its food is {}".format(pet_factory.get_food()))
