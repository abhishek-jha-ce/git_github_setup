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

# Example_text = "abhishek here's sOme text wIth lOt's of text"
# # Count no. of occurrence
# print(Example_text.count("text"))
# # lower case and upper case and Capitalize
# print(Example_text)
# print(Example_text.lower())
# print(Example_text.upper())
# print(Example_text.capitalize())
# # replace
# print(Example_text.replace("wIth", ","))

# ### Concatenation & Casting
# - adding strings together
# - casting/converting data types

# # User data input
# first_name = "abhishek"
# last_name = "jha"
# salary = 40
#
# print(first_name)
# print(last_name)
# print(first_name.capitalize() + " " + last_name.capitalize())  # Concatenation
# print(first_name + " " + last_name + " earns a salary of £" + str(salary))  # Casting int to string before concatenating
# print(f"{first_name} {last_name} earns a salary of £{salary}")  # Another way of writing it

# Using what we have learned so far let's head back to our user_details_capture file and ensure we are using / casting
# the same type. Extend the capture further to grab details such as address (ensuring that a house number is correctly
# represented, hobbies, etc. and respond to the user the details they have provided.

# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# address = input("Enter your address: ")
# dob = input("Enter you Date of Birth: ")
# course_name = input("Enrolled Course Name: ")
# is_resident = input("Are you a UK resident: ")
#
# address_list = address.split(" ")
# house_no = address_list[0]
# # street_address = address_list[1 : -2]
# post_code = address_list[-2] + " " + address_list[-1]
#
# #house_no = address.split(" ")[0];
# #post_code = address.split(" ")[-2] + " " + address.split(" ")[-1]
# print(f"Hello {first_name} {last_name}.")
# print(f"Your House Number is: {house_no}")
# # print(f"Your Street Address is: {street_address}")
# print(f"Your post code is {post_code}")
# print("Your Date of Birth is: " + dob) # Another way of printing
# print("You Are Enrolled in " + course_name + " and you have to be a " + is_resident)


