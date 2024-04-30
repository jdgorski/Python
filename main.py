# # # #order of execution
# # # # in python

# # # print("Hellow World")
# # # # strings are surrounded by quotes
# # # # sing or double quotes '' or ""
# # # print("order of execution")

# # # print("in python")
# # # print("*"*20)
# # # #variables are used to store data
# # # # variables are created when you assign a value to it
# # # #variables are case sensitive
# # # price = 10 #integer variable
# # # # name = "John" #string variable
# # # # rating = 4.9 #float variable
# # # # is_published = True #boolean variable
# # # # #start all variables with a lower case letter or underscore
# # # # # use camel case if you want to start with a capital letter
# # # # # on the next word
# # # # playerBulls = "michael jordan"
# # #Concatentation to join variables in a sentence
# # # print(name + " is a basketball player")
# # # # print(name + "has a rating of " + str(rating))
# # # # #use the str() function to convert a number to a string
# # # # #the plus (+) sogn is used to concatenate strings
# # # personName = input("What is your name? ")
# # # favoriteColor = input("What is your favorite color? ")
# # # print(personName + )


# # # create variables for the following :
# # age = 25
# # name = "John"
# # song = "Happy Birthday"
# # food = "bananas"
# # number = 100
# # print("")


# #what does the + sign do? What is it called?

# print(f'the length of the phrase  {len(phrase)}')
# declarationOfIndependance = "The unanimous Declaration of the thirteen united States of America, When in the Course of human events, it becomes necessary for one people to dissolve the political bands which have connected them with another, and to assume among the powers of the earth, the separate and equal station to which the Laws of Nature and of Nature's God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation."
# print(f'the length of the Declaration Of Independance is  {len(declarationOfIndependance)}')
# declarationOfIndependance = str(declarationOfIndependance)

# # len is used to find the length of the phrase



# #what if I wanted to get the length of a phrase?


# #what if I wanted to make the letters in the variable upper case or lower?




# #what if I wanted to check and see if the phrase was all lower or upper?


# #What if I wanted to get one letter of the phrase


# # The names you use when creating these labels need to follow a few rules:
# # 1. Names can not start with a number.
# # 2. There can be no spaces in the name, use _ instead.
# # 3. Can't use any of these symbols :'",<>/?|()!@#$%^&*~-+
# # 4. It's considered best practice (PEP8) that names are lowercase.
# # 5. Avoid using the characters 'l' (lowercase letter el), 'O' (uppercase letter oh), or 'I' (uppercase
# # letter eye) as single character variable names.



# # Working with numbers bold text
# # We'll learn about the following topics:
# # 1. Types of Numbers in Python
# # 2. Basic Arithmetic
# # 3. Differences between classic division and floor division


# # Addition

# # Subtraction

# # Multiplication

# # Division

# # Modulus

# # Exponentiation

# # Floor Division

# # Order of Operations followed in Python

# # You can use parentheses to specify the order in which you want operations to be performed.

# #to do more you need to import special math libraries from python
# #from math import *
# #this goes out and grabs some different math functions we can use
# #floor method
# #ceil method
# #sqrt method
# from math import * #import everything
# print(floor(95.76666))
# print(ceil(98.3333))
# print(sqrt(54))


# # Python has various "types" of numbers (numeric literals).
# # 1. We'll mainly focus on integers and floating point numbers. Integers are just whole numbers,
# # positive or negative. For example: 2 and -2 are examples of integers.
# # 2. Floating point numbers in Python are notable because they have a decimal point in them, or
# # use an exponential (e) to define the number. For example 2.0 and -2.1 are examples of
# # floating point numbers. 4E2 (4 times 10 to the power of 2) is also an example of a floating
# # point number in Python.



# # challenge exerces... 
# #create a program that asks for the user's name and age and then prints out the user's name and age

# # create a program that asks for the user's name and then prints out the user's name in all caps

# # create a program that asks for the user's name and then prints out the user's name in all lower case

# # create a program that asks for price and then prints out the price with a 10% discount

# # Given the phrase "Hancock High School", perform the following operations:
# # Print the phrase with a newline character to separate "Hancock" and "High" and "School".
# # Concatenate the phrase with " is cool", and print the result.
# # Print the length of the phrase.
# # Convert and print the phrase in uppercase and lowercase.
# # Check if the phrase is all lower or all upper and print the result.
# # Print the first and the last letter of the phrase.

new_phrase = "welcome to day 2 part 3"
print(len(new_phrase))
print(new_phrase.upper())
#.upper makes the phrase all UPPERCASE
print(new_phrase.lower())
# .lower makes the phrase all lowercase
print(new_phrase[0]) 
# the [0] prints the first letter of the phrase
print(new_phrase[1])
print(new_phrase[2])
print(new_phrase[11])
#Addition
print(2 + 2)
# Subtraction
print(2-5)
# Division
print(10/3)
# Modulus
print(10%3)
# Exponentation
print(2**3)
# Floor Division
print(10//3)
# Order of Operations
print(2*3+1)

