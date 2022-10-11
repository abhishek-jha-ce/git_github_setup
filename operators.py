# Let's see the operators in action
### Intro to Data types & Operators
# - `+` `-` `*` `/`
### Comparision Operators
# - > greater than
# - < less than
# - == True or False
# - >= greater than or equal
# - <= less than or equal
#
# a = 24
# b = 16
#
# print(a+b) # outcome added value of a & b
# print(a-b) # outcome substraction value of a & b
#
# # Comparison
# print(a>b) # True
# print(a<b) # False
#
# print(a!=b)

# # Built in Methods
# # DRY - Don't Repeat Yourself
# # - print()
# greeting = "Hello World!"
# print(greeting)
# print(greeting.isalpha())        # Check if the variable is alphabet Only
# print(greeting.islower())        # Check if the variable is in lowercase
# print(greeting.startswith('H'))  # Check if starts with a specified letter
# print(greeting.endswith('!'))    # Check if ends with a specified letter

# String
# String indexing - starts from 0
# H e l l o   W o r l d  !
# 0 1 2 3 4 5 6 7 8 9 10 11
#           -2-1

# greeting = "Hello World!"
# print(greeting)
# # len method checks the length of the string
# print(len(greeting))
#
# # Forward Indexing
# print(greeting[0:5])   # Prints Hello
# print(greeting[6:12])  # Prints World!
#
# # Reverse Indexing
# print(greeting[-12:-6]) # Prints Hello
# print(greeting[-6:])   # Prints World!

# Available String Method
# white_space = "lots of spaces at the end                                "
# print(len(white_space))
# # strip() removes white space
# print(len(white_space.strip())) # this will remove all the white at the end.

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



