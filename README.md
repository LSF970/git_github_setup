# Python intro
## Why python
### Python use cases
#### Python setup with Pycharm
##### Python variables

- Env Testing`print("Hello World")`

```python
# testing the env with print statement
# Dynamic typed language (Python)

# Python variables
# store any data -
# To store user data - hard code the data - any other time
# first_name = "Angel" - string
# name = "Subhaan" - string
# DOB = 99 - int
# UK_resident = yes or no - bool
# salary = 40000 - int
# travel = 15.4 - float

# gross_salary = salary + travel

# first_name = "Luke"
# last_name = "Fairbrass"
# salary = 50
# travel = 3.5

# print(salary + travel)

# print(first_name + " " + last_name)
# Display the value of variable first_name -> Use print statement

# How to find out the data type of a variable
# type()
# print(type(salary))

# interact with the user by taking data in - input()
# print("Welcome! Please enter your name")
# username = input() # store user input in variable
# print("Your name is " + username) # Do something with the name

# get user first_name and last_name
# display the names in a line
# user dob
# user course_name
# UK resident status

print("Welcome, please enter the information about yourself when prompted")
print("Enter your first name")
first_name = input()
print("Thank you. Now enter your last name")
last_name = input()
print("OK, so your name is " + first_name + " " + last_name)
print("Please enter your date of birth")
DOB = input()
print("Your date of birth is " + DOB)
print("Please enter the course you are enrolled on")
course = input()
print("You are on the " + course + " course")
print("Finally, are you a UK resident?")
uk_resident = input()
print("Here are your details in full")
print("First name: " + first_name)
print("Last name: " + last_name)
print("DOB: " + DOB)
print("Course: " + course)
print("UK Resident: " + uk_resident)

```

## Adding to a file
- add changes to our GitHub repo - the changes that we made on localhost

- `git add filename` or `git add .` . means push everything to the repo
- `git commit -m "New markdown guide added"`
- Now send this new data to GitHub
- `git push -u origin main`
- `git status` Tells us what will be changed, added, taken out etc.
- This is change to show git pull
- To pull from GitHub use `git pull` this will sync any changes you made via the web client to your localhost
