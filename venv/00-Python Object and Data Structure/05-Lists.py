#Assign a list to an variable named my_List

my_List = [1,2,3]

my_List = ['A String', 23, 100.5, 'k']

print(len(my_List))

my_List = ['one', 'two', 'three', 4,5]

#Grab element at index 0
print(my_List[0])

#Grab index 1 and everything past it
print(my_List[1:])

#Grab everything Up TO index 3
print(my_List[:3])

print(my_List + ['new item'])

#Reassign
my_List = my_List + ['add new item permanently']
print(my_List)

#make the list double
print(my_List * 2)

print(my_List)

list1 = [1,2,3]

#append
list1.append('append me!')
print(list1)

#pop "pop off"
list1.pop(0)
print(list1)

#assign the popped element, remember default popped index is -1
popped_item = list1.pop()
print(popped_item)
#remaining list
print(list1)

new_list = ['a', 'e', 'x', 'b', 'c']
print(new_list)

#reverse
new_list.reverse()
print(new_list)

#sort
new_list.sort()
print(new_list)

#Nesting Lists

lst_1 = [1,2,3]
lst_2 = [4,5,6]
lst_3 = [7,8,9]

#make a list of lists to form a matrix
matrix = [lst_1,lst_2,lst_3]
print(matrix)

#grab first item in matrix
print(matrix[0])
print(matrix[0][0])

#List Comprehensions
first_col = [row[0] for row in matrix]
print(first_col)