# __init__ == constructor

class Car():

    #Constructor __init__
    def __init__(self, model, year, cc, madeBy):
        self.model = model
        self.year = year
        self.cc = cc
        self.madeBy = madeBy

# Creat a class object
car1 = Car("Mercedes", 2017, 6, "Germany")
print(car1.model)
print(car1.year)
print(car1.cc)
print(car1.madeBy)

car2 = Car("GMC Terrain", 2016, 4, "USA")
print(car2.model)
print(car2.year)
print(car2.cc)
print(car2.madeBy)



