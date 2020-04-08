# Function Practice Solutions

# Question 1 lesser of two evens

'''
def lesser_of_two_evens(a,b):

    if a%2 == 0 and b%2 == 0:
        #Both numbers are even
       if a < b:
           result = a
       else:
           result = b
    else:
       #one or both numbers are odd!
       if a > b:
           result = a
       else:
           result = b

    return result

print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))
'''
def lesser_of_two_evens(a,b):
    if a%2 ==0 and b%2 ==0:
        return min(a,b)
    else:
        return max(a,b)

print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))

#Question 2 Animal Checkers

def animal_crackers(text):
    wordlist = text.upper().split()
    print(wordlist)
    return wordlist[0][0] == wordlist[1][0]

print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy cangroo'))

#Question 3 twenty

def makes_twenty(n1,n2):
    return (n1+n2)==20 or n1 == 20 or n2 ==20

    '''
    if n1 + n2 == 20:
        return True
    elif n1 == 20:
        return True
    elif n2 == 20:
        return  True
    else:
        return False
    '''
print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))