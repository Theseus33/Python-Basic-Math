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

  


so if you actually want a backslash you need \\ or else Python will think its the start of an escape char


#Converting Data Types

In string interpolation, data types are implicitly converted into string form.
You can also explicitly convert variables by using the name of the builtin type as a function.

decimal = 12.563456344534
integer = int(decimal) #12 but does not round up/down

my_list = [1, 2, 3]
my_list_as_a_string = str(my_list) #"[1, 2, 3]"

num = 12
type(num)
>num = float(num)
type(num)
<class 'float'>
num 
12.0
int(99.4443)
99
int(99.99)
99
