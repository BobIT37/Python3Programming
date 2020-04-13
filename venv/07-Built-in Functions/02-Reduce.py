# reduce()

# Syntax
# reduce(func, iterable[, initial]

from functools import reduce

def sumOfNum(x,y):
    return x + y

print(reduce(sumOfNum, [12, 18, 20, 10]))

numbers = [3,4,6,9,34,12]

def custom_sum(first, second):
    return first + second
result = reduce(custom_sum, numbers)
print(result)


