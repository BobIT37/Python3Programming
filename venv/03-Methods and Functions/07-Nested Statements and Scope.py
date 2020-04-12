# Nested Statements and Scope


x = 25 #global

def printer():
    x = 50 #local variable
    return x

print(x)
print(printer())

'''
LEGB Rule:

L: Local — Names assigned in any way within a function (def or lambda), and not declared global
   in that function.
E: Enclosing function locals — Names in the local scope of any and all enclosing functions
   (def or lambda), from inner to outer.
G: Global (module) — Names assigned at the top-level of a module file, or declared global
   in a def within the file.
B: Built-in (Python) — Names preassigned in the built-in names module : open, range, SyntaxError,...

'''

name = "this is a global name"

def greet():

    name = 'Sammy'

    # Enclosing function (inner method)
    def hello():
        print('Hello '+ name)

    hello()

greet()

#global
print(name)

#Built in
print(len(name))

#local variables

x = 50 #global
    
def func(x):
    print('x is ', x)
    x = 2 #local
    print('Changed local x to ', x)

func(x)
print('x is still ', x)