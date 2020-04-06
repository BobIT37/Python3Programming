#args and kwargs

def myfunc(a,b):
    return sum((a,b)) * .05
result = myfunc(40,60)
print(result)

def myfunc(a=0,b=0,c=0,d=0):
    return sum((a,b,c,d)) * .05
result2= myfunc(40,60,20)
print(result2)

# *args
# When a function parameter starts with an asterisk it allows for an arbitrary number of arguments,
# and the function takes them in as a tuple of values

def myfunc(*args):
    return sum(args) * .05
result3 = myfunc(40,60,20)
print(result3)

def myfunc(*spam):
    return sum(spam)*.05
result4 = myfunc(40,60,20)
print(result4)

# **kwargs
def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print(f"my favorite fruit is {kwargs['fruit']}")
    else:
        print("I don't like fruit")
myfunc(fruit='pineapple')
myfunc()

# *args and **kwargs

def myfunc (*args, **kwargs):
    if 'fruit' and 'juice' in kwargs:
        print(f"i like {' and '.join(args)} and my favorite fruit is {kwargs['fruit']}")
        print(f"may I have some {kwargs['juice']} juice?")
    else:
       pass
myfunc('eggs', 'spam', fruit='cherries', juice='orange')