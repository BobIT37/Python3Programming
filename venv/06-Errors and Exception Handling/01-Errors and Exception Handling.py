#try except finally, raise

"""
try:
  You do your operations here...
except ExceptionI:
  If there is ExceptionI, then execute this block
except ExceptionII:
  if there is ExceptionII, then execute this block
  ...
else:
  if there is no exception then execute this block

"""
"""
try:
    a = int("23456ryryf")
    print("Here is int section")
except:
    print("You have an exception")
print("Your bloks was ended")

"""
'''
try:
    a = int("23456ryryf")
    print("Here is int section")
except ValueError:
    print("You have an exception")
print("Your bloks was ended")

'''

#a = int("2345ertyty")
#print(2/0)
'''
try:
    a = int(input("NUmber 1: "))
    b = int(input("Number 2: "))
    print(a/b)
except ValueError:
    print("Please enter correct value")
except ZeroDivisionError:
    print("You cannot divide a number to 0")
 +++++++++++   
 try:
    a = int(input("Number 1: "))
    b = int(input("Number 2: "))
    print(a/b)
except (ValueError, ZeroDivisionError):
    print("Zero division or Value error")
   ++++++++ 
try:
    a = int(input("Number 1: "))
    b = int(input("Number 2: "))
    print(a/b)
except ValueError:
    print("Please enter correct value")
except ZeroDivisionError:
    print("You cannot divide a number to 0")
finally:
    print("Finally block works in any condition")    
 
'''
#raise

def reverseString(s):
    if(type(s) != str):
        raise ValueError("Please enter correct value")
    else:
        return s[::-1]

try:
   print(reverseString("Python"))
except ValueError:
   print("An exception occured")




