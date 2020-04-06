import math

#Functions in Python

#How to create a function

#def == defining function

def name_of_function():
    print('hello')

name_of_function()

def say_hello():
    '''
     DOCSTRING: Information about the function
     INPUT: no input
     OUTPUT: hello, how are you?
    :return:
    '''
    print('hello, how are you?')

say_hello()
help(say_hello)

# Parameterized function

def greeting(name):
    print('Hello %s'%(name))
greeting('John')

#return for function
def add_num(num1,num2):
    return num1+num2
print(add_num(2,5))

result = add_num(3,7)
print(result)

result2 = add_num('one', 'two')
print(result2)

#prime number divisible 1 and itself
def is_prime(num):
    for n in range(2,num):
        if num % n == 0:
            print(num, ' is not prime')
            break
        else:
           print(num, ' is prime')
           break

is_prime(16)
is_prime(17)

# math class usage

def is_prime2(num):
    if num % 2 == 0 and num > 2:
        return False
    for i in range(3, int(math.sqrt(num))+ 1,2):
        if num % i == 0:
            return False
    return True

print(is_prime2(16))
print(is_prime2(17))