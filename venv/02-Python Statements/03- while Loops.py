#While loop

#Example

x = 0

'''
while x < 10:  # 0 1 2 3 4 5 6 7 8 9 10
    print('x is currently : ', x)
    print(' x is still less than 10, adding 1 to x')
    x+=1

while x < 10:  # 0 1 2 3 4 5 6 7 8 9 10
    print('x is currently : ', x)
    print(' x is still less than 10, adding 1 to x')
    x+=1

else:
    print('All Done!')
    
'''
# break continue pass

# break: breaks out of the current closest enclosing loop
#continue: goes to the top of the closest enclosing loop
# pass: does nothing at all

while x < 10:  # 0 1 2 3 4 5 6 7 8 9 10
    print('x is currently : ', x)
    print(' x is still less than 10, adding 1 to x')
    x+=1
    if x == 3:
        print('x == 3')
        break
    else:
        print('continuing...')
        continue



