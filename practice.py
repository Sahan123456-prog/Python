import practice

print ("Welcome to python practice!")

#output: Welcome to python practice!

print ("---------------------------------")

#Data types in python
#1. String

x = "Hello World"
print (x)

#output: Hello World

print ("---------------------------------")

#2. Integer

z = 20
print (z)

#output: 20
#In Python, an integer is a whole number without a decimal point. It can be positive, negative, or zero. Integers are used for counting, indexing, and performing arithmetic operations.
#And also in Python, integers we not use " " or ' ' to define an integer. We just write the number without any quotes.

print ("---------------------------------")

#3. Float

y = 20.5
print (y)

#output: 20.5
#In Python, a float is a number that has a decimal point. Floats are used for representing real numbers and performing arithmetic operations that involve decimals.

print ("---------------------------------")

#4. Boolean

w = True
print (w)

#output: True
#In Python, a boolean is a data type that can only have two values: True or False. Booleans are used for logical operations and decision-making in programs.

print ("---------------------------------")

#5. List

l = [14, 67, 89, 23, 45]
print (l)

#output: [14, 67, 89, 23, 45]
#In Python, a list is a collection of items that are ordered and changeable. Lists are used to store multiple items in a single variable.
#If we use multiple values in a list, we need to separate them with commas and enclose them in square brackets [].

print(l[0])  # Output: 14
print(l[1])  # Output: 67
print(l[2])  # Output: 89
print(l[3])  # Output: 23
print(l[4])  # Output: 45

#If you want to print value in a list, you can use the index number of that value. The index number starts from 0 for the first value, 1 for the second value, and so on.

print ("---------------------------------")

#6. Tuple

t = (4, 8, 15, 16, 23, 6)
print (t)

#output: (4, 8, 15, 16, 23, 6)
#In Python, a tuple is a collection of items that are ordered and unchangeable. Tuples are used to store multiple items in a single variable.
#If we use multiple values in a tuple, we need to separate them with commas and enclose them in parentheses ().

print(t[0])  # Output: 4
print(t[1])  # Output: 8
print(t[2])  # Output: 15
print(t[3])  # Output: 16
print(t[4])  # Output: 23
print(t[5])  # Output: 6

#Difference between list and tuple is that list is mutable (changeable) while tuple is immutable (unchangeable). This means that we can add, remove, or change items in a list, but we cannot do the same with a tuple.

(x, y, z) = (4, 8, 15)
print(x)  # Output: 4
print(y)  # Output: 8
print(z)  # Output: 15

print ("---------------------------------")

#7. Set

s = {1, 2, 3, 4, 5}
print (s)

#output: {1, 2, 3, 4, 5}
#In Python, a set is a collection of unique items that are unordered and unindexed.

print ("---------------------------------")

#8. Dictionary

d = {"name": "John", "age": 30, "city": "New York"}
print (d)

#output: {'name': 'John', 'age': 30, 'city': 'New York'}
#In Python, a dictionary is a collection of key-value pairs that are unordered and changeable. Dictionaries are used to store data in a structured way, where each value is associated with a unique key.

print(d["name"])  # Output: John
print(d["age"])   # Output: 30
print(d["city"])  # Output: New York

print ("---------------------------------")

#9. None

n = None
print (n)

#output: None
#In Python, None is a special value that represents the absence of a value or a null value. It is often used to indicate that a variable has not been assigned a value yet or that a function does not return anything.

print ("---------------------------------")

#10. Complex
c = 3 + 4j
print (c)

#output: (3+4j)
#In Python, a complex number is a number that has both a real part and an imaginary part. Complex numbers are used in mathematical and scientific computations.

print(c.real)  # Output: 3.0
print(c.imag)  # Output: 4.0

print ("---------------------------------")

#11. Mixed Data Types

mixed = [1, "Hello", 3.14, True]
print (mixed)

#output: [1, 'Hello', 3.14, True]

