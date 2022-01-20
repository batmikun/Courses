# Python Course

# The indentation is SUPER IMPORTANT!!!!

# Reserved Words : False, None, True, and, as, assert, break, class, if, def, del, elif, else, except,
#                  return, for, from, global, try, import, in, is, lambda, while, not, or, pass, raise,
#                  finally, continue, nonlocal, with, yield

# Assignment x = 2
# Sum x = x + 2
# Dump -> print() ('More close to echo because print in console')

# Interactive Python is good for experiments and programs of 3-lines long

# Script, just like a php script

# Flow
# Sequence (1 rst, 2 cnd), Conditional (if, while), Repeated (for, foreach, etc)

# Sequential
# => A partir de 3.7 no se necesita mas porque el dict regular tiene la misma funcionalidad
from contextlib import contextmanager
from queue import Queue
from queue import queue
from typing import ContextManager
from quere import queue
from threading import Thread, Lock, current_thread
from threading import Thread
from multiprocessing import Process
import functools
import os
import numpy as np  # => This is the alias
import secrets  # => password, security token, etc. The algorithms are slower
import random
import logging
from collections import defaultdict
from collections import OrderedDict
from collections import namedtuple
from collections import Counter
from functools import reduce
from itertools import accumulate, combinations, combinations_with_replacement, cycle, groupby, permutations, product
from timeit import default_timer as timer, repeat
import time
import csv
import sqlite3
import urllib.error
import urllib.parse
import urllib.request

from bs4.element import Tag
import twurl
import hidden
import oauth
import urllib
import json
import xml.etree.ElementTree as ET
import ssl
from bs4 import BeautifulSoup
import socket
import re

print('Sequential')
x = 2
print(x)
x = x + 2
print(x)

# Conditional
print('Conditional')
x = 5
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')
print('Finis')

# Repeated
print('Repeated')
n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff!')

# All together
name = input('Enter file:')
handle = open(name, 'r')

counts = dict()  # data structure
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None

for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)

# Constants
# Fixed values such as numbers, letters, and strings

# Variables Name Rules
# Must start with a letter or underscore
# Case Sensitive

# Mnemonic Variable Name
# The name of the variables has to help us remember what we storage in that variable
# mnemonic = memory aid

# Assignment statement
# x (name of variable) = (expresion)

# Numeric Expressions
# + Addition
# - Subtraction
# * Multiplication
# / Division
# ** Power
# % Remainder

# Operator Precedence Rules

# Parenthesis, Power, Multiplication or Division, Addition or Substraction, Left to Right

# Type
# Variables, literals and constants have a "type"
# Knows the difference between an integer and a string
# + means addition, both for numbers and strings
# 'Hello' + 1 is not as PHP that converts the int to a string, in Python trows a error
# with the function type(variable) we can learn the type of a variable
# ints are divied in int and float

# Type Conversion
# with functions we can convert type, for example with the function float(99) we convert int 99 to float 99.0

# The division always return a float type

# String Conversions
sval = '123'
# transforms sval into an integer only if the string is numeric
ival = int(sval)

# User input
# To ask the user for data, we use the function input
name = input('Who are you? ')
print('Welcome', name)
# The input() function returns a string

inp = input('Europe floor?')
usf = int(inp) + 1
print('US floor', usf)

# Conditional Execution
# if condition:
#   instructions

# Comparison Operator
# < Less than
# <= Lass than or Equal to
# == Equal to
# >= Greater than or Equal to
# > Greater than
# != Not equal

# Indentation
# Increase indent: indent after an if statement or for statement (after :)
# Maintain indent to indicate the scope of the block
# Reduce indent back to the level of the if statement or for statement to indicate the end of the block
# Blank lines are ignored - they do not affect indentation
# The indentation has to be 4 spaces (is not the same as a tab)

# if/else
x = 4
if x > 2:
    print('Small')
elif x < 10:
    print('Medium')
else:
    print('Large')
print('All done')

# For handle blowout errors we use try/except
number = input('Enter a number:')
try:
    int(number)
    print('Nice work')
except:
    print('You do not input a number')

# Functions

# Functions are defined with the reserved word def (definition) it not runs at less is it invoke


def thing():
    print('Hello')
    print('Fun')


# To run the function you call it
thing()
print('Zip')
thing()

# Two type of functions

# 1) Built-in functions - print(), input(), type(), float(), int()
# 2) Functions that we define ourselves

# 1)
big = max('Hellor wordl')  # scans the biggest character in the string
print(big)
tiny = min('Hello world')  # scans the smallest character in the string
print(tiny)

# A function is some stored code that we use. A function takes some input and produces an output
# An argument is a value we pass into the function as its input when we call the function
# A parameter is a variable wich we use in the function definition. It is a "handle" that allows the code in the function to access the arguments for a particular function invocation


def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')


greet('en')
greet('es')
greet('fr')

# Return values
# Often a function will take its arguments, do some computation, and return a value to be used as the value of the function call in the calling expression. The return keyword is used for this


def greet():
    return 'Hello'


print(greet(), 'Glenn')

# If the function doesn't have a return, the last line is consider the return.
# A "fruitful" function is one that produces a result (or return value)
# The return statement ends the function execution and "sends back" the result of the function
# When a function does not return a value, we call it a "void" function, this functions are not "fruitful"

# Loops and iteration

while n > 0:
    print(n)
    n = n - 1

print('Blastoff!')
print(n)

# Loops have iteration variables that change each time through a loop. Often the iteration variables go through a sequence of numbers.
# Breaking out of a loop
# The break statement ends the current loop and jumps to the statement inmediately following the loop
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')
# Continue statement ends the current iteration and jumps to the top of the loop and starts the next iteration
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

# The while loop is define as a "Indefinite loops"

# Definite Loops
# Quite often we have a list of items of the lines in a file - effectively a finite set of things
# We can write a loop to run the loop once for each of the items in a set using the Python for construct
# We say that "definite loops iterate through the members of a set"

# For loop
for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff!')

friends = ['Joseph', 'Nicolas', 'Jimena']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')

# Definite loops (for loops) have explicit iteration variables that change each time through a loop. These iteration variables move through the sequence or the set

largestNumber = 0
for ln in [3, 41, 12, 9, 74, 15]:
    if ln > largestNumber:
        largestNumber = ln
print(largestNumber)

# None have type one value, None is a constant, indicates empty/existent/

smallest = None
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value

print(smallest)

# The 'is' and 'is not' are operator, are comparable to === in PHP compares value and type

# if 0 == 0.0 True but if 0 is 0.0 False

# String Data Type
# A string is a sequence of characters
# A string literal uses quotes 'Hello'
# When a string contains numbers, it is still a string
# We can convert numbers in a string into a nunber using int()
# To concatenar strings we use +, 'Hello' + 'World'

# Looking inside Strings
fruit = 'banana'
letter = fruit[1]  # 'a'
# if you index outside of the range it throws a Traceback
lenght = len(fruit)  # Returns the lenght of the string
# loop through strings
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    index = index + 1

fruit = 'banana'
for letter in fruit:
    print(letter)

# Slicing strings
# we use variable[0:4] The second number is one beyond the end of the slice - "up to but not including"
# If the second number is beyond the of the string, it stops at the end

s = 'Monty Python'
print(s[0:4])  # "Mont"
print(s[6:7])  # "P"
print(s[6:20])  # "Python
print(s[:2])  # "Mo"
print(s[2:])  # "nty Python"

# We can use in as a logical operator
fruit = 'banana'
'n' in fruit  # True
'nan' in fruit  # True
if 'a' in fruit:
    print('Found it!')

# String Comparison, be always aware if the strings are uppercase or lowercase. Always compare in the same case.
# String Library, Python has a number of string functions which are in the string library, these buil into function are in every string - we invoke them by appending the function to the string variables
# These function does not modiffy the original string, these functions make a copy

greet = 'Hello Bob'
zap = greet.lower()
print(zap)  # 'hello bob'

stuff = 'Hello world'
type(stuff)  # <class 'str'>
dir(stuff)  # Return all the functions that can be applied to a string

# Find
fruit = 'banana'
pos = fruit.find('na')  # 2

# Upper and Lower
greet = 'Hello Bob'
nnn = greet.upper()  # HELLO BOB
www = greet.lower()  # hello lob

# Search and Replace
greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane')  # Hello Jane
nstro = greet.replace('o', 'X')  # HellX BXb

