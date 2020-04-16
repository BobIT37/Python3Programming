
#Rule 1: Since a function is also an object, we can return this function
#        from another function


def function1(operator):

    def addition(*args):
        sum = 0
        for i in args:
            sum += i
        return sum

    def multiplication(*args):
        multiply = 1
        for i in args:
            multiply *= i
        return multiply

    if operator == "addition":
        return addition
    else:
        return multiplication

a = function1("addition")
print(a)

print(a(1,2,3,4,5))

b = function1("multiplication")
print(b)

print(b(1,2,3,4,5,6,7))

#Rule 2: We can send a function as an argument to another function due to
#        all functions are also an object in Python

def addition(a,b):
    return a + b
def subtraction(a,b):
    return a - b
def multiplication(a,b):
    return a * b
def division(a,b):
    return a/b

def mainFunction(func1,func2,func3,func4, operator):

    if(operator == "addition"):
        print(func1(3,4))
    elif(operator == "subtraction"):
        print(func2(10,3))
    elif(operator == "multiplication"):
        print(func3(3,4))
    elif(operator == "division"):
        print(func4(4,2))
    else:
        print("Invalid operator")

mainFunction(addition, subtraction, multiplication, division, "addition")
mainFunction(addition, subtraction, multiplication, division, "division")
mainFunction(addition, subtraction, multiplication, division, "multiplication")  