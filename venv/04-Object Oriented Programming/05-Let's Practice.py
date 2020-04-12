class Developer():

    def __init__(self, firstname, lastname, phone, salary, languagePro):
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone
        self.salary = salary
        self.languagePro = languagePro

    def info(self):

      print("""
      Developer information:
      
      Name : {}
      Lastname : {}
      Phone : {}
      Salary : {}
      Laguages : {}
      
      """.format(self.firstname, self.lastname, self.phone, self.salary, self.languagePro))

developer1 = Developer("Ilhan", "Turkmen", 201913213, 2500, ["Python", "Java", "Groovy", "JavaScript"])

developer1.info()
'''
print(developer1.firstname)
print(developer1.lastname)
print(developer1.phone)
print(developer1.salary)
print(developer1.languagePro)

'''
