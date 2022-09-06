# Upper // Lower

text = "Hello I will back with strong"
print(text.upper())
print(text.lower())

# slice the string

value = text[0:5]
print(value)

# The isnumeric() method checks if all the characters in the string are numeric.

user_value = input("enter the number")

if user_value.isnumeric():
    print("you are enter the correct number")
else:
    print("You enter the sting")    

# you cannot use indexing to change individual characters within a string

# text[8] = 'i'