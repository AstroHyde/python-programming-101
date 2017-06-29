#!/usr/bin/python
#Example python script
#GA Python 101
#E.A. Hyde 2017
#use the hash key to make comments that will make your code more readable to humans, these lines will not be compiled in the python compiler

#import statements will load in packages
import sys

#The following line of the program displays the prompt, the statement saying “Press the enter key to exit”, and waits for the user to take action −

input("\n\nPress the enter key to exit.")

#This next line will output a simple print statement

print("Hello, Python!")

#Here are some variable types in Python
counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
name    = "John"       # A string

#What are strings?
#Strings in Python are identified as a contiguous set of characters represented in the quotation marks.
str = 'Hello World!'

print(str)          # Prints complete string
print(str[0])       # Prints first character of the string
print(str[2:5])     # Prints characters starting from 3rd to 5th
print(str[2:])      # Prints string starting from 3rd character
print(str * 2)      # Prints string two times
print(str + "TEST") # Prints concatenated string

#How about lists?
#Lists are the most versatile of Python's compound data types. A list contains items separated by commas and enclosed within square brackets ([]).

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print(list)          # Prints complete list
print(list[0])       # Prints first element of the list
print(list[1:3])     # Prints elements starting from 2nd till 3rd 
print(list[2:])      # Prints elements starting from 3rd element
print(tinylist * 2)  # Prints list two times
print(list + tinylist) # Prints concatenated lists

#Now for the strange sounding type...
#What is a tuple?
#A tuple is another sequence data type that is similar to the list. A tuple consists of a number of values separated by commas. Unlike lists, however, tuples are enclosed within parentheses.

#The main differences between lists and tuples are: Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed, while tuples are enclosed in parentheses ( ( ) ) and cannot be updated. Tuples can be thought of as read-only lists. 

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print(tuple)           # Prints complete list
print(tuple[0])        # Prints first element of the list
print(tuple[1:3])      # Prints elements starting from 2nd till 3rd 
print(tuple[2:])       # Prints elements starting from 3rd element
print(tinytuple * 2)   # Prints list two times
print(tuple + tinytuple) # Prints concatenated lists


#How about a more complicated type... a dictionary can store several types in one area. Python's dictionaries are kind of hash table type. They work like associative arrays or hashes found in Perl and consist of key-value pairs. A dictionary key can be almost any Python type, but are usually numbers or strings. Values, on the other hand, can be any arbitrary Python object.

#To access dictionary elements, you can use the familiar square brackets along with the key to obtain its value.

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])
