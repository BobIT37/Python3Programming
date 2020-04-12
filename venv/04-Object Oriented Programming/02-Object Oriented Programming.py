# Class
# User defined objects are created using the class keyword
# The class is a blueprint that defines the nature of a future object

'''
# Create a new object type called Sample
class Sample:
    pass

# Instance of Sample
x = Sample() # class object

print(type(x))

'''

class Computer():

 # Varibales == attributes

 model = "Apple"
 color = "Gray"
 ram = "8 gb"
 storage = "256 gb"

# Class Object

computer1 = Computer()
print(computer1)

#Call variables
print(computer1.model)
print(computer1.color)
print(computer1.ram)
print(computer1.storage)

computer2 = Computer()
print(computer2.model)
print(computer2.color)
print(computer2.ram)
print(computer2.storage)

#How to assign different values for object
#Functions == methods
print(dir(computer1))

# __init__

