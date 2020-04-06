#To create a String in Python we can use '' or ""

print('hello')
print("hello")

#Entire phrase
print("This is also String in Python")
print('This is also String in Python')

#Be Careful
print("I'm using single quotes")

#Define string variable
name = "ilhan"
print(name)
print(type(name))

print('use \n to print a new line')

s = 'hello world'
print(s)

#Show first element
print(s[0])

print(s[2])

#We can use a : to perform slicing which grabs everything up to a designated point

print(s[3:])
print(s[:3])
print(s[:])
print(s[:-1])
print(s[::1])
print(s[::2])

#We can use this to print a string backwards - reverse string
print(s[::-1])

#Concatenate

b = 'hello world'

b = b + ' concatenate me!'
print(b)

print('Addition: ', (2+1))

letter = 'z'
print(letter*10)

#Uppercase

m = 'my name is Ilhan'
print(m.upper())

#lowercase
print(m.lower())

#Split- split a string by blank space
print(m.split())

#split by a specific element
print(m.split('n'))

# .format()

print('Insert another string with curly brackets: {}'.format('The inserted string'))
print('My First name is ilhan and last name is: {}'.format('turkmen'))

#placeholders method %s
print("I'm going to inject %s here"%'something')

print("I'm going to inject %s text here, and %s text here."%('some', 'more'))

x, y = 'some', 'more'
print("I'm going to inject %s text here, and %s text here."%(x, y))

#Format conversion methods

print('He said his name was %s'%'Frank')
print('He said his name was %r'%'Frank')

# \t
print('I once caught a fish %s'% 'this \tbig')
print('I once caught a fish %r'% 'this \tbig')

# %s and %d
print('I wrote %s programs today'%3.75)
print('I wrote %d programs today'%3.75)

#Padding and precision of floating point numbers
print('Floating point numbers: %5.2f'%(13.144))
print('Floating point numbers: %5.0f'%(13.144))


