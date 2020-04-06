#Constructing a Dictionary

#Make a dictionary with {} and : to signify a key and a value

my_dict = {'key1':'value1', 'key2':'value2'}
print(my_dict)
print(my_dict['key2'])

my_dict = {'key1': 123, 'key2': [12,23,34], 'key3':['item0', 'item1', 'item2']}
print(my_dict['key3'])
print(my_dict['key2'])

#call an index on that value
print(my_dict['key3'][1])

#Can then even call methods on that value
print(my_dict['key3'][0].upper())

print(my_dict['key1'])

#Subtract 123 from the value
my_dict['key1'] = my_dict['key1'] - 123
print(my_dict['key1'])

#Create a new Dictionary
d = {}

#Create a new key through assignment
d['animal'] = 'dog'

#Can do this with any object
d['answer'] = 42

print(d)

#Nested dictionary
d = {'key1': {'nestedKey': {'subnestkey': 'value'}}}
print(d['key1']['nestedKey']['subnestkey'])

d = {'key1': 1, 'key2': 2, 'key3': 3}

#Methods

#keys is a method to return a list of all keys
print(d.keys())

#value is method to grab all values
print(d.values())

#items is a method to return tuples of items
print(d.items())
