# Algorithm

# A set of steps a program takes to finish a task

# There is an established bodies of knowledge that give us tools to solve certain problems

# The most important part of algorithm is to know when to use certain algorithm

# Give us an understanding of complexity and efficiency

# Linear Search = Is a search algorithm. Is going one by one until find the desire result

array = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

valueSearch = 5

for a in array:
    if a == valueSearch:
        print('Found It')
        break

# Guides for an algorithm

# Clearly defined problem statement, input, and output -> Break the problem into smaller problems that contains a
# specific input and a specific output

# The steps in the algorithm need to be in a very specific order

# The steps also need to be distinct

# The algorithm should complete in a finite amount of time

# For a given input it must result in the same output every time

# Efficiency -> Time and Space

# Time Complexity -> How long it takes to an algorithm to run

# Space Complexity -> The amount of memory take from the computer

# We can test linear search with the best case and the worst case scenario to help us measureless the efficiency of
# an algorithm

# Binary Search
# Finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that
# could contain the item, until you've narrowed down the possible locations to just one. We used binary search in the
# guessing game in the introductory tutorial.
import time


def binary(search_value=2, search_array=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)):
    """
        Instead of doing int(len(search_array) / 2 we can do len(search_array) // 2
        double slash means floor, this will round up the result of the division
    """
    middle_of_array = len(search_array) // 2

    if search_array[middle_of_array] == search_value:
        return print(f'Found The Number {search_array[middle_of_array]}')

    if search_array[middle_of_array] > search_value:
        return binary(search_value, search_array[:middle_of_array])

    return binary(search_value, search_array[middle_of_array:])


numbers = [x for x in range(0, 1000000)]
start = time.time()
binary(1, numbers)
end = time.time()
print(end - start)
# We want to evaluate the algorith in the worst case scenario

# We can make a graphic with the number of tries or run time in the y axis
# and the maximum number of options in the x scenario
#
# Tries
#   |
#   |
#   |
#   |
#   |
#   |____________________ n
#
# With this graphic we can estimate the Order of Growth
#
# This leads to the Big(O) notation

# Big O
# Theoretical definition of the complexity of an algorithm as a function of the size
# Notation use to describe complexity
# Simplify everything to a single variable

# An example looks like this O(n) -> Order of magnitude of complexity
# This only serve when we are comparing algorithm that solves the same problem
# For example linear search vs binary search.

# O (n) -> A function of the size -> Upper Bounds of the algorithm -> This means that
# Big O measures the performance of the algorithm in the worst case scenario

# O(n) -> Linear Time -> This is a lineal function
# O(log n) -> Logarithmic Time -> This is a logarithmic function
# Log n -> Is how many times I have to divide n to obtain 1
# Log2 8 = 3 -> Because it takes 3 times to divide 8 by 2 to obtain 1
# Log is the opposite of exponential

# Each steps of the algorithm has his own time and space complexity

# When the function is
# Runtime per operations
#         |
#         |
#         |
#         |------------------
#         |__________________
#           n
# This is O(1) the ideal space and time complexity for an algorithm
# In other words this ideal algorithm does not caer of the options size
# because it takes the same time for 1 options and for infinite options
# This is known as constant time
#
#
#
#  |                 .
#  |              .
#  |           .
#  |        .
#  |     .
#  |  .
#  |____________________
#
# When the algorithm makes a diagonal line is known as
# Linear and in notation is illustrated as O(n)
#
#
# Another commons big(o)
#
# Quadratic times
# x^2 -> O(n^2)
#
# Cubic Runtimes
# x^3 -> O(n^3) -> This is very rare to encounter
#
# Quasilinear Runtimes
#
# O(n log n) -> This places between a linear algorithm and a quadratic
# This is seen in Sorting Algorithms -> Merge Sort is the worst
# This all are Polynomial Runtime O(n^k) -> This are considered efficients algorithm
#
# Exponential Algorithms -> These are considered not efficient and are not use in practice
#
# O(X^n)
#
# Factorial Algorithms
#
# n! = n(n-1)(n-2).....(2)(1)
#
#
# We base our analysis in the step of the algorithm that takes more time
# In some cases we can analysis the average case if we control the amount of inputs