print(mixed[0])  # Output: 1
print(mixed[1])  # Output: Hello
print(mixed[2])  # Output: 3.14
print(mixed[3])  # Output: True

print ("---------------------------------")

print ("Arithmetic Operations in Python")

x = 20
y = 10
result = x + y
print ("Addition: ", result)

#output: Addition: 30

result = x - y
print ("Subtraction: ", result)

#output: Subtraction: 10

result = x * y
print ("Multiplication: ", result)

#output: Multiplication: 200

result = x / y
print ("Division: ", result)

#output: Division: 2.0

result = x // y
print ("Floor Division: ", result)

#output: Floor Division: 2

result = x % y
print ("Modulus: ", result)

#output: Modulus: 0

result = x ** y
print ("Exponentiation: ", result)

#output: Exponentiation: 10240000000000

print ("---------------------------------")

print ("String Operations in Python")

var = "Small"
print (var[0])

#output: S

print (var[0:2])

#output: Sm

print (var[3:])

#output: all

print (var[:2])

#output: Sm

print (var[10])

#output: IndexError: string index out of range

len(var)

#output: 5

#Semicolon is not required in python. It is used to separate multiple statements on a single line. But it is not recommended to use semi-colon in python as it reduces the readability of the code.

print ("---------------------------------")

print ("Functions in Python")

x = -7.5
print (abs(x))

#output: 7.5

#math.e = 2.718281828459045
#math.pi = 3.141592653589793

import math
x = 10
print (math.exp(x))

#output: 22026.465794806718

print (math.sqrt(x))

#output: 3.1622776601683795

max(1, 34, 587, 3654, 968, 5879, 365, 587, 3654, 968, 5869)
print (max)

#output: 5879

min(1, 34, 587, 3654, 968, 5879, 365, 587, 3654, 968, 5869)
print (min)

#output: 1

print("---------------------------------")

print ("Lists in Python")

num = [1, 2, 3, 4, 5]
print (num)

#output: [1, 2, 3, 4, 5]

letter = ["a", "b", "c", "d", "e"]
print (letter)

#output: ['a', 'b', 'c', 'd', 'e']

stg = ["get", "cat", "dog", "bat"]
print (stg)

#output: ['get', 'cat', 'dog', 'bat']

mix = [1, 6, "dog", "cat"]
print (mix)

#output: [1, 6, 'dog', 'cat']

print (mix[3])
#output: cat

print (mix[-2])
#output: dog
#In this example, we are using negative indexing to access the elements of the list. The index -1 refers to the last element of the list, -2 refers to the second last element, and so on.

print (mix[2:])
#output: ['dog', 'cat']
#In this example, we are using slicing to get the elements from index 2 to the end of the list. The output is a new list that contains the elements from index 2 to the end of the original list.

print (mix[:2])
#output: [1, 6]
#In this example, we are using slicing to get the elements from the beginning of the list up to, but not including, index 2. The output is a new list that contains the elements from the beginning of the original list up to, but not including, index 2. 

print (mix[1:3])
#output: [6, 'dog']
#In this example, we are using slicing to get the elements from index 1 to index 3 (not including index 3) of the list. The output is a new list that contains the elements from index 1 to index 2 of the original list.

print (mix[::2])
#output: [1, 'dog']
#In this example, we are using slicing with a step of 2 to get every second element from the list. The output is a new list that contains the elements at indices 0, 2, 4, and so on.
#mix[start:stop:step] is the syntax for slicing a list in Python. The start index is inclusive, the stop index is exclusive, and the step index determines the interval between elements to include in the new list.

print (mix[::-1])
#output: ['cat', 'dog', 6, 1]
#In this example, we are using slicing with a negative step of -1 to get the elements of the list in reverse order. The output is a new list that contains the elements of the original list in reverse order.

print (mix[1:4:2])
#output: [6, 'cat']
#In this example, we are using slicing with a step of 2 to get every second element from the list. The output is a new list that contains the elements at indices 1, 3, 5, and so on.

print ("---------------------------------")