# Stripping Whitespace
greet = '    Hello Bob   '
greet.lstrip()  # 'Hello Bob  '
greet.rstrip()  # '    Hello Bob'
greet.strip()  # 'Hello Bob'

# Prefixes
line = 'Please have a nice day'
line.startswith('Please')  # True
line.startswith('p')  # False

# Parsing and Extracting
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)  # 21
sppos = data.find(' ', atpos)  # find(what we whant to find, starting position)
print(sppos)  # 31
host = data[atpos + 1: sppos]
print(host)  # uct.ac.za

# In Python 3, all strings are Unicode

# Reading Files
# A text file can be thought of as a sequence of lines
# Before we can read the contents of the file, we must tell Python which file we are going to work with and what we will be doing with the file
# This is done with the open() function
# open() returns a "file handle" - a variable used to perfom operations on the file

handle = open(filename, mode)

# filename is a string
# mode is optional and should be 'r' if we are planning to read the file and 'w' if we are going to write to the file
# methods open, read, write, close

# The newline Character
stuff = 'Hello\nWorld!'
# Hello
# World!

# The \n is a character
stuff = 'X\nY'
len(stuff)  # 3

# All the lines in a file when read it, have a \n in the end, even those that are empty
xfile = open('mbox.txt')
for line in xfile:
    print(line)

# We can use the for statement to iterate through a sequence
# Remember - a sequence is an ordered set
# We can read the whole file(newlines and all) into a single string
fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))  # 31312
print(inp[:20])  # The first 20 characters
# print adds a new line \n
fhand = open('mbox.short.txt')
for line in fhad:
    line = line.rstrip()  # eliminates \n (eliminates all non-printable characters)
    if line.startswith('From:'):
        print(line)

# We can structure the loop in diffent way
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)

for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)

fname = input('Enter the file name: ')

try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1

print(count)

# quit() is like die()

# Python Lists

# Algorithms : A set of rules or steps used to solve a problem
# Data Structures : A particular way of organizing data in a computer

# Collections : allows us to put many values in a single "variable". Is nice because we can carry all many values around in one convenient package

# List is a simple array, the list have index just like an array
list = [1, 2, 76]
another_list = [1, [5, 6], 7]

# List are mutable, strings are "immutable" - we cannot change the contents of a string - we must make a new string to make any change
# Lists are "mutable", we can change an element of a list using the index operator
# The len() function takes a list as a parameter and returns the number of elements in the list
# Using the range function, the range function returns a list of number that range from zero to one less than the parameter

print(range(4))  # [0,1,2,3]
friends = ['nico', 'jime', 'jessi']
print(range(len(friends)))  # [0,1,2]

for friend in friends:
    print(friend)

for i in range(len(friends)):
    friend = friends[i]
    print(friend)

# We can concatenate lists using +
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)  # [1,2,3,4,5,6]

# Also we can slice the lists
t = [9, 41, 12, 3, 74, 15]
t[1:3]  # [41,12]
t[:4]  # [9,41,12,3]

# List Methods: append, count, extend, index, insert, pop, remove, reverse, sort

# Append
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)  # ['book', 99]
stuff.append('cookie')
print(stuff)  # ['book', 99, 'cookie']

# In operator
some = [1, 9, 12, 15]
9 in some  # True
15 in some  # True
20 not in some  # True

# Lists are in order
friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends)['Glenn', 'Joseph', 'Sally']

# Max
# Finds the largest
# Min
# Finds the smallest
# Sum
# Sums all the elements of the list

# Split breaks a string into parts and produces a list of strings. We think of these as words. We can access a particular word or loop through all the words

abc = 'With three words'
stuff = abc.split()
print(stuff)  # ['With', 'three', 'words']

# Split without parameter searchs for spaces (all withespaces)

line = 'first;second;third'
thing = line.split(';')
print(thing)  # ['first', 'second', 'third']

han = open('mbox-short.txt')

for line in han:
    line = line.rsttrip()
    wds = line.split()
    # Guardian Pattern (protects a algorith to throw a bakctrace or break)
    if len(wds) < 1:
        continue
    # This could blow up
    if wds[0] != 'From':
        continue
    print(wds[2])

# Dictionaries
# Data structure where the data contains key, and is not in order [in PHP they are the associative array]

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)  # {'money': 12, 'tissues': 75, 'candy': 3}
print(pruse['candy'])
purse['candy'] = purse['candy'] + 2

# Dictionary Literals
# Dictionary literals use curly braces and have a list of key:value pairs

jjj = {'chuck': 1, 'fred': 42, 'jan': 12}

# We cannot look for a key that doesn't exist
# But with the in operator we can ask if the key exist

ccc = {'Herv': 12}
if 'csev' in ccc:
    ccc['csev'] = 43

# The get method for dictionaries
# The pattern of checking to see if a key is already in a dictionary and assuming a defult valuey if the key
# is not there is so common that there is a method called get() that does this for us

if name in counts:
    x = counts[name]
else:
    x = 0

x = counts.get(name, 0)

# This is usefull to do estadistics
counts = dict()
names = ['csev', 'cwen', 'zquian', 'cwen']

for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)

# Counting Pattern
counts = dict()
print('Enter a line of text:')
words = line.split()
print('Words:', words)
print('Counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)

# The general pattern to count the words in a line of text is to split the line into words, then loop trhough the words and use a dictionaty to track the count of each word independently

# Even though dictionaries are not stored in order, we can write a for loop that goes through all the entries in a dictionary - actually it goes through all of the keys in the dictionary
# and looks up the values

counts = {'chuck': 3, 'fred': 42, 'jan': 100}

for key in counts:
    print(key, counts[key])
# Retrieving lists of Keys and Values
jjj = {'chuck': 1, 'fred': 42}
print(jjj.keys())  # ['chuck', 'fred']
print(jjj.values())  # ['1', '42']
# [('chuck', 1), ('fred', 42)] This is a tuple (combined data structure)
print(jjj.items())

jjj = {'chuck': 1, 'fred': 2}
for aaa, bbb in jjj.items():
    print(aaa, bbb)  # chuck 1

fname = input('Enter File: ')
if len(fname) < 1:
    fname = 'clown.txt'
handle = open(fname)

dic = dict()

for line in handle:
    line = line.rstrip()
    words = line.split()
    for w in words:

        if w in dic:
            dic[w] = dic[w] + 1
            print('__Existing__')
        else:
            dic[w] = 1
            print('__New__')
        print(w, dic[w])

# Better way to do a count a word
    for line in handle:
        line = line.rstrip()
        words = line.split()
        for w in words:
            # w the key we are trying to find, 0 the default value if that key doesn't exist in the dic
            oldcount = dic.get(w, 0)
            newcount = oldcount + 1
            dic[w] = newcount
            # Better way to express this
            # These are the three past lines in one line
            dic[w] = dic.get(w, 0) + 1
print(dic)

"dic.get(key, defaultvalue if key doesn't exist)"

# now we want to find the most common word
largest = None
theword = None
for word, count in dic.items():
    if largest is None:
        largest = count
    if count > largest:
        largest = count
        theword = word


# TUPLES
# Tuples are another kind of sequence that functions much like a list - they have elements which are indexed starting at 0
# Tuples are "immutable"
t = (5, 4, 3)  # Tuple
l = [9, 8, 7]  # List
d = {'hola': 1}  # Dictionary

# Everything that you can do to a list that modify the list, you can't do it to a Tuple
# Tuple has to in-built functions count(), index()
# It creates with
tuple = tuple()  # They are more eficient than list and dictionary

# We prefer tuples over lists, when the thing we create is something temporary
(x, y) = (4, 'fred')  # tuples can go in the right side
print(x)  # 4
print(y)  # fred

# The items() methos in dictionaries returns a list of (key, value) tuples
tups = d.items()
print(tups)  # [(csev, 9), (sc, 10)]
# The Tuples are comparable
# The comparison operator work with tuples and other sequences, If the first item is equal, Pythos goes on to the next element, and so on, until it finds elements that differ
# Only scans until find the anwser

d = {'a': 10, 'b': 1, 'c': 22}
d.items()  # List of tuples ([('a', 10), ('b', 1)])
sorted(d.items())  # This sort for the key of the dictionarie

# You can sort the values when entering the for
for k, v in sorted(d.items()):
    print(k, v)

# If we could construc a list of tuples of the form(value,key) we could sort by value
# We do this with a for loop that creates a list of tuples

c = {'a': 10, 'b': 1}
tmp = list()
for k, v in c.items():
    tmp.append((v, k))
print(tmp)
[(10, 'a'), (1, 'b')]
tmp = sorted(tmp, reverse=True)
[(1, 'b'), (10, 'a')]

# Top 10 most common words
fhand = open('romeo.txt')
counts = dic()
for line in fhand:
    words = line.split()
    for word in words:
        counts[words] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:10]:
    print(key, val)

