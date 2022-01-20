# SOLID

# Software is always in a state of flux -> it is changing
# and each change generates ripples

# The changes has to be isolated and controlled to avoid ripples

# In OOP

# Can confine the ripples of change to a single class
# Allow separation of concerns:
#           - Algorithms and data structures choices
#           - Operating system varieties

# What are the cocerns??

# SOLID principles:
#          - Common Concerns - What they are?
#          - Separation Techniques - Design patterns
#          - Ripple Effects - Control Change - Prevental Disasters
#
#
# Overview

# 1. Prevent Problems -> What can go wrong will go wrong
# 2. Distinguish Styles from Substance -> Is this just rearranging white space?

# Five Design Principles

# S: Single Responsability
# O: Open/Closed
# L: Liskov Substitution
# I: Interface Segregation
# D: Dependency Inversion

# Other OO Principles that will help us understand and implement better SOLID

# 1 - Don't repeat yourself (DRY) -> Avoid code duplication
# 2 - GRASP - General Responsability assignment software principles -> Allocate responsibilities to classes
# 3 - TDD - Test Driven Development -> Write tests first, then code

# This principles are not a formal methodology for class design
# The principles overlap each other sometimes
# Have multiple points of view

# SOLID is an aid not a rigid formula

# The differences between desing are performance, less use memories
# We can desing a class in different ways, what we choose depends on what we want

# There are other prolbems like Deployment, Support, and Maintenance
# The SOLID principles are not a solution to these problems

# SOLID ONLY FOCUSES ON THE RIPPLE EFFECT FROM CHANGE
# AND HOW WELL THE SOFTWARE FITS THE SOLUTION

# The nmemonic SOLID ir pure poetry, but poor on pragmatism

# We are gonna start with:

# INTERFACE SEGREGATION PRINCIPLE
# - Helps design good classes
# - Helps write unit test cases

# After segregating the interfaces,it helps to look at how subclasses extends to superclasses
# LISKOV SUBSTITUTION PRINCIPLE
# - Objects of some superclass S can be replaces with objects of anu subclass of s
# - Constrains subclass desing
# - Helps programmers design good polymorphism

# OPEN/CLOSED
# - Fine way to tune the design, it help to desing wich features of the class needs to be exposed
# - Open to extension means adding subclasses as needed
# - Closed to modification avoids "tweaking" the code to handle new situations

# DEPENDENCY INVERSION
# - Packagin the code, some languajes have tools or framework taht helps us to implement it
# - A direct dependency--on a concrete class--needs to be "inverted"
# - Depend ob abstraction classes or interfaces
# - Avoid concrete class name dependencies

# SINGLE RESPONSIBILITY
# - Summary of the other four principles, after applying them a class tends to be:
# - One responsibility per class
# - Follow-up questions:
#       - At what level of abstraction should the class be?
#       - How are the responsibilities counted?


# INTERFACE SEGREGATION PRINCIPLE
# No client should be forced to depend on methods it does not use
# A cliente should depend on the smallest set of interface features:
#   - the fewest methods and attributes

class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        print('Vehicle is moving')

    def stop(self):
        print('Vehicle is stopping')


class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name)

    def move(self):
        print('Car is moving')

    def stop(self):
        print('Car is stopping')


class Plane(Vehicle):
    def __init__(self, name):
        super().__init__(name)

    def move(self):
        print('Plane is moving')

    def stop(self):
        print('Plane is stopping')

# LISKOV SUBSTITUTION PRINCIPLE
# Proper design satisfy the rule that objects of some superclass S can be replaced with objects of any subclass of s
#              SuperClass
# Subclass 1            Subclass 2
#
# The behaivor of the subclass has to be the same as the superclass
# The difference between the Segregation and Liskov is that for the second to work
# The class and subclass has to have the same methods and attributes


class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print('Animal is moving')

    def stop(self):
        print('Animal is stopping')


class Dog(Animal):
    def move(self):
        print('Dog is moving')

    def stop(self):
        print('Dog is stopping')


class Cat(Animal):
    def move(self):
        print('Cat is moving')

    def stop(self):
        print('Cat is stopping')

# After we do segregation, and we want to see if the class are substituable
# we have to pay attention to the metods and attributes
# If the method of the subclass are incompatible with the superclass,
# The subtitution is not possible

# In this case we have two options:
#   1 - Rethink : Is this distinction important or necessary?
#   2 - Refactor : Can the distinction be pushed up to the superclass?

# Unit test cases are required to show Liskov substitution

# Sometimes the subclasses are not gonna be substituable, but that is fine
# Because we can have a superClass Furniture
# and to subclasses like Chair and Table
# The both subclasses are sustituable to the superclass
# But the beetwen them are not
# And that is okey because a chair has nothing to do with a table

# Sometime when the subclass has new attributes that the superclass don't

# We can use default values in the subclass constructor

# Another way to avoid default values is to
# convert those parameters into methods

# BASICALLY LISKOV LOOKS AT THE SIGNATURE OF ALL THE CLASSES
# THE SIGNATURE IS THE EXPOSED METHODS AND ATTRIBUTES
# ARE THE SIGNATURES COMPATIBLES
# THE NEW CLASS ONLY ADD NEW METHODS AND ATTRIBUTES
# IF THIS CONDITIONS MET, LISKOV IS POSSIBLE
# IF ABSOLUTE NECCESARY TO BUILD UNIT TEST CASES


# OPEN CLOSE PRINCIPLE
# - This principle says that the class has to be open
# - for extension, but closed for modification
# - This principle is closed align with Segretation and Liskov
# - Summerize the golds of Segregation and Liskov

# Constant be parameterized always
# Features should be parameterized in a way that the subclass can override them
# There has no need to modify a class for adding a new feautures
# Our class should be expanded trhough subclasses

# Our goal is to use inheritance and composition to build
# classes that we don't have to modify to expand

# Composition is a way to build a class from other classes

# Extending a class

# 1 - Inheritance
# 2 - Composition:
#        - This patterns are a way to extend classes trhough composition
#        - Strategy
#        - Adapter
#        - Decorator

# Is there a need to modify the class?
# Is there a way to extend the class to make changes?
# This are the questions proposed by the Open/Close Principle
# The idea is to not modify the source code, to avoid possible bugs or break eberithing


# DEPENDECY INVERSION

# Depends on two things
# "High level modules should not depend on low level modules"
# "Both should depend on abstractions"

# The high level modules should depend on details.
# Details should depend on abstractions.

# DEPENDE ON ABSTRACTION

# "direct" dependency: hard-wired reference to a concrete class (common class)
    # Often includes the class constructor

# "Inverted" dependency: a reference to an abstraction
    # Ideally, an object construction id indirect via a factory

# ISP, OCP, DIP encourage the Factory Pattern
