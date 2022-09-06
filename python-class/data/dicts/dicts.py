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