# Even Shorter Version
c = {'a': 10, 'b': 1, 'c': 22}
# This code does the same thing that the code on top
print(sorted([(v, k) for k, v in c.items()]))

# List comprehension creates a dynamic list. In this case, we make a list of reversed tuples and then sort it

# REGULAR EXPRESSIONS
# Provides a concide and flexible means for matching strings of text, such as particular characters, words, or patterns of characters. A regular expression is written in a formal language
# that can be interpreted by a regular expression processor
# Really clever "wild card" expressions for matching and parsing strings

# Very powerful and quite cryptic
# Fun once you understand them
# Regular expressions are a language unto themselves
# A language of "marker characters" - programming with characters
# It is kind of an "old school" language - compact

# ^ Matches the beginning of a line
# $ Matches the end of the line
# . Matches any character
# \s Marches whitespace
# \S Matches any non-whitespace character
# * Repeats a character zero or more times
# *? Repeats a character zero or more times (non-greedy)
# + Repeats a character one or more times
# +? Repeats a character one or more times (non-greedy)
# [aeiou] Matches a single character in the listed set
# [^XYZ] Mathes a single character not in the listed set
# [a-z0-9] The set of characters can include a range
# ( Indicates where string extraction is to start
# ) Indicates where string extraction is to end

# Before you can use regular expressions in your program, you must import the library using "import re"
# You can use re.search() to see if a string matches a regular expression, similar to using the find() method for strings
# You can use re.findall() to extract portions of a string that match your regular expression, similar to a combination of find() and sliceng: var[5:10]

# Using re.search() like find()


