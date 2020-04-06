
#if elif and else

#First Example

if True:
    print('it was true!')

#Second example
x = False

if x:
    print('x was True!')
else:
    print('i will be printed in any case where x is not true')

#Third Example
loc = 'Bank'

if loc == 'Auto Shop':
    print("Welcome to the Auto shop")
elif loc == 'Bank':
    print('Welcome to the bank')
else:
    print('Where are you?')

#Fourth Example
person = 'Sammy'

if person == 'Sammy':
    print('Welcome Sammy!')
else:
    print('Welcome, what is your name?')

#Fifth Example

person = 'George'

if person == 'Sammy':
    print('Welcome Sammy')
elif person == 'George':
    print('Welcome, George!')
else:
    print('Welcome, what is your name?')
