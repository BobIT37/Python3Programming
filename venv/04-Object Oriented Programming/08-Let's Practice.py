class Employee():

    def __init__(self, name, salary, department):
        print("This init in Employee class")
        self.name= name
        self.salary = salary
        self.department = department

    def showInfo(self):
       print("Employee information: ")
       print("Name: {} \nSalary: {} \nDeaprtment: {}\n".format(self.name,
                                                               self.salary,
                                                               self.department))

    def changeDepartment(self, new_Department):
         print("Department is changing...")
         self.department = new_Department

class Manager(Employee):
     pass

manager1 = Manager("Bob Lerry", 3000, "IT")
manager1.showInfo()

manager1.changeDepartment("HR")
manager1.showInfo()