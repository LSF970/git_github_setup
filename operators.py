# # Let's see the operators in action
#
# ### Intro to Data types & Operators
# # - ` +  -  *  /`
#
# a = 24
# b = 16
#
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
#
# ###### Comparison operators
# # - `>` greater than
# # - `<` less than
# # - `==` true or false
# # - `>=` greater than or equal to
# # - `<=` less than or equal to
#
# print(a > b)
# print(a < b)
# print(a == b)
# print(a >= b)
#
# # % operator - what it is and how is it used?
# # divides and shows remainder
#
# print(a % b)
#
# # Is not equal to
#
# print(a != b)
#
# # # Booleans and Boolean methods
# # DRY - Don't Repeat Yourself - e.g. print("")
# greeting = "Hello World!"
# print(greeting)
# print(greeting.isalpha())
# print(greeting.islower())
# print(greeting.startswith("H"))
# print(greeting.endswith("!")) # checks if the variable ends with !
# print(greeting.isdigit())

# String slicing
# String indexing - starts from 0, not 1!
# Hello World!
# 0-H 1-e 2-l 3-l 4-o 5- 6-W 7-o 8-r 9-l 10-d 11-!

greeting = "Hello World!"
print(greeting)
# We have a built-in method that checks the length of a string
print(len(greeting))
print(greeting[1])
print(greeting[0:5])
print(greeting[6:12])
# Reverse (using - indexing
print(greeting[:5])
print(greeting[-6:])









