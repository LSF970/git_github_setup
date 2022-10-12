# What is a dictionary? - Data collection type
# How to manage a dictionary - how to manage the data using a dictionary
# It works as a key value pair: key = value
# Syntax: = { Key: "value" }

# Store student's data - name, stream, completed_lessons
student_1 = {
    "key": "values",
    "name": "Luke",
    "stream": "DevOps",
    "completed_lessons": 5,
    "completed_topics_name": ["Data_types", "Lists", "Tuples", "String_methods", "Bool_methods"]
}

# Using the dictionary
print(student_1)
print(student_1["stream"]) # Print the value for the name of the key - stream in this case
print(student_1["completed_topics_name"][0]) # Displays a particular index from a list in a dictionary
student_1["completed_topics_name"].remove("Data_types") # Removes from a list in a dictionary
print(student_1["completed_topics_name"]) # Showcases removed data, Lists is now first index

print(student_1["completed_lessons"])
student_1["completed_lessons"] = 4 # Change a value in a dictionary
print(student_1["completed_lessons"])

print(student_1["completed_topics_name"][0]) # Print first index in list within dictionary

student_1["completed_topics_name"].remove("Bool_methods") # Remove a value from a key
print(student_1["completed_topics_name"])

# Dictionary methods

## keys -> returns just the keys in the dictionary
print(student_1.keys())
print(type(student_1.keys()))

## get -> works the same way as using the square brackets to access a key
print(student_1.get("name"))

## values -> does the same as the keys method but for the values
print(student_1.values())

## items -> returns an array of tuples
print(student_1.items())


