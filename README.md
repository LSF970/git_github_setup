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
- This is a change to show git pull
- To pull from GitHub use `git pull` this will sync any changes you made via the web client to your localhost

## git cheat sheet
```bash
usage: git [-v | --version] [-h | --help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           [--super-prefix=<path>] [--config-env=<name>=<envvar>]
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone     Clone a repository into a new directory
   init      Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add       Add file contents to the index
   mv        Move or rename a file, a directory, or a symlink
   restore   Restore working tree files
   rm        Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect    Use binary search to find the commit that introduced a bug
   diff      Show changes between commits, commit and working tree, etc
   grep      Print lines matching a pattern
   log       Show commit logs
   show      Show various types of objects
   status    Show the working tree status

grow, mark and tweak your common history
   branch    List, create, or delete branches
   commit    Record changes to the repository
   merge     Join two or more development histories together
   rebase    Reapply commits on top of another base tip
   reset     Reset current HEAD to the specified state
   switch    Switch branches
   tag       Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch     Download objects and refs from another repository
   pull      Fetch from and integrate with another repository or a local branch
   push      Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
See 'git help git' for an overview of the system.

```
### Intro to Data types & Operators
- ` +  -  *  /`

###### Comparison operators
- `>` greater than
- `<` less than
- `==` true or false
- `>=` greater than or equal to
- `<=` less than or equal to

### Boolean methods
```python
# # Booleans and Boolean methods
# DRY - Don't Repeat Yourself - e.g. print("")
greeting = "Hello World!"
print(greeting)
print(greeting.isalpha())
print(greeting.islower())
print(greeting.startswith("H"))
print(greeting.endswith("!")) # checks if the variable ends with !
print(greeting.isdigit())
```

### String methods in action

```python
# String Methods that are available

# # use case: var = string "asadfnodsjfnosanf                       " - lots of spaces, not needed
white_space = "lots of spaces at the end                           "
print(len(white_space))
# # strip() - removes white spaces
print(len(white_space.strip())) # Value returned is 25 because white space AT THE END is removed

example_text = "here's sOme text with lOts of text"
print(example_text)
print(example_text.count("text"))
print(example_text.lower())
print(example_text.upper())
print(example_text.capitalize())
print(example_text.replace("with", ","))

```

### Concatenation and casting
- adding strings together
- casting/converting data types

## Data collections
### Lists and Tuples

```python
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
```




