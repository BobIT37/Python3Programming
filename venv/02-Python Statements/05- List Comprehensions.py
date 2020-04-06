# List Advanced methods

#Example

# Grab every letter in String 'word' 'w', 'o', 'r', 'd'

lst = [x for x in 'word']
print(lst)

#Example
#Square numbers in range and turn into list

lst = [x**2 for x in range (0,11)]
print(lst)

#Example
# check for even numbers in a range

lst = [x for x in range(0,11) if x % 2 == 0]
print(lst)

#Example
# convert celsius to Fahrenheit
celsius = [0,10,20.1,34.5]

fahrenheit = [((9/5)*temp +32) for temp in celsius]
print(fahrenheit)

#nested list

lst = [x**2 for x in [x**2 for x in range(11)]]
print(lst)


