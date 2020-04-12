class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Dog:

    def __init__(self, name):
        self.name =name

    def speak(self):
         return self.name + ' says woof'

class Cat:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name+ ' says meow'

niko = Dog('niko')
felix = Cat('felix')

print(niko.speak())
print(felix.speak())

for pet in [niko, felix]:
    print(pet.speak())

def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
pet_speak(felix)

fido = Dog('fido')
isis = Cat('isis')

print(fido.speak())
print(isis.speak())
