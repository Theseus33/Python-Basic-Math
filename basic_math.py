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


#Loops

In Python, for loops are written like so:

for item in iterable_object:
    # do something with item

A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

Example
Print each fruit in a fruit list:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
The for loop does not require an indexing variable to set beforehand.

Looping Through a String
Even strings are iterable objects, they contain a sequence of characters:

Example
Loop through the letters in the word "banana":

for x in "banana":
  print(x)
The break Statement
With the break statement we can stop the loop before it has looped through all the items:

Example
Exit the loop when x is "banana":

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
Example
Exit the loop when x is "banana", but this time the break comes before the print:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
The continue Statement
With the continue statement we can stop the current iteration of the loop, and continue with the next:

Example
Do not print banana:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
The range() Function
To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

Example
Using the range() function:

for x in range(6):
  print(x)
Note that range(6) is not the values of 0 to 6, but the values 0 to 5.

The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):

Example
Using the start parameter:

for x in range(2, 6):
  print(x)
The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):

Example
Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):
  print(x)
Else in For Loop
The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

Example
Print all numbers from 0 to 5, and print a message when the loop has ended:

for x in range(6):
  print(x)
else:
  print("Finally finished!")
Note: The else block will NOT be executed if the loop is stopped by a break statement.

Example
Break the loop when x is 3, and see what happens with the else block:

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
Nested Loops
A nested loop is a loop inside a loop.

The "inner loop" will be executed one time for each iteration of the "outer loop":

Example
Print each adjective for every fruit:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
The pass Statement
for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

Example
for x in [0, 1, 2]:
  pass


#Lists

A list is ajust a collection or grouping of items.

Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:
Example

Create a List:
thislist = ["apple", "banana", "cherry"]
print(thislist)
List Items

List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.
Ordered

When we say that lists are ordered, it means that the items have a defined order, and that 
order will not change.

If you add new items to a list, the new items will be placed at the end of the list.

Note: There are some list methods that will change the order, but in general: the order of 
the items will not change.
Changeable

The list is changeable, meaning that we can change, add, and remove items in a list after 
it has been created.

Allow Duplicates

Since lists are indexed, lists can have items with the same value:
Example

Lists allow duplicate values:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
List Length

To determine how many items a list has, use the len() function:
Example

Print the number of items in the list:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
List Items - Data Types

List items can be of any data type:
Example

String, int and boolean data types:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

A list can contain different data types:
Example

A list with strings, integers and boolean values:
list1 = ["abc", 34, True, 40, "male"]
type()

From Python's perspective, lists are defined as objects with the data type 'list':
<class 'list'>
Example

What is the data type of a list?
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
The list() Constructor

It is also possible to use the list() constructor when creating a new list.
Example

Using the list() constructor to make a List:
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
Python Collections (Arrays)

There are four collection data types in the Python programming language:

    List is a collection which is ordered and changeable. Allows duplicate members.
    Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    Set is a collection which is unordered and unindexed. No duplicate members.
    Dictionary is a collection which is unordered and changeable. No duplicate members.

When choosing a collection type, it is useful to understand the properties of that type. 
Choosing the right type for a particular data set could mean retention of meaning, and, it 
could mean an increase in efficiency or security.

Pop 
rRemove the item at the given position in the list and return it.
If no index is specified, removes and returns last item in the list

first_list = [1.2 3. 4]
first_list.pop() #4
first_list.pop(1) #2

Index 
Returns the index of the specified item on the list

numbers = [5, 6, 7, 8, 9, 10]

numbers.index(6) # 1
numbers.index(9) # 4

numbers = [5, 5, 6, 7, 5 , 8, 8, 9, 10]

numbers.index(5) # 0
numbers.index(5, 1) #1
numbers.index(5, 2) #4

numbers.index(8, 6, 8) #6

slice

Make new lists using slices of the old list

some_list[start:end:step]

first parameter for Slice:StopIteration
what index to start slicing from

first_list = [1, 2, 3, 4]
first_list[1:] # [2, 3, 4]
first_list[3:] #[4]

colors = ["red", "orange", "yellow", "green", "blue,
"indigo", "violet"]

colors[2:] # ["green", "blue,"indigo", "violet"]

Second Parameter for slice :end

The index to copy up to (exclusive counting)

first_list = [1, 2, 3, 4]
first_list[:2] #[1, 2, 3]
first_list[1:3] #[2, 3]

