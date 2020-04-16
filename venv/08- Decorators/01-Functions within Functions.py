# Functions within Functions

# In python, as you know functions are also objects
# We can assign a function to a variable
"""
def hello(name):
    print("Hello ", name)

hello("Bob")

hello1 = hello

print(hello)
print(hello1)

hello1("ilhan")

del hello
print(hello)

print(hello1)


"""
def function1(): #main function
    def function2(): #Local function
        print("Hello from small function")
    print("hello from big function")
    function2()

function1()
#function2()

def function3(*args): #args (1,2,3,4,5,) #main function

    def sum_Numbers(args): #(1,2,3,4,5) # local function
        sum = 0
        for i in args:
            sum += i
        return sum
    print(sum_Numbers(args))

function3(1,2,3,4,5,6,7)

def hello(name='Robert'):
    print('The hello() function has been executed')

    def greet():
        return '\t This is insidee the greet() function'

    def welcome():
        return '\t This is inside the welcome() function'

    print(greet())
    print(welcome())
    print('Now we are back inside the hello() function')

hello()

def hello2(name='Bob'):

    def greet():
        return '\t This is inside the greet() function'

    def welcome():
        return '\t This is inside the welcome() function'

    if name == 'Bob':
        return greet()
    else:
        return welcome()

#x = hello2
#print(x())
print(hello2('Bob'))
print(hello2(name='Robert'))
print(hello2())

def hello():
    return 'Hi Bob'

def other(func):
    print('Other code would go here')
    print(func())
    
other(hello)