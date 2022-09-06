#what is dictionaries

# It contain the key and value also immutable.

# create the Empty dictionaries, 


dic = dict()
print(type(dic))
dic = {}
print(type(dic))


# create the list of emails address based on user profile.

emails = {
    'Nataraj' : 'nataraj@gmail.com',
    'Vino'    : 'vino@gmail.com',
    'Rama'    :  'rama@gmail.com'
}

print(emails['Rama'])

# You cannot keep the similar key into dictionaries 

animals = {
    'dog' : 'dog',
    'cat' : 'cat',
    'elephant' : 'elephant',
    'dog' : 'dog1'
}

print(animals)
print(animals['dog'])

# we assign the integer value in key 

animals = {
    1 : 'dog',
    2 : 'cat',
    3 : 'cow'
}

print(animals[2])


# we assign the cannot assign the list value in key 

# animals = {
#     [1] : 'dog',
#     [2] : 'cat',
#     [3] : 'cow'
# }

# print(animals[2])


# assign the string into key

city_rating = {
    'banglore' : [7,8],
    'chennai'  : [7,8]
}


# assig the value to dictiories 

grades = {}

grades['John'] = 'A'
grades['Ram'] = 'B'

print(grades)


# update the value 

grades.update({'John' : '-A'})
print(grades)

# count the dictionaries value

print(len(grades))

# if condition 

for John in grades:
    print( "John got", grades['John'])
    
    
# del the value    

del(grades['John'])
print(grades)


# for loop and you get the key value

grades = {}

grades['bye'] = 'A'
grades['hello'] = 'B'

for el in grades:
    print(el)
    
    
# or both are similar output.

for el in grades.keys():
    print(el)
    
    
#using for loop get the dictionries value

for el in grades.values():
    print(el)
    
    
# Get the both value in dictionaries

for x,y in grades.items():
    print(x ,'got', y)