# # Data Collections
# # Lists
# # Tuples
# # Dict
#
# # Lists
# # syntax list_name = ["one", "two", "three"]
#
# #Apply DRY
# shopping_list = ["ketchup", "fanta", "eggs", "bread"]
# print(shopping_list)
# print(type(shopping_list))
# shopping_list.append('chicken')
# print(shopping_list)  # add an item to the list
# print(shopping_list[2])
# shopping_list[2] = "Icecream"  # replacing an item with another one in the list
# print(shopping_list)
# shopping_list.remove('fanta')  # removing an item from the list using value
# shopping_list.pop(1)  # removing an item from the list using index
# print(shopping_list)

# # Can list have multiple types
# multiple_type = [1, 2, 3, "One", "two", 4, "three"]
# print(multiple_type)
# print(multiple_type[2])

# Tuples
# Immutable - can't be changed - edited - added
# For e.g. In user_details Date Of Birth never change
# Syntax ("")
essentials = ("milk", "paracetamol", "drinks")
print(essentials)
print(type(essentials))

essentials[0] = "coffee"
print(essentials)

