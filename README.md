# Python Intro
## Why Python
### Python Use Case
#### Python set up with pycharm
##### Python Variable

```commandline
print()
```

#### Git & Github

- add changes to our Git-Hub repo - the changes that we made on localhost

- `git add filename` or `git add .` - means push everything from current location
- `git commit -m "new markdown guide added"`
- now let's send this new data to github
- `git push -u origin main` (-u stands for upstream)
- `git status` - To check for changes
- add `.gitignore` then add the folders and files you don't want to upload to github
- to pull changes from Git-hub `git pull`

### Git Help
```
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
```
## Python

### Intro to Data types & Operators
### - `+` `-` `*` `/`

### Comparison Operators
- `>` greater than
- `<` less than
- `==` True or False
- `>=` greater than or equal
- `<=` less than or equal

```
a = 24
b = 16

print(a+b) # outcome added value of a & b
print(a-b) # outcome substraction value of a & b

# Comparison
print(a>b) # True
print(a<b) # False
```

#### Modulo Operator `%`

The `%` symbol in Python is called the Modulo Operator. It returns the remainder of dividing the left hand operand by right hand operand.

#### Use Case:


#### Not Equal Operator `!=`


```commandline
# Built in Methods
# DRY - Don't Repeat Yourself
# - print()
greeting = "Hello World!"
print(greeting)
print(greeting.isalpha())        # Check if the variable is alphabet Only
print(greeting.islower())        # Check if the variable is in lowercase
print(greeting.startswith('H'))  # Check if starts with a specified letter
print(greeting.endswith('!'))    # Check if ends with a specified letter

```

```commandline
# String
# String indexing - starts from 0
# H e l l o   W o r l d  !
# 0 1 2 3 4 5 6 7 8 9 10 11
#           -2-1

greeting = "Hello World!"
print(greeting)
# len method checks the length of the string
print(len(greeting))

# Forward Indexing
print(greeting[0:5])   # Prints Hello
print(greeting[6:12])  # Prints World!

# Reverse Indexing
print(greeting[-12:-6]) # Prints Hello
print(greeting[-6:])   # Prints World!
```

```commandline
# Available String Method
white_space = "lot's of spaces at the end                                "
print(len(white_space))
# strip() removes white space
print(len(white_space.strip())) # this will remove all the white at the end.
Example_text = "abhishek here's sOme text wIth lOt's of text"
# Count no. of occurrence
print(Example_text.count("text"))
# lower case and upper case and Capitalize
print(Example_text)
print(Example_text.lower())
print(Example_text.upper())
print(Example_text.capitalize())
# replace
print(Example_text.replace("wIth", ","))
```

### Concatenation & Casting
- adding strings together
 - casting/converting data types
```commandline
# User data input
first_name = "abhishek"
last_name = "jha"
salary = 40

print(first_name)
print(last_name)
print(first_name.capitalize() + " " + last_name.capitalize())  # Concatenation
print(first_name + " " + last_name + " earns a salary of £" + str(salary))  # Casting int to string before concatenating
print(f"{first_name} {last_name} earns a salary of £{salary}")  # Another way of writing it

Expected Output:
abhishek
jha
Abhishek Jha
abhishek jha earns a salary of £40
abhishek jha earns a salary of £40
```

### Exercise 2.1

```commandline
Using what we have learned so far let's head back to our user_details_capture file and ensure we are using / casting the same type. Extend the capture further to grab details such as address (ensuring that a house number is correctly represented, hobbies, etc. and respond to the user the details they have provided.

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
address = input("Enter your address: ")
dob = input("Enter you Date of Birth: ")
course_name = input("Enrolled Course Name: ")
is_resident = input("Are you a UK resident: ")

address_list = address.split(" ")
house_no = address_list[0]
# street_address = address_list[1 : -2]
post_code = address_list[-2] + " " + address_list[-1]

#house_no = address.split(" ")[0];
#post_code = address.split(" ")[-2] + " " + address.split(" ")[-1]
print(f"Hello {first_name} {last_name}.")
print(f"Your House Number is: {house_no}")
# print(f"Your Street Address is: {street_address}")
print(f"Your post code is {post_code}")
print("Your Date of Birth is: " + dob) # Another way of printing
print("You Are Enrolled in " + course_name + " and you have to be a " + is_resident)

```


