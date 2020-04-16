"""
In Python, functions are the first class objects, which means that –

Functions are objects; they can be referenced to, passed to a variable and returned
from other functions as well.

Functions can be defined inside another function and can also be passed as argument to another function.

Decorators are very powerful and useful tool in Python since it allows programmers to modify
the behavior of function or class. Decorators allow us to wrap another function in order
to extend the behavior of wrapped function, without permanently modifying it.

In Decorators, functions are taken as the argument into another function and then
called inside the wrapper function.

"""

def new_decorator(func):

    def wrap_func():
        print('Code would be here, before executing the func')

        func()

        print("Code here will execute after the func()")

    return wrap_func

def func_needs_decorator():
    print("this function is in need of decorator")

func_needs_decorator()

func_needs_decorator = new_decorator(func_needs_decorator)
func_needs_decorator()

print("******************************")
@new_decorator
def func_needs_decorator():
    print("this function is in need of decorator...")

func_needs_decorator()

#Decorators allow us to write code in shorter way
#You can avoid duplicate code using decorator



