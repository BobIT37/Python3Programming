# filter()
#This function will be applied to every element of the iterable.
# Only if the function returns True will the element of the iterable
# be included in result
# numbers = [1,2,3,4,5,6,7,8,9,10]
# filter(function, list)

#First let's make a function
def even_check(num):
    if num%2 == 0:
        return True

lst   = range(20)
print(list(filter(even_check, lst)))