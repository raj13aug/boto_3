#The biggest difference between lists and tuples is that lists are mutable and tuples are immutable.

#Incidentally string and python are also immutable, I explained how you can access individual characters in a string but I also told you can't replace

from ast import Num


empty_tuples = ()
print(type(empty_tuples))

one_tuple = 1,
print(type(one_tuple))

three_tuple = 1,2,3
print(type(three_tuple))

# udate the exiting the value

user_data = ('John', 'American', 1964)
user_data = ('Raj', 'India', 36)

print(user_data)

# cannot the append the value and delete

#user_data.append('work')
#del user_data[0]

# access the value

print(user_data[0])


# combined the both tuples

value_1 = (1,2,3,4)
value_2 = (5,6,7,8)

combined = value_1 + value_2
print(combined)

# for loop

user_data = (1,2,3,4,5,6,7,8)

for i in user_data:
    print(i)
    
# multiple 

number = (0,1) * 10
print(number)