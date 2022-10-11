# Data collections

# Lists
# Tuples
# Dictionaries (dict)
# All of these store data

# LISTS

# # syntax is: name_list = ["asfasdfA", "SAFASFASF", "asfasfasf"]
# shopping_list = ["eggs", "milk", "bread", "tea"]
# print(shopping_list)
# print(type(shopping_list))
# print(shopping_list[0])
# # remove from the list
# shopping_list.remove("eggs")
# print(shopping_list)
# # use .pop to remove from the end of the list
# shopping_list.pop()
# print(shopping_list)
# # add to the end of the list
# shopping_list.append("cheese")
# print(shopping_list)
# # replace an item in the list
# print(shopping_list[2])
# shopping_list[2] = "Bacon"
# print(shopping_list)
# # Use .pop with an index to remove a specific value via index rather than name (in this case Bacon)
# shopping_list.pop(2)
# print(shopping_list)

# Lists can also have multiple types
multiple_types = [1, 2, 3, "one", "two", "three"]
print(multiple_types)
print(multiple_types[2:4]) # slicing and indexing

# Tuples
# Why do we need tuples? They cannot be changed! (imutable)
# Syntax for tuple: use (...)
tuple_example = (1, 2, 3, "one")
print(tuple_example)
print(type(tuple_example))
# tuple_example.pop() # Will cause error because you cannot change tuple



