# map filter and lambda expressions

# map function

def square(num):
    return num**2
my_nums = [1,2,3,4,5]

print(map(square,my_nums))

#loop concept with map
for item in map(square, my_nums):
    print(item)
#List concept with map
print(list(map(square, my_nums)))

def splicer(myString):
    if len(myString) % 2 == 0:
        return 'even'
    else:
        return myString[0]
myNames = ['John', 'Cindy', 'Sarah', 'Kelly', 'Mike']
print(list(map(splicer, myNames)))

# filter function
def check_even(num):
    return num % 2 == 0
nums = [0,1,2,3,4,5,6,7,8,9,10]

print(filter(check_even, nums))
#list concept with filter
print(list(filter(check_even, nums)))

#loop concept with filter
for n in filter(check_even, nums):
    print(n)

# lambda expression

#square = lambda num : num**2

print(list(map(lambda num : num ** 2, nums)))

print(list(filter(lambda n: n % 2 == 0, nums)))

print(list(map(lambda x: x[0], myNames)))