hand = open('hola.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)

# Using re.search() like startswith()
hand = open('hola.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):  # ^Solamente busca string que empiecen con From
        print(line)

# X-Sieve: CMU Sieve 2.3  Regular expresion [^X.*:] Strings que empiezen con X que tengan uno o mas caracteres por delante y que terminen con un colon "X-Sieve:"

# X-Sieve asdasda: CMU Sieve 2.3  Regular expresion [^X-\S+:] Strings que empiezen con X- y que tengan uno mas non-whitespaces character followed by a color "Not Match because has whitespace"

# From matching and extracting data
# re.search() returns a True/False
# re.findall() return the strings that matchs

x = 'My 2 favorite numbers are 19 and 42'
# [0-9] This is one character we add the + to say that we want to match with all the digits 0,1,2,3,4,5,6,7,8,9
y = re.find('[0-9]+', x)

x = 'From: Using the : character'
# When te thing is in greedy the regexp choose the largest one 'Using the:' that is greedy
y = re.findall('^F.+', x)

y = re.findall('^F.+?:', x)  # This is not-greedy, this return 'From:'

x = 'From stephen.marquard@uct.ac.za Sat'
y = re.findall('\S+@\S+', x)  # This return the email

# You can refine the match for re.findall() and separately determine wich portion of the match is to be extracted by using parentheses

# The parentheses indicates what you want to extract
y = re.findall('^From (\S+@\S+)', x)

# This return the host [^ ] This is other way to match many non-whitespace characters
y = re.findall('@[^ ]*', x)

# Escape Character : if we want to search for $ we have to escapate with \ because $ is reserved character

# Representing Simple Strings
# Each character is represented by a number between 0 and 256 stored in 8 bits of memory
# We can know the ASCII order of a character with the funcion ord

print(ord('H'))

# Python use unicode internally, that is why when we send something across the network we have to encode() and decode() the response (encode transform unicode to utf-8)
# UTF-8 - 1-4 bytes
# UTF-8 is recommended practice for encoding data to be exchanged

x = b'abc'
type(x)  # bytes
x = 'koreano'
type(x)  # str
x = u'koreano'
type(x)  # str

# When we talk to a network resource using sockets or talk to a database we have to encode and decode data (usually to UTF-8)


# We create a socket that is a stream, and is the type that goes trhough the internet
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Define the host o url and port we want to connect
mysock.connect(('data.pr4e-org', 80))
cmd = 'GET http://data.pr4e.com/romeo.text HHTP/1.0\n\n'.encode()  # Prepare

mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()

# Making HTTP easier with urlib
# Using urllib in Python


# By default this doesn't show the headers, we can read .txt .html
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

# Parsing HTML (a.k.a Web Scrapping)
# When a program or script pretends to be a browser and retrieves web pages, looks at those web pages, extracts information, and then looks at more web pages
# Search engines scrape web pages - we call this "spidering the web" or "web crawling"

# Pull data
# Get your onw data back out of some systema that has no "export capability"
# Monitor a site for new information

# Beautiful Soup save us the time and retrieves for us the text from the HTML


# Ignore SSL certificate errors for https
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag - get('href', None))

# With the HTTP Request/Response well understood and well supported, there was a natural move toward exchanging data between programas using these protocols

# WEB SERVICIES
# Agreeing on a "Wire Format"
# Two formats of comunication XML, JSON

# XML - eXtensible Markup Language
# Primary purpose is to help information systems share structured data
# Terminology
    # Tags indicate the beginning and ending of elements
    # Attributes - Keywords/value pairs on the openning tag of XML


input = '''
<stuff>
    <users>
        <user x"2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x"2">
            <id>001</id>
            <name>Jeff</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
# Find retrieves one tag, Findall retrieves multiple tag
list = stuff.findall('users/user')

for item in list:
    print('Name ', item.find('name').text)
    print('Id ', item.find('id').text)
    print('Attr ', item.get("x"))

# XML SCHEMA
# Description of the legal format of an XML document
# Expressed in terms of contraints on the structure and content
# Language: DTD, XSD
# XSD xs:element xs:sequence xs:complexType types: xs:string xs:integer xs:date

# JSON - JavaScript object notification

data = '''{
    "name": "Chuck",
    "phone": {
        "tpye": "intl",
        "number": "+1 734 303 4456"
    },
    "email" : {
        "hide": "yes"
    }
}'''

info = json.loads(data)  # This returns a dictionarie
print('Name: ', info["name"])
print('Hide: ', info["email"]["hide"])

# Service Oriented Approach

input = '''
[
    {
        "id": "001",
        "name": "Chuck
    },
    {
        "id": "001",
        "name": "Chuck
    }
]'''

info = json.loads(input)
print('User count: ', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])


# Json {} that starts with curly braces transform into a dictionarie, a json that start with [] transform into a list of dictionaries

# Most non-trivial web app use servicies
# They use services from other app
    # Credit Card Charge
    # Hotel Reservation systems
# Services publish the "rules" app must follow to make use of the service(API)

# WEB SERVICES
# API = Application Program Interface. Is a contract that you got to fullfil to gain access to the data.


serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address < 1):
        break
    url = serviceurl + urllib.parse.urlencode({'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

# The compute resouerces to run these APIs are not free
# The data providede by these APIs is usually valuable
# The data providers might limit the number of request per day, demand an API "key", or even charge for usage
# They might change the rules as things progress...

# TWURL


def augment(url, parameters):
    secrets = hidden.oauth()
    consumer = oauth.OAuthConsumer(
        secrets['consumer_key'], secrets['consumer_secret'])
    token = oauth.OAuthToken(
        secrets['consumer_key'], secrets['consumer_secret'])
    oauth_request = oauth.OAuthRequest.from_consumer_and_token(
        consumer, token=token, http_method='GET', http_url=url, parameters=parameters)
    oauth_request.sign_request(
        oauth.OAuthSignatureMethod_HMAC_SHA1(), consumer, token)
    return oauth_request.to_url()

# HIDDEN


def oauth():
    return{"comsumer_key": "123122", "consumer_secret": "12312313", "token_key": "a112312", "token_secret": "ad123asd"}


TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

while True:
    print(' ')
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1):
        break
    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '5'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url)
    data = connection.read().decode()
    headers = dict(connection.getHeaders())
    print('Remaining', headers['x-rate-limit-remaining'])
    js = js.loads(data)
    print(json.dumps(js, indent=4))

    for u in js['users']:
        print(u['screen_name'])
        s = u['status']['text']
        print('  ', s[:50])

# OBJECT ORIENTED
    # A program is made up of many cooperating objects
    # Instead of being the "whole program" - each object is a little "island" within the program and cooperatively working with other objects
    # A program is made up of one or more objects working together - objects make use of each other's capabilities
    # An object is a bit of self-contained code and data
    # Objects hide detail - they allow us to ignore the detail of the "rest of the program"
# What contains an object?
    # "CLASS" - a template - Dog
    # Method or Message - A defined capability of a class - bark()
    # Filed or attribute - A bit of data in a class - lenght
    # Object or Instance - A particular instance of a class - Lassie

# CLASS - Defines the characteristics of a thing (object), including the thing's characteristics (its attributes, fields or properties) and the thing's behaviors(methods, operations or features)
        # One might say that a class is a blueprint or factory that describes the nature of something. For example, the class Dog would consist of traits shared by all dogs, such as bree and
        # fur color(characteristics), and the ability to bark and sit (behaviors)


class PartyAnimal:  # This is the template for making PartyAnimal objects
    x = 0

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)


an = PartyAnimal()  # Construct a PartyAnimal object and store in an

an.party()
an.party()
an.party()

# Object Lifecycle
# Objects are created, used and discarded
# We have special blocks of code (methods) that get called
# At the moment of creation (consctructor)
# At the moment of destruction (destructor)
# Constructors are used a lot
# Destructors are seldom used


class PartyAnimal:
    x = 0

    def __init__(self):
        print('I am constructed')

    def party(self):
        self.x = self.x + 1

    def __del__(self):
        print('I am destructed', self.x)

# Inheritance
    # When we make a new class - we can reuse an existing class and inherit all the capabilities of an existing class and then add our own little bit to make our new class
    # Another form of store and reuse
    # Write once - reuse many times


class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, nam):
        self.name = nam

    def party(self):
        self.x += 1

# FootballFan is a class which extends PartyAnimal. It hass all the capabilities of PartyAnimal and more


class FootballFan(PartyAnimal):
    points = 0

    def touchdown(self):
        self.points += 7
        self.party()


# Relational Databases and SQLITE
    # Model data by storing rows and columns in tables. The power of the relational db lies in its ability to efficiently retrieve data from those tables and in particular where there are
    # multpile tables and the relationships between those tables involved in the query

    # Database - contains many tables
    # Relation (or table) - contains tuples and attributes
    # Tuple (or row) - a set of fileds that generally represents an "object" like a person or a music track
    # Attribute (also column or filed) - one of possibly many elements of data corresponding to the object represented by the row


# This creates the file if don't exist
conn = sqlite3.connect('emaildb.sqlite')

conn.execute('DROP TABLE IF EXISTS Counts')

conn.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

fname = input('Enter file name: ')

if(len(fname) < 1):
    fanme = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    conn.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    row = conn.fetchone()
    if row is None:
        conn.execute(
            'INSERT INTO Counts (email, count) VALUES (?, 1)', (email,))
    else:
        conn.execute(
            'UPDATE Counts SET count = count + 1 WHERE email = ? ', (email,))

    conn.commit()

sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in conn.execute(sqlstr):
    print(str(row[0]), row[1])

conn.close()

# grid wonder horror lobster truck seed file extra shrimp globe history canyon

# OOP In Python
# We can assing attibutes wihtout the neccessity of adding variables in the class itself
# We can say the tipes that a def expect, by assinging the paramter:type or parameter=0 (default value 0 already tells python that the parameter is int)
# We can validate the parameter that a function recives with the command assert , assert price >= 0, f"Message"


class Item:
    pay_rate = 0.8  # Class attribute
    all = list()

    def __init__(self, name: str, price: float, quantity: int):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater or equeal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equeal to zero!"

        # Assing to self object
        self.__name = name  # Adding double underscore makes that attribute private
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @ property  # Property Decorator = Read-Only Attribute outside of the class
    def name(self):  # Definition of getter in python, this is call when you try to show o access to the value like item.name
        return self.__name

    @ name.setter  # This decorator is used to create a setter in a property that is readonly
    # This is used where you want to set an attribute item.name = value
    def name(self, value):
        self.__name = value

    # All the methods of a class recives as a first argument the instance of the object
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):  # This magic method help us to change the way that a object is represented in console
        return f"Item('{self.name}', '{self.price}', '{self.quantity}'')"

    @ classmethod  # This is a decorator from python
    # This is a class method, a static function. The class reference must be passes as an argument
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:  # With defines a context, in this example all the lines indented above the with are gonna run, and when finished the files will close automatically, with can only be use with objects that inherents the context manager interface
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @ staticmethod
    # This is an static method, this doesn't recive neither the self or the cls. This is the difference with @classmethod
    def is_integer(regularParameter):
        # isinstance check if the passed parameter is of that type or not
        if isinstance(regularParameter, float):
            return regularParameter.is_integer()
        elif isinstance(regularParameter, int):
            return True
        else:
            return False


item1 = Item("Phone", 1000, 3)
item1.calculate_total_price()
item1.apply_discount()

item2 = Item("Laptop", 30000, 5)
item2.calculate_total_price()
item2.pay_rate = 0.7  # Reassinging a class attribute makes that python check for the value in the instance and not in the class itself

# We can access the class attributes from the object itself or from an instance, is like a static variable
Item.pay_rate
item1.pay_rate

# Obtain all attributes of a class
# This maggic attribute transforms the object into a dictionary
print(Item.__dict__)

item1 = Item("Phone", 1000, 3)
item2 = Item("Laptop", 200, 1)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 2)
item5 = Item("Keyboard", 75, 7)

for instance in Item.all:
    print(instance.name)

# We have to use staticmethod when this should do something that has a relationship with the class,
# but not something that must be unique per instance!

# We hace to use classmethod when this should do something that has a relationship with the class,
# but usually, those are used to manipulate different structures of data to instantiate objects,
# like we have done with CSV.

# The only main difference between classmethod and staticmethod, is that staticmethod doesn't recive self or cls

# OOP PRINCIPLES

# Encapsulation
# Restricting the direct access to values of an object
# Like with getters and setters
# Creating methods in the class to manipulate the value of the read-only attribute

# Abstraction
# Hide unnesecary information from the instances of a object
# Using private methods, and having one point of entry, etc, private methods can be achived with double underscore, the same as the attributes

# Inheretance
# Mechanism to re-use code, parent class, child class, interfaces, etc
# To make scalable estructures

# Polymorphism
# Is refered to use of a single type entity to represent differents types in differents escenarios
# Refers to many forms
# Have many escenarios that uses a single entity
# For example the function len from python, can tell the lenght of different types of object, string, list, dict, etc.

# sets python is a collection of unordered unique elements
# we can add elements with set.add() this will add elements in the set, if the element already exists, it will not be added

# Numpy is a library that allows us to work with arrays and matrices
# It is a high performance library that allows us to work with large data sets
# It is a multidimensional array, that is a matrix
# numpy.array(list) => creates an array from a list
# numpy.array(list, dtype=float) => creates an array from a list, and the type of the elements is float
# numpy.array(list, dtype=int) => creates an array from a list, and the type of the elements is int
# numpy.array(list, dtype=bool) => creates an array from a list, and the type of the elements is bool
# numpy.sum(array) => sum of all the elements in the array
# numpy.mean(array) => mean of all the elements in the array
# numpy.std(array) => standard deviation of all the elements in the array
# numpy.var(array) => variance of all the elements in the array

# 3

# LISTS

# Is a collection data type that is ordered mutable, and that allows
# duplicate elements

# Dos formas de crear una List

myList1 = list()  # => empty list
mylist2 = ["hola", "chau"]

# Allows different data types

# To acces one intem you reference the index of the list
mylist2[0]  # If you use an index out of range explotes
mylist2[-1]  # If you use a negative index, it starts from the end of the list

# Para recorrer list
for (item, index, key) in mylist2:
    print(item)

# To check if something is in a list

if "hola" in mylist2:
    print(True)

# Cantidad de elementos
len(mylist2)

# Append something to the end
mylist2.append("chau")

# Insert
mylist2.insert(0, "hola")

# Pop
lastItem = mylist2.pop()  # Removes the last element

# Remove
# Removes the first element that matches the value
firstItem = mylist2.remove("hola")

# Remove all elements
mylist2.clear()

# Reverse
mylist2.reverse()  # Reverse the order of the list

# Sort
mylist2.sort()  # Sort the list

# New sorted list
new_list = sorted(mylist2)

# Repet items
mylist = [0] * 5  # [0, 0, 0, 0, 0]


# Concat
mylist1 = [1, 2, 3]
mylist2 = [4, 5, 6]
mylist3 = mylist1 + mylist2

# Slicing, access sub part in your list
mylist1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = mylist[1:5]  # [2, 3, 4, 5]

# If we dont specify the end of the slice, it will go to the end of the list
# If we dont specify the start of the slice, it will go to the start of the list

# Step index
mylist[::2]  # [1, 3, 5, 7, 9]
mylist3[::5]  # [2, 7]

# Copy
list_org = [1, 2, 3]
list_copy = list_org.copy()

# If we do
# It will copy the reference, not the values. This mean that the two list have the same reference in memory
list_copy = list_org

# Comprehesion => Elegant and fast way to create a new list
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [i * i for i in mylist]  # => [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# b = [expresion for item in list]

# TUPLES
# Collections that are ordered and unchangeable
# Tuples are faster than lists
# Tuples are immutable
# They are helpful when we have inteconectable objects

myTyple = (1, 2, 3)

# To have a Tuple for a one item myTuple = (1,)

myTuple = tuple(1, 2, 3)

item = myTuple[0]  # You can also use minus index

for item in myTuple:
    print(item)

if 1 in myTuple:
    print(True)
else:
    print(False)

my_tuple = ['a', 'b', 'c']

len(my_tuple)  # cantidad de elementos
my_tuple.count('a')  # cantidad de a
my_tuple.index('b')  # first indice of the apparence of b

# Convert Tuple to List
my_list = list(my_tuple)
# Convert List To Tuple
my_tuple = tuple(my_list)

# Slicing
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = my_tuple[1:5]  # [2, 3, 4, 5]

# Step
my_tuple[::2]  # [1, 3, 5, 7, 9]

# Unpacking => like destructuring in JS
a, b, c = my_tuple  # a = 1, b = 2, c = 3
# The amount of variables must be the same as the amount of elements in the tuple

i1, *i2 = my_tuple  # i1 = 1, i2 = [2, 3, 4, 5, 6, 7, 8, 9, 10]

# Working with tuples can be more eficcient some times
# especially working with BigData

# DICTIONARY
# Collection data type unordered, mutable, and changeable
# It is a key value pair
mydict = {"key": "value", "key2": "value"}
mydict2 = dict(key="value", key2="value")

value = mydict["key"]

# change
mydict["key"] = "value2"

# add
mydict["key3"] = "value3"

# Remove
del(mydict["key3"])
mydict.pop("key3")
mydict.popitem()  # Remove the last item

# Check => To ways to check if a key exist
if "key" in mydict:
    print(True)

try:
    mydict["key"]
except KeyError:
    print("Key not found")

# loop

for key in mydict:
    print(key)

for key in mydict.keys():
    print(key)

for value in mydict.values():
    print(value)

for (key, value) in mydict.items():
    print(key, value)

# Copy
mydict_copy = mydict.copy()
mydict_copy = dict(mydict)

# Update
my_dict = {"name": "John", "age": 30}
my_dict2 = {"City": "New York"}

my_dict.update(my_dict2)  # => my_dict2 overrides same keys in the mydict

# Index

# We can change the index of the dict
my_dict = {3: 9, 6: 36, 9: 81}  # this replace the normal index of the dict
value = my_dict[3]

# We can use tuple as key
mytyple = [8, 7]
mydict = {myTuple: 15}

# SETS
# Collection data type unordered, mutable, and changeable
# It does not allow duplicate values

myset = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
myset = set([1, 2, 3, 4, 5, 6])  # => {1, 2, 3, 4, 5, 6}
myset = set("Hello")  # => {'H', 'e', 'l', 'o'}

# To create a empty set, we hace to do it with the code word
myset = set()

# Add
myset.add(1)

# Remove
myset.remove(1)
myset.discard(1)  # If the value is not in the set, it will not throw an error
myset.clear()  # Remove all elements
randomElement = myset.pop()  # Remove a random element

# Iterate
for item in myset:
    print(item)

# Check
if 1 in myset:
    print(True)

# Union & Intersection
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

# Union combines elements from both sets without dupplication
u = odds.union(evens)  # => {1, 3, 5, 7, 9, 0, 2, 4, 6, 8}

# Interseccion combines elements that are found in both sets
i = odds.intersection(evens)  # => {}
a = evens.intersection(primes)  # => {2}

# Difference => Elements in the first set but not that matches in the second set
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}
diff = setA.difference(setB)  # => {1, 2, 3}

# Symetric Difference => All elements that the sets don't have in common
symetricDiff = setA.symmetric_difference(setB)  # => {1, 2, 3, 6, 7, 8}

# This methods modified the original set
# Interseccion Update => Update the first set with the elements that are in both sets
setA.intersection_update(setB)  # => {4, 5}

# Difference update
setA.difference_update(setB)  # => {1, 2, 3}

# Symetric Difference update
setA.symmetric_difference_update(setB)  # => {1, 2, 3, 6, 7, 8}

# Update
setA.update(setB)  # => {1, 2, 3, 4, 5, 6, 7, 8}

# Subset
setA.issubset(setB)  # => True

# Superset
setA.issuperset(setB)  # => False

# Disjoint
# => False # There is no common elements between the sets
setA.isdisjoint(setB)

# Copy
setA_copy = setA.copy()
setB = set(setA)

# FROZEN SET => Immutable Set

a = frozenset([1, 2, 3, 4, 5])

# STRINGS => Collection Ordered and inmutable data type used for text

name = "John"
my_string = "Hello World"
my_string = 'Hello World'
my_string = "i'm word"
my_string = """ Hello World """  # Multiline string
my_string = r"Hello World"  # Raw string
my_string = f"Hello World {name}"  # Formatted string

# Access
char = my_string[0]  # => 'H'

# Slicing
my_string[0:5]  # => 'Hello'

# Contact
my_string + " " + name  # => 'Hello World John'
my_string = f"Hello Word {name}"

# Loop
for char in my_string:
    print(char)

# Check
if "e" in my_string:
    print("e is in the string")

# Whitespace
my_string = my_string.strip()  # Remove whitespace
my_string = my_string.lstrip()  # Remove whitespace from the left
my_string = my_string.rstrip()  # Remove whitespace from the right

# Lower
my_string.lower()  # => 'hello world'

# Upper
my_string.upper()  # => 'HELLO WORLD'

# Start
my_string.startswith("Hello")  # => True

# End
my_string.endswith("World")  # => True

# Index
my_string.find("e")  # => 1

# Count
my_string.count("l")  # => 3

# Replace
my_string.replace("World", "Universe")  # => 'Hello Universe'

# Convert to List
my_list = list(my_string)  # => ['H', 'e', 'l', 'l', 'o']
# => ['Hello'] By default split search for whitespace
my_list = my_string.split()

# Convert back to string
# Before the dot we put what we what as separator # => 'Hello'
new_string = "".join(my_list)

# Making a word
my_list = ['a'] * 6
my_string = "".join(my_list)  # => 'aaaaaa'

# We can check how much time takes a operation to execute

start = timer()
my_string = ''
for i in range(10000000):
    my_string += 'a'

stop = timer()

start = timer()
my_string = ''.join(['a'] * 10000000)
stop = timer()

# Formatting string

# Very old format
var = "Tom"  # %s is for string, %d is for number, %f is for float
var2 = 6.123456
my_string = "The variable is %s" % var

# Not so old format
my_string = "The variable is {} and {}".format(var, var2)

# Newest format
# Evaluate what is inside {} at runtime, we can put expressions inside the {}
my_string = f"The variable is {var} and {var2}"

# COLLECTIONS

# Container data type : Counter, NamedTuple, OrderedDict, DefaultDict, Deque

# Counter

# from collections import Counter

# Create a dict with the count as values and the elements as keys

a = ['a'] * 5
my_counter = Counter(a)  # => Counter({'a': 5})

# Most Common => Returns a tuple
my_counter.most_common(2)  # => [('a', 5), ('a', 5)]

# Elements => Returns a list
my_counter.elements()  # => {'a', 'a', 'a', 'a', 'a'}

# Named Tuple => Easy to create and lightweight object type
# from collections import namedtuple

# This will create a class named Point with the fields x,y
Point = namedtuple('Point', ['x', 'y'])
pt = Point(1, 2)
print(pt.x, pt.y)  # => 1 2

# OrderedDict => Regular Dict but with order


orderec_dict = OrderedDict()
orderec_dict['a'] = 1
orderec_dict['b'] = 2
orderec_dict['c'] = 3
# orderec dict => {'a':1, 'b':2, 'c':3}

# Default Dict
# from collections import defaultdict # The difference is that the default value is not None

defaultDict = defaultdict(int)  # As argument we have to pass a type

# Deque
# from collections import deque # A double-ended queue we can add elements to the start and end

d = deque()
d.append(1)
d.append(2)

d.appendleft(3)
d.appendright(4)

d.pop()
d.popleft()

d.clear()

d.extend([1, 2, 3])
d.extendleft([4, 5, 6])

d.rotate(2)  # Takes negative values to rotate to the left

# ITERTOOLS => Data types that we can use in loops, this library help us to iterate over data structures

# from itertools import product

a = [1, 2]
b = [3, 4]
prod = product(a, b, repeat=2)  # => ((1, 3), (1, 4), (2, 3), (2, 4))
print(prod)  # => <itertools.product object at 0x7f8b8b8b9c18>
print(list(prod))  # => [(1, 3), (1, 4), (2, 3), (2, 4)]

# from itertools import permutations => Return all possible orderings of an input
perm = permutations(a)
list(perm)  # => [(1, 2), (2, 1)]

# from itertools import combinations => makes all possible combinations with the especified lenght no dupplicates

comb = combinations(a, 2)  # => ((1, 2), (2, 1))

# combinations_with_replacement, in this dupplicates
# => ((1, 1), (1, 2), (1, 2), (2, 2), (2, 2))
comb_wr = combinations_with_replacement(a, 2)

# accumulated => Return an iterator that yields the accumulated results of calling the function with the previous result

# from itertools import accumulate
a = [1, 2, 3, 4]
acc = accumulate(a)
print(acc)  # => [1, 3, 6, 10]

# import operator
acc_op = accumulate(a, func=max)  # returns the max
print(acc_op)  # => [1, 2, 3, 4]

# groupby => Return an iterator that groups elements in tuples
# from itertools import groupby


def samller_than_3(x):
    return x < 3


a = [1, 2, 3, 4, 5, 6, 7]
group_obj = groupby(a, key=samller_than_3)

for key, value in group_obj:
    print(key, list(value))  # => True [1, 2] False [3,4,5,6,7,8,9]


person = [{'name': 'Tim', 'age': 35}, {'name': 'Jorge', 'age': 33}]


group_obj = groupby(person, key=lambda x: x['age'])

for key, value in group_obj:
    # => 35 [{'name': 'Tim', 'age': 35}] 33 [{'name': 'Jorge', 'age': 33}]
    print(key, list(value))

# INFINITE ITERATORS

# COUNT

for i in count(18):
    if i == 15:
        break

# CyCLE

a = [1, 2, 3]

for i in cycle(a):
    print(i)

# Repeat

for i in repeat(1, 5):  # for i in repeat(value, stopRepeticion)
    print(i)


# LANDA IS A FUNCTION THAT RETURNS A FUNCTION
# IS a small one line anonymous functions

# lambda arguments: expression => This will create some functions, evaluate the expression and return it

def add10(x): return x + 10


lambda x: x + 10


def mult(x, y): return x * y


lambda x, y: x * y

# This functions are use when you need a simple function that is used only once in the code
# Or as an argument to another function or higher order function

# Sorted With lambda

points20 = [(1, 2), (15, 1), (6, -1), (10, 4)]
points20_sorted = sorted(points20)
# => [(1, 2), (6, -1), (10, 4), (15, 1)]

# => [(1, 2), (6, -1), (10, 4), (15, 1)]
points20_sorted = sorted(points20, key=lambda x: x[1])

points20_sorted = sorted(points20, key=lambda x: x[0] * x[1])

# map

# map(function, iterable) => Return an iterator that applies the function to each item of the iterable
a = [1, 2, 3, 4, 5]
b = map(lambda x: x * 2, a)  # => [2, 4, 6, 8, 10]
c = [x * 2 for x in a]  # => [2, 4, 6, 8, 10]
print(list(b))

# filter(function, iterable) => Return an iterator that filters the iterable by the function
a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x % 2 == 0, a)  # => [2, 4, 6]
c = [x for x in a if x % 2 == 0]  # => [2, 4, 6]

# reduce(function, iterable) => Return a single value by calling the function with the first two items of the iterable
# and the result of the function with the next two items

a = [1, 2, 3, 4, 5, 6]

product_a = reduce(lambda x, y: x * y, a)
# => 720

# Errors

# 1 Syntax Error => The syntax is wrong
# 2 Name Error => The name is wrong
# 3 Type Error => The type is wrong
# 4 Index Error => The index is wrong
# 5 Key Error => The key is wrong
# 6 Value Error => The value is wrong
# 7 Attribute Error => The attribute is wrong
# 8 Import Error => The import is wrong
# 10 Tab Error => The identation is wrong

# EXCEPTIONS
# A python program inmediately stops when an exception is raised

# To raise an exception
x = -5
if x < 0:
    raise Exception('X should be positive')

# Assert statement
assert(x > 0), 'X should be positive'

# Catch Exceptions
try:
    x = -5 / 0
except ZeroDivisionError:
    print('Error')
except TypeError as e:
    print(e)
else:  # [OPTIONAL]  # => This runs if no exception is raised
    print('No error')
finally:  # [OPTIONAL]  # => This runs always
    print('cleaning up...')


# Is good practice to catch the specific exception
# TYPES OF EXCEPTIONS
# Exception
# BaseException
# ArithmeticError
# ZeroDivisionError
# AssertionError
# AttributeError
# EOFError
# FloatingPointError
# GeneratorExit
# ImportError
# IndentationError
# IndexError
# KeyError
# KeyboardInterrupt
# MemoryError
# NameError
# NotImplementedError
# OSError
# OverflowError
# ReferenceError
# RuntimeError
# StopIteration
# SyntaxError

# Define our own exception

class ValueTooHighError(Exception):
    pass


class ValueTooLowError(Exception):
    def __init__(self, message, value):
        super().__init__(message)
        self.value = value


def test_value(x):
    if x > 10:
        raise ValueTooHighError('Value is too high')


try:
    test_value(11)
except ValueTooHighError as e:
    print(e)

# LOGGING
# import logging

# Example config
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

# Create Logger

# import logging

logger = logging.getLogger('MyLogger')

# create handler
stream_h = logging.StreamHandler()  # StreamHandler() => Prints to the console
# file handler
file_h = logging.FileHandler('myProgramLog.txt')

stream_h.level = logging.DEBUG
file_h.level = logging.WARNING

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

# Investigate logging.config
# when we have set the config file
# in our file we do
# import logging.config
# logging.config.fileConfig('logging.conf')

# we can use also a dict config

# JSON
# import json

person = {'name': 'John', 'age': 30}

# Create a JSON STRING
personJSON = json.dumps(person, indent=4, sort_keys=True)

# DUMP THE JSON IN A FILE
with open('person.json', 'w') as file:
    json.dump(person, file)

# Decode the JOON
person = json.loads(personJSON)

# LOAD THE JSON FROM A FILE
with open('person.json', 'r') as file:
    person = json.load(file)

# Creating our personal encoding


def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age}

#

# RAMDON NUMBERS


# Random module
# import random => The numbers sims random but they are not entirely

random.seed(1)  # => Set the seed [OPTIONAL]

a = random.random()  # => This will return a random number between 0 and 1
# => This will return a random number between 1 and 10
a = random.uniform(1, 10)
# => This will return a random number between 1 and 10 The upperbound is included
a = random.randint(1, 10)
# => This will return a random number between 1 and 10. The upperbound not inlcued
a = random.randrange(1, 10, 2)
# => This will return a random number with a normal distribution
a = random.normalvariate(1, 2)

# Sequences
mylist = list("ABCDEFGHR")
a = random.choice(mylist)  # => This will return a random element from the list
a = random.sample(mylist, 3)  # => This will return a list of 3 random elements
# => This will return a list of 3 random elements. This will include the same element
a = random.choices(mylist, k=3)
a = random.shuffle(mylist)  # => This will shuffle the list

# This numbers are reproducible, that is way the call pseudorandom numbers
# They are not recommended to use in security

# SECRET MODULE
# import secrets

# => This will return a random number between 0 and 9
a = secrets.randbelow(10)

a = secrets.randbits(5)  # => This will return a random number with 5 bits

mylist = list("ABCDEFGHR")
# => This will return a random element from the list
a = secrets.choice(mylist)

# If you are working with arrays you can use numpy
# NUMPY
# import numpy as np

# => This will return a array with 3 ramdon number between 0 - 1
a = np.random.rand(5, 5)

# => This will return a array with 3 ramdon number between 1 - 10
a = np.random.randint(1, 10, {3, 3})

a = np.array([1, 2, 3], [3, 4, 6])  # => [[1,2,3],[3,4,6]]

np.random.shuffle(a)  # => This will shuffle the array only in the x axis

# DECORATORS
# There are two types of decorators : function and class


@mydecorator  # => This is a function decorator
def dosomething(func):
    def wrapper():
        print('Doing something before')
        func()
    return wrapper

# Is a function that takes another function as argument
# and extends the behavior of the function without modifying it
# Functions in python are first class objects. They can be passed as arguments. They can be pass as argument, functions can be returned from functions, and they can be returned from classes.


def start_end_decorator(func):
    def wrapper():
        print('Starting')
        func()
        print('Ending')
    return wrapper


@start_end_decorator  # => This is a function decorator
def print_name():
    print('John')


# This represent the @start_end_decorator
# print_name = start_end_decorator(print_name)

# import functools

# TEMPLATE FOR A NICE DECORATOR
def start_end_decorator(func):
    # => this help python knows who is the decorator and who is the function
    @functools.wraps(func)
    def wrapper(*args, **kwargs):  # This is a function that takes arguments
        print('Starting')  # This executes before the function
        result = func()  # If we want the result to the function that we apply the decorator
        print('Ending')  # This executes after the function
        return result
    return wrapper


@start_end_decorator
def add(x):
    return x + 1

# Decorator can take arguments


def repeat(num_times):  # When the decorator takes arguments, we have to wrap the decorator inside another function
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat


@repeat(num_times=3)
def greet(name):
    print(f'Hello {name}')

# We can stak decorator, and have nested decorators


def debug(func):
    def wrapper(*args, **kwargs):
        print(f'You are in the debug mode')
        result = func(*args, **kwargs)
        print(f'You are out of the debug mode')
        return result
    return wrapper


@debug  # First execute this. func inside debug decorator is calling start_end_decorator
# Inside the first decorator we execute this. func inside this decorator is calling say_hello
@start_end_decorator
def say_hello(name):  # Inside the start_end_decorator we execute this
    greeting = f'Hello {name}'
    print(f'Hello {name}')

# CLASS DECORATOR


class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    # We implement this inside class decorator. This is the same as the inner function in the function decorator
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'Call {self.num_calls} of {self.func.__name__}')
        return self.func(*args, **kwargs)


@CountCalls
def say_hello_class(name):
    greeting = f'Hello {name}'
    print(f'Hello {name}')

# USE CASES
# Implement timer decorator => Time how long it takes to execute a function
# Implement debug decorator => add more information to the function
# Implement check decorator => check if some arguments are allright
# etc


# GENERATORS => Generators are functions that can be iterated over.

def mygenerator():  # The generator writes likes a normal function but instead of using return, use yield
    yield 1
    yield 2
    yield 3


g = mygenerator()  # We have to create our generator object

for i in g:
    print(i)  # => 1 2 3

# (This is the same as g.next()) . This executes the funciton until encounters the first yield
value = next(g)  # => 1

value = next(g)  # => 2

# We can use it as input in another function
print(sum(g))  # => 6

sorted(g)  # => [1, 2, 3]


def countdown(n):
    print('Starting')
    while n > 0:
        yield n
        n -= 1
    print('Done')


cd = countdown(5)  # We have to create our generator object

value = next(cd)  # => Starting
print(value)  # => 5
value = next(cd)  # => 4
value = next(cd)  # => 3
value = next(cd)  # => 2
value = next(cd)  # => 1
value = next(cd)  # => Done

# They save a lot of memory when you work with large data


def fibonnacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


fib = fibonnacci(100)
for i in fib:
    print(i)

mygenerator = (i for i in range(10) if i % 2 == 0)  # Even numbers

for i in mygenerator:
    print(i)

print(list(mygenerator))  # => [0, 2, 4, 6, 8]


# Is similar to list comprehension
# List comprehension is with []
# Generator is with ()


# THREADING AND MULTIPROCESSING

# Process = An instance of a program (ej a Python Interpreter)
#         - Takes andavantage of multiple CPUs and cores
#         - Separate memory space -> Memory is not shared between processes
#         - Great for CPU-bound processing
#         - New process is started independently from other processes
#         - Processes are interruptable/Killable
#         - One GIL (Global Interpreter Lock) for each process -> avoids GIL limitation
#
#         CONS:
#         - Heavy weight
#         - Startin a process is slower than starting a thread
#         - More Memory
#         - IPC (Inter-Process Communication) is more complicated


# Thread = A lightweight process that can be scheduled to run in parallel with other processes
#         - An entity within a process that can be scheduled
#         - A process can spawn multiple threads
#         - All treads within a process share the memory
#         - Startin a thread is faster than starting a process
#         - Great for I/O-bound tasks -> I/O(Input/Output)
#
#         CONS:
#         - Threading is limited by GIL: Only one thread at a time
#         - No effect for CPU-bound tasks
#         - Not interruptable/Killable
#         - Careful with race conditions -> When two or more thread want to modify the same variable at the same time

# GIL = Global interpreter lock
#       - A lock that allows only one thread at a time to execute in Python
#       - Needed in CPython because memory management is not thread-safe

#       - Avoid Lock:
#             - Use multiprocessing
#             - Use a different, free-threaded Python implementation (Jython, IronPython)
#             - Use Python as a wrapper for third-party libraries (C/C++ -> numpy, scipy)

# from multiprocessing import Process
# import os


def square_number(n):
    print(f'Square of {n} is {n * n}')


process = []
num_processes = os.cpu_count()  # -> a good number of processes is the number of cpu

# create Processes
for i in range(num_processes):
    p = Process(target=square_number, args=(i,))
    process.append(p)

# start each proccess
for p in process:
    p.start()

# join -> i want to wait until all processes are done and block the main thread
for p in process:
    p.join()


# MultiThreading is with the functions that proccess, the difference is for create a thred
# we have to do Thread(target=square_number, args=(i,))

# from threading import Thread, Lock

def square_number_thread(n):
    print(f'Square of {n} is {n * n}')


if __name__ == '__main__':
    thread = []
    num_threads = 10

    for i in range(num_threads):
        t = Thread(target=square_number_thread, args=(i,))
        thread.append(t)

    for t in thread:
        t.start()

    for t in thread:
        t.join()

# Share data between threads

database_value = 0


def increase(lock):
    global database_value  # -> make a variable accesible for all thread

    lock.acquire()  # -> lock the variable
    local_copy = database_value

    # proccessing
    local_copy += 1

    database_value = local_copy
    lock.release()  # -> unlock the variable


def increase2(lock):
    global database_value

    with lock:  # -> with is a context manager, that allows us to use the lock as a context manager. And functions equall to the first increase
        local_copy = database_value
        local_copy += 1
        database_value = local_copy


if __name__ == '__main__':
    lock = Lock()  # This help us avoid race conditions, we use it to lock variables so two threads can access to the same time

    thread = []
    num_threads = 10

    print('Start Value', database_value)  # -> 0

    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print('end value', database_value)  # -> end value is 2

    print('end main')

# from queue import Queue

# queue -> FIFO (First In First Out)

q = Queue()

q.put(1)
q.put(2)
q.put(3)

first = q.get()  # -> get and remove the first item

q.empty  # -> return true if the queue is empty

q.task_done()  # -> tell the queue that the task is done

q.join()  # -> wait until all tasks are done


def worker(q, lock):
    while True:
        value = q.get()  # q.get is thread-safe
        with lock:
            print(f'In {current_thread().name} got {value}')
        q.task_done()


if __name__ == '__main__':
    q = Queue()

    num_threads = 10

    lock = Lock()

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock))
        thread.daemon = True  # -> The daemon thread dies when the main thread dies
        thread.start()

    for i in range(1, 21):
        q.put(i)  # q.put is thread-safe

    q.join()

    print('end main')

# Functions Parameters

# Parameter - Are the variables that are passed to the function
# Arguments - Are the values that are passed to the function


def print_name(parameter):
    print(f'{parameter}')


print_name(arguments)


def foo(a, b, c):
    print(a, b, c)


# Positional Arguments -> The order matters
foo(1, 2, 3)

# Key arguments -> The order does not matter
foo(a=1, c=3, b=2)

# We can mixup positional and key arguments, but after a key argument we can not use positional arguments


# Default Parameters -> Must be at the end of the parameter list
def foo(a, b, c, d=4):
    print(a, b, c, d)

# If we mark parameter with one star, we can pass any number of positional arguments
# If we mark parameter with two stars, we can pass any number of key arguments.


def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f'{key} = {value}')


def foo(a, b, *, c, d):
    print(a, b, c, d)


foo(1, 2, c=3, d=4)


def foo(a, b, c):
    print(a, b, c)


my_list = [0, 1, 2]
foo(*my_list)  # Like destructuring in javascript

my_dict = {'a': 1, 'b': 2, 'c': 3}
foo(**my_dict)  # Like destructuring in javascript
# The lenght of the dict and the name of its properties has to be equal to the parameters that are expected in the function

# ASTERISK OPERATOR

# Multiplications
result = 5 * 7  # -> 35

# Power operation
result = 2 ** 3  # -> 8

# Create List, Tuples or String with repetead elements
mylist = [0] * 5  # -> [0, 0, 0, 0, 0]
mylist = [0, 1] * 5  # -> [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

mytuple = (0, 2) * 5  # -> (0, 2, 0, 2, 0, 2, 0, 2, 0, 2)

mystring = 'AB' * 3  # -> 'ABABAB'

# ARGS -> The arguments that are passed to the function


def a(*args):  # -> args is a tuple
    print(args)


a(1, 2, 3, 4, 5, 6)  # => args = (1,2,3,4,5,6)

# KWARGS -> The key arguments that are passed to the function


def k(**kwargs):  # -> kwargs is a dict
    print(kwargs)


k(a=1, b=2, c=3)  # => kwargs = {'a': 1, 'b': 2, 'c': 3}

# ARGUMENT UNPACKING


def foo(a, b, c):
    print(a, b, c)


# The lenght of the list has to be equal to the number of parameters that are expected in the function
my_list = [0, 1, 2]
foo(*my_list)  # -> foo(0, 1, 2)

my_tuple = (0, 1, 2)
foo(*my_tuple)  # -> foo(0, 1, 2)


# The lenght of the dict and the name of its properties has to be equal to the number of parameters that are expected in the function
my_dict = {'a': 1, 'b': 2, 'c': 3}
foo(**my_dict)  # -> foo(a=1, b=2, c=3)

# UNPACKING CONTAINERS

my_list = [1, 2, 3, 4, 5, 6]
*beginning, last = my_list  # -> beginning = [1, 2, 3, 4, 5] and last = 6
# beginning comes as a list
# last comes as a single value

my_tuple = (1, 2, 3, 4, 5, 6)
*beginning, last = my_tuple  # -> beginning = (1, 2, 3, 4, 5) and last = 6
# beginning comes as a list
# last comes as a single value

# MERGE LIST, TUPLES AND SET
my_tuple = (1, 2, 3, 4, 5, 6)
my_list = [7, 8, 9]
my_set = {10, 11, 12}

# new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
new_list = [*my_tuple, *my_list, *my_set]

# MERGE DICT
dict_a = {'a': 1, 'b': 2, 'c': 3}
dict_b = {'d': 4, 'e': 5, 'f': 6}

# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
my_new_dict = {**dict_a, **dict_b}

# CONTEXT MANAGER
# The context manager is a special type of function that can be used to create a context.

# with context help us to close the file when we leave the block
with open('notes.txt', 'w') as f:
    f.write('Hello World!')

# THIS BELOW BLOCK OF CODE IS THE SAME THAT THE UPPER WITH THE "WITH"
file = open('notes.txt', 'w')
try:
    file.write('Hello World!')
finally:
    file.close()

# CON EL OPERADOR WITH LLEVA MENOS LINEAS Y NOS AHORRA EL TRABAJO DE
# TENER QUE ACORDARNOS DE CERRAR EL ARCHIVO

# otro tipico uso es para abrir y cerrar base de datos
# otro es para usar el modulo lock

# Create our owns context manager


class ManagedFile:  # -> Context Manager
    def __init__(self, filename):
        self.filename = filename

    # This will be called when we use the with statement
    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file

    # This will be called when we leave the with statement
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with ManagedFile('notes.txt') as f:
    f.write('Hello World!')

# Also we can implement it as a function
# from contextlib import contextmanager


def managed_file(filename):
    f = open(filename, 'w')
    try:
        # INSIDE OF THE TRY WE WRITE ALL OF GOES INSIDE A __ENTER__ METHOD
        yield f  # when you yield, the execution will stop and the file will be returned
    finally:
        # INSIDE OF THE TRY WE WRITE ALL OF GOES INSIDE A __EXIT__ METHOD
        f.close()


with managed_file('notes.txt') as f:
    f.write('Hello World!')

# We can also use the context manager as a decorator


@contextmanager
def managed_file(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()


# PATTERN MATCHING SWITCH

# IN PYTHON 3.10 WE CAN USE THE RESERVED WORD MATCH LIKE SWITCH IN PHP

""" def http_error(status):
    match status:
        case 400:
            print('Bad Request')
        case 404:
            print('Not Found')
        case 401 | 403:
            print('Internal Server Error')
        case _:
            print('Unknown Error') """

# We can match with a tuples, set, objects


""" def matchTest(data):
    match data:
        case (1, 2, 3):
            print('Tuple')
        case {1, 2, 3}:
            print('Set')
        case {'a': 1, 'b': 2}:
            print('Dict')
        case 'a':
            print('String')
        case 1:
            print('Number')
        case True:
            print('Boolean')
        case None:
            print('None')
        case _:
            print('Default') """

# PARENTHIZED CONTEXT MANAGER


""" with (ContextManager1() as ctx1, ContextManager2() as ctx2, ContextManager3() as ctx3,):
    pass """

# We can enclose multiple context manager inside a parenthesis

# STRICT ARGUMENT FOR ZIP METHODS

names = ['Max', 'John', 'Mark']
ages = [22, 26]

result = zip(names, ages)  # -> result = [('Max', 22), ('John', 26)]

# -> result = ERROR IF THE TWO ITERABLES DON?T HAVE THE SAME LENGHT
result = zip(names, ages, strict=True)

# NEW TYPING FEATURES


def square(number: int | float) -> int | float:
    return number * number


isinstance(1, int | str)  # -> True

# MODULES, PACKAGES AND IMPORTS

# A MODULE IS CREATED WHEN A PYTHON SOURCE FILE IS CREATED
# MODULES NAME HAS TO START WITH A LETTER, AND ALL THE LETTERS HAS TO BE LOWERCASE


# IF WE ARE IN THE SAME FOLDER OF THE MODULE WE JUST CREATED, WE CAN IMPORT IT
# IN OTHER FILE JUST DOING

# import file_name

# ALSO WE CAN IMPORT SPECIFIC FUNCTIONS FROM THE MODULE

# from file_name import function_name

# WHEN THE MODULES ARE IMPORTED, THEY ONLY GET IMPORTED ONCE

# PACKAGES ARE LARGER COLLECTIONS OF CODE/MODULES

# TO MAKE A PACKAGE WE HAVE TO PUT OUR MODULES IN THE SAME FOLDER
# AND THE NAME OF THAT FOLDER, BECAMES THE NAME OF THE PACKAGE
# ALSO WE HAVE TO CREATE A __INIT__.PY FILE IN THAT FOLDER

# THE SUBSEQUENT FOLDERS OF THE MAIN PACKAGES ARE "INDEPENDENT" PACKAGES
# GOOD PRACTICES DICTATED THAT WE HAVE TO PUT AN EMPTY
# __INIT__.PY FILE IN EACH PACKAGE / DIRECTORY

# TO IMPORT A SUBPACKAGE WE HAVE TO USE THE DOT NOTATION

# Folder1
#     __init__.py
#     function.py
#     Folder2
#       __init__.py
#       function2.py
#
#
# import Folder1.Folder2.function2
#
#
#
# ABSOLUTE IMPORTS
#   import Folder1.Folder2.function2
# RELATIVE IMPORTS
#   from .Folder2 import function2 WE CAN THINK IT LIKE A PATH
# IF WE PUT A DOT BEFORE FOLDER2 THAT IS MEANING THAT WE ARE LOOKING IN THE SAME DIRECTORY
# IF WE PUT TWO DOT BEFORE FOLDER2 THAT IS MEANING THAT WE ARE LOOKING IN THE PARENT DIRECTORY
