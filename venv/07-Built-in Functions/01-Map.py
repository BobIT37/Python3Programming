# map() takes in two or more arguments
# a function and one or more iterables
# syntax
# map(function, iterable...)
# map returns iterator

my_pets = ["alfred", "tabitha", "william", "arla"]
uppered_pets = []

''' 
for pet in my_pets:
    pet_ = pet.upper()
    uppered_pets.append(pet_)
print(uppered_pets)
'''
uppered_pets = list(map(str.upper, my_pets))
print(uppered_pets)

def fahrenheit(celsius):
    return (9/5)*celsius + 32
temps = [0, 22.5, 40, 100]

F_temps = map(fahrenheit, temps)
print(list(F_temps))

# map() with multiple iterables

a = [1,2,3,4]
b = [5,6,7,8]
c = [9,10,11,12]

print(list(map(lambda x,y,z:x+y+z,a,b,c)))







