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

letters = ["a", "b", "c", "d", "e"]
print (letters)

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

print ("Operations on Lists in Python")

z = [0]*10
print (z)
#output: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

letters = ["a", "b", "c", "d", "e"]
print (letters)

stg = ["get", "cat", "dog", "bat"]
print (stg)

conc = letters + stg
print (conc)
#output: ['a', 'b', 'c', 'd', 'e', 'get', 'cat', 'dog', 'bat']

var = list("Hey there!")
print (var)
#output: ['H', 'e', 'y', ' ', 't', 'h', 'e', 'r', 'e', '!']

num = [1, 2, 3, 4, 5]
print (num)

one, *other = num
print (one)
#output: 1
#In this example, we are using unpacking to assign the first element of the list num to the variable one and the rest of the elements to the variable other. The * operator is used to indicate that we want to capture all remaining elements in a list.

print (other)
#output: [2, 3, 4, 5]
#In this example, we are using unpacking to assign the first element of the list num to the variable one and the rest of the elements to the variable other. The * operator is used to indicate that we want to capture all remaining elements in a list.

print ("---------------------------------")

print ("List Methods in Python")

print ("1. append() method")

num = [1, 2, 3, 4, 5]
print (num)
#output: [1, 2, 3, 4, 5]

num.append(6)
print (num)
#output: [1, 2, 3, 4, 5, 6]

print ("2. extend() method")

num = [1, 2, 3, 4, 5]
print (num)
#output: [1, 2, 3, 4, 5]

num.extend([6, 7, 8])
print (num)
#output: [1, 2, 3, 4, 5, 6, 7, 8]

stg = ["get", "cat", "dog", "bat"]
print (stg)
#output: ['get', 'cat', 'dog', 'bat']

num.extend(stg)
print (num)
#output: [1, 2, 3, 4, 5, 6, 7, 8, 'get', 'cat', 'dog', 'bat']
#In this example, we are using the extend() method to add the elements of the list stg to the end of the list num. The extend() method takes an iterable (like a list) as an argument and adds each element of that iterable to the end of the list.

print ("3. insert() method")

num.insert(5, "Simple")
print (num)
#output: [1, 2, 3, 4, 5, 'Simple', 6, 7, 8, 'get', 'cat', 'dog', 'bat']
#In this example, we are using the insert() method to add the string "Simple" at index 5 of the list num. The insert() method takes two arguments: the index where we want to insert the new element and the element itself. The existing elements in the list are shifted to the right to make room for the new element.

print ("4. remove() method")

num.remove("Simple")
print (num)
#output: [1, 2, 3, 4, 5, 6, 7, 8, 'get', 'cat', 'dog', 'bat']
#In this example, we are using the remove() method to remove the first occurrence of the string "Simple" from the list num. The remove() method takes one argument: the element we want to remove from the list. If the element is not found in the list, a ValueError will be raised.

var1 = ['b', 'd', 'q', 'a', 'l']
var1.sort()
print (var1)
#output: ['a', 'b', 'd', 'l', 'q']
#In this example, we are using the sort() method to sort the elements of the list var1 in ascending order. The sort() method modifies the original list in place and does not return a new list. If we want to sort the list in descending order, we can pass the argument reverse=True to the sort() method.

print ("5. pop() method")

num.pop()
print (num)
#output: [1, 2, 3, 4, 5, 6, 7, 8, 'get', 'cat', 'dog']
#In this example, we are using the pop() method to remove and return the last element of the list num. The pop() method takes an optional argument: the index of the element we want to remove. If no index is provided, the last element of the list is removed by default. The pop() method modifies the original list in place and returns the removed element.

print ("6. index() method")

print (num.index(5))
#output: 4
#In this example, we are using the index() method to find the index of the first occurrence of the integer 5 in the list num. The index() method takes one argument: the element we want to find the index of. If the element is not found in the list, a ValueError will be raised.

print ("7. count() method")

num = [1, 2, 3, 4, 5, 5, 6, 7, 8]
print (num)
#output: [1, 2, 3, 4, 5, 5, 6, 7, 8]

print (num.count(5))
#output: 2
#In this example, we are using the count() method to count the number of occurrences of the integer 5 in the list num. The count() method takes one argument: the element we want to count. It returns the number of times the element appears in the list.

print ("8. reverse() method")

num.reverse()
print (num)
#output: [8, 7, 6, 5, 5, 4, 3, 2, 1]
#In this example, we are using the reverse() method to reverse the order of the elements in the list num. The reverse() method modifies the original list in place and does not return a new list. If we want to create a new list that is a reversed version of the original list, we can use slicing with a step of -1 (num[::-1]).

print ("9. clear() method")

num.clear()
print (num)
#output: []
#In this example, we are using the clear() method to remove all elements from the list num. The clear() method modifies the original list in place and does not return a new list.

print ("10. copy() method")

num = [1, 2, 3, 4, 5]
num_copy = num.copy()
print (num_copy)
#output: [1, 2, 3, 4, 5]
#In this example, we are using the copy() method to create a shallow copy of the list num. The copy() method returns a new list that contains the same elements as the original list. Changes made to the new list will not affect the original list, and vice versa.

print ("11. list() method")

num = [1, 2, 3, 4, 5]
num_list = list(num)
print (num_list)
#output: [1, 2, 3, 4, 5]
#In this example, we are using the list() method to create a new list that contains the same elements as the original list num. The list() method takes an iterable as an argument and returns a new list containing all the elements of the iterable.

print ("12. del() method")

