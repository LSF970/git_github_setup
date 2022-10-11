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

# greeting = "Hello World!"
# print(greeting)
# # We have a built-in method that checks the length of a string
# print(len(greeting))
# print(greeting[1])
# print(greeting[0:5])
# print(greeting[6:12])
# # Reverse (using - indexing
# print(greeting[:5])
# print(greeting[-6:])

# String Methods that are available

# # # use case: var = string "asadfnodsjfnosanf                       " - lots of spaces, not needed
# white_space = "lots of spaces at the end                           "
# print(len(white_space))
# # # strip() - removes white spaces
# print(len(white_space.strip())) # Value returned is 25 because white space AT THE END is removed
#
# example_text = "here's sOme text with lOts of text"
# print(example_text)
# print(example_text.count("text"))
# print(example_text.lower())
# print(example_text.upper())
# print(example_text.capitalize())
# print(example_text.replace("with", ","))

# user data input
first_name = "Luke"
last_name = "Fairbrass"
salary = 40

print(first_name)
print(last_name)
print(first_name + last_name)
# Need to add a space
print(first_name + " " + last_name)
# How to concatenate two data types
print(first_name + " " + last_name + " " + str(salary)) # cast int as string using str()
# or use f-string (later versions of python only)
print(f"Hello {first_name} {last_name}, £{salary} per hour")













