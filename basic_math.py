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

#User Input
There is a built-inb function in Python called "input" that will prompt the user and store the result 
in a variable.

name = input("Enter your name here: ")
Enter your name here:

#Conditional Statements

Conditional logic using if statements represents different paths a program can take based on some type
of comparison of input

pseudocode

if some condition is True:
    do something
elif some other condition is True:
    do something
else: 
    do something

example

if name == "Arya Stark":
    print("Valar Morghulis")
elif ma,e == "Jon Snow":
    print("You know nothing")
else:
    print("Carry on")

#Truthiness

In Python, all conditional checks resolve to True or False.bit_length

x = 1
x is 1 #True
x is 0 #False

We can call values that will resolve to True "truthy", or values that will resolve to False "falsy".capitalize

Besides False ocnditional checks, other things that are naturally falsy include: empty objects, empty strings,
None, and zero.

#Comparison Operators
if a = 1 and b = 1

Operator    What it does                                    example

==          Truthy if a has the same value as b             a==b #True
!=          Truthy if a does NOT havet he same value as b   a!=b #False
>           Truthy if a is greater than b                   a>b #False
<           Truthy if a is less than b                      a<b #False
>=          Truthy if a greater than or equal to b          a>=b #True
<=          Truthy if a is less than or equal to b          a<=b #True

#Logical Operators

In Python, the following operators can be used to make Boolean Logic comparisons or statements:

Operator    What it does                                    example

and         Truthy if both a AND b are True                 if a and b:
            (logical conjunction)                               print(c)

or          Truthy if either a OR b are True                if am_tired or is_bedtime:
            (logical disjunction)                               print("go to sleep")

not         Truthy if the opposite of a is True             if not is_weekend:
            (logical negation)                                  print("go to work")


from random import choice
food = choice(['apple','grape', 'bacon', 'steak', 'worm', 'dirt'])

if food == 'apple' or food == 'grape':
    print("fruit")
elif food == 'bacon' or food == 'steak':
    print("meat")
else:
    print("yuck")


age = 21
# 2-8 2 dollar ticket
# 65 5 dollar ticket
# 10 dollar ticket

(age >= 2 and age <= 8) or (age >=65 )

#Note on Is Vs ==
In Python "==" and "is" are very similar comparators, however they are not the same.

a = 1
a == 1 #True
a is 1 #True

a = [1,2,3] # a list of numbers
b = [1,2,3] 
a == b #True
a is b #False

If you want to check values use "=="
while is checks if the variable is in the same place in memory.

x = 13
y = 13
x == y #True
x is y #True (because its not a new object in memory but the same value)

a = [1,2]
b = [1,2]
a == n #True
a is b #False (because although the values are the same they are two seperate objects in memory)

#Bouncer Code - Along and Nested Conditionals

#ask for age
age = input("How old are you:")

if int(age) >= 18 and int(age) < 21:
    print("You can enter, but need a wristband!")
# 18-21 wristband
elif age >= 21:
# 21+ drink, normal entry
    print("You are good to enter and can drink!")
else:
# too young sorry
    print("You cannot come in, little one! :(")
else:
    print("Please enter an age!")