num = [1, 2, 3, 4, 5]
del num[2]
print (num)
#output: [1, 2, 4, 5]
#In this example, we are using the del() method to remove the element at index 2 from the list num. The del() method takes an index as an argument and removes the element at that index from the list. The existing elements in the list are shifted to the left to fill the gap left by the removed element.

print ("13. in operator")

num = [1, 2, 3, 4, 5]
if 3 in num:
    print ("3 is present in the list")
#output: 3 is present in the list

if 6 not in num:
    print ("6 is not present in the list")
#output: 6 is not present in the list

print ("14. len() method")

num = [1, 2, 3, 4, 5]
print (len(num))
#output: 5
#In this example, we are using the len() method to get the number of elements in the list num. The len() method takes a list as an argument and returns the number of elements in that list.

print ("15. sum() method")

num = [1, 2, 3, 4, 5]
print (sum(num))
#output: 15
#In this example, we are using the sum() method to calculate the sum of all elements in the list num. The sum() method takes a list as an argument and returns the sum of all elements in that list.

print ("16. sorted() method")

num = [5, 2, 9, 1, 5, 6]
sorted_num = sorted(num)
print (sorted_num)
#output: [1, 2, 5, 5, 6, 9]
#In this example, we are using the sorted() method to create a new list that contains the elements of the original list num in ascending order. The sorted() method does not modify the original list and returns a new list. If we want to sort the list in descending order, we can pass the argument reverse=True to the sorted() method.

print ("17. list comprehension")

num = [1, 2, 3, 4, 5]
squared_num = [x**2 for x in num]
print (squared_num)
#output: [1, 4, 9, 16, 25]
#In this example, we are using list comprehension to create a new list that contains the squares of all elements in the list num. The list comprehension takes the form [expression for item in iterable].
#x is the expression that defines how to transform each item in the iterable (in this case, squaring each number), and num is the iterable we are iterating over. The result is a new list containing the squared values of the original list.

print ("---------------------------------")

print ("Built-in functions with Lists in Python")

x = [9, 12, 14, 5, 90, 45, 65, 55, 75, 85]

len(x)
print(len(x))
#output: 10

min(x)
print(min(x))
#output: 5

max(x)
print(max(x))
#output: 90

sorted_x = sorted(x)
print(sorted_x)
#output: [5, 9, 12, 14, 45, 55, 65, 75, 85, 90]

sum_x = sum(x)
print(sum_x)
#output: 455

Average_x = sum(x) / len(x)
print(Average_x)
#output: 45.5

print ("---------------------------------")

print ("Tuples in Python")

emp = ()
print (type(emp))
#output: <class 'tuple'>

print (emp)
#output: ()

city = ("New York", "Los Angeles", "Chicago", "Houston", "Phoenix")
print (city)
#output: ('New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix')   

type(city)
#output: <class 'tuple'>

city = "New york",
type(city)
#output: <class 'tuple'>

tuple1 = (1, 2, 3, 4, 5)
tuple1.append(6)
#output: AttributeError: 'tuple' object has no attribute 'append'
#tuple object has no attribute 'append' because tuples are immutable, meaning that their elements cannot be changed after they are created. Therefore, we cannot add or remove elements from a tuple using methods like append() or remove().
#We can use or not use the parentheses () to define a tuple. If we use parentheses, we can create an empty tuple or a tuple with one or more elements. If we do not use parentheses, we can create a tuple with one or more elements, but we cannot create an empty tuple.
#Difference between list and tuple is that list is mutable (changeable) while tuple is immutable (unchangeable). This means that we can add, remove, or change items in a list, but we cannot do the same with a tuple.

print ("---------------------------------")

print ("Concatenation of Tuples in Python")

print (city)
#output: ('New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix')

num = (1, 2, 3, 4, 5)
print (num)
#output: (1, 2, 3, 4, 5)

print (city + num)
#output: ('New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 1, 2, 3, 4, 5)

print (city * 2)
#output: ('New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix')

print ("---------------------------------")

print("Nested Tuples in Python")

nest = (city, num)
print (nest)
#output: (('New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'), (1, 2, 3, 4, 5))

print (nest[0])
#output: ('New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix')

print (nest[1])
#output: (1, 2, 3, 4, 5)

print (nest[0][1])
#output: Los Angeles

print (nest[1][3])
#output: 4

print ("---------------------------------")

print ("Repetition of Tuples in Python")

print (city * 3)
#output: ('New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix')

rep = (1, 2, 3) * 4
print (rep)
#output: (1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)

print ("---------------------------------")

print ("Slicing of Tuples in Python")

num = (1, 2, 3, 4, 5)
print (num[1:4])
#output: (2, 3, 4)

print(num[::-1])
#output: (4, 3, 2, 1)

print ("---------------------------------")

print ("Unpacking of Tuples in Python")

tuple("Simplilearn")
#output: ('S', 'i', 'm', 'p', 'l', 'i', 'l', 'e', 'a', 'r', 'n')

num = (1, 2, 3, 4, 5)
print(num)
#output: (1, 2, 3, 4, 5)

a, b, c, d, e = num
print(a, b, c, d, e)
#output: 1 2 3 4 5

a, *b, c, d = num
print(a, b, c, d)
#output: 1 [2, 3] 4

print ("---------------------------------")

print("Deleting a Tuple in Python")

tuple1 = (1, 2, 3, 4, 5)
print(tuple1)
#output: (1, 2, 3, 4, 5)

del tuple1
print(tuple1)
#Error

print ("---------------------------------")

print ("Converting list to tuple")

lst = [1, 2, 3, 4, 5]
print (type(lst))
#output: <class 'tuple'>

tpl = tuple(lst)
print (tpl)
#output: (1, 2, 3, 4, 5)

print ("---------------------------------")

