from random import shuffle
from random import randint
#shuffle the list "in place " meaning it wont return anything, instead it will effect the list passed
# randint retruns random integer in range [a,b], including both end points


# range() == to generate list

#range(0,11)  # 0-10

print(list(range(0,11)))
print(list(range(0,12)))

# to add step size (third parameter)
print(list(range(0,11,2))) # 0, 2 4 6 8 10
print(list(range(0,101,10)))

# enumerate adds counter to an iterable and returns it
print('**************************')
index_count = 0

for letter in 'abcde':
    print("At index {} the letter is {}".format(index_count,letter))
    index_count += 1

print('**********+++++++++************')
for i, letter in enumerate('abcde'):
    print("At index {} the letter is {}".format(i,letter))

# zip()  to iterate over two lists in parallel

print(list(enumerate('abcde')))

myList1 = [1,2,3,4,5]
myList2 = ['a', 'b', 'c', 'd', 'e']

print(zip(myList1, myList2))

print(list(zip(myList1, myList2)))
print('***********************************')
for item1, item2 in zip(myList1, myList2):
    print('For this tuple, first item was {} and second item was {}'.format(item1,item2))

print('x' in ['x', 'y', 'z']  )

# min max
myList3 = [10,20,30,40,100]
print(min(myList3))
print(max(myList3))

#random

shuffle(myList3)
print(myList3)

print(randint(0,100))
print(randint(0,100))

# input == to enter any value including text

print(input ('Enter your age: '))
print(input ('Enter your location: '))