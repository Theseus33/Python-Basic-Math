# + addition
# - subtraction
# * multiplication
# / division
# ** exponent
# % modulo
# // integer division

# Variables and Datatypes
# a variable in python works just like in math where the variable needs to be assigned first 

num_of_cats = 99

num_of_cats

#Variable Assignment
# variables can be: assigned to other variables, reassigned at any time.

#Variable Restrictions

1. Must start with a letter or underscore.
2. The  rest of the name must consist of letters, numbers, or underscores.
3. Names are case sensitive.

#Standard Style Conventions

1. Most variables shoudl be snake_case (underscore between words)
2. Most vairables should also be lowercase, with some exceptions
    ie: CAPITAL_SNAKE_CASE usually referes to contansts (eg Pi = 3.14)
        UpperCamelCase usually refers to a class
3. Variables that start and end with two underscores (called "dunder" ) are supposed to be private
or left alone
    ie: __dont_touch__

#Data Types Overview

1. Booleans (True/False)
2. Intergers (1,2,3)
3. Strings (a sequence of unicode or characters)
4. Lists (an ordered sequence of values of other data types)
5. Dictionary (a collection of key:value pairs)

#Dynamic Typing
Python is highly flexible about reassigning variables to different types. Varibales can change 
values as well as types.

awesomeness = True (Boolean)
awesomeness = "a dog" (String)
awesomeness = None (special value)
Awesomeness = 22 / 7 (float)

# The Special Value None
needs a capital "N" - None
represents nothingness in python
similar to Null in other languages

#Declaring Stings
String literals in Python can be decalared wit heither single or double quotes but be consistant!

#String Escape Characters/Sequences
In Python there are also "escape characters", which are "metacharacters" - they get interpreted by
Python to do something special:

All escape characers start with a backslash "\"
new_line = "hello \n world"
print(new_line)

returns the following 
#hello
#world

so if you actually want a backslash you need \\ or else Python will think its the start of an escape char

#String Concatenation
Concatenation is combining multiple strings together. In Python you can do this with the "+" operator.

str_one = "your"
str_two = "face"
str_three = str_one + " " + str_two
#your face

#String Formatting
There are also several ways to format strings in Python to interpolate variables.
The new way (new in Python 3.6+) => F-Strings

x = 10
formatted = f"I've told you {x} times already!"

The tried  and true way (Python 2-> 3.5) => .format method

X = 10 
formatted " I've told you {} to,es aleady!".format(10)


