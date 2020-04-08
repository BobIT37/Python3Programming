# Function Level 2 Solutions

def has_33(nums):
    for i in range (0, len(nums)-1):

        if nums[i:i+2] == [3,3]:
            return True
    return False

print(has_33([1,3,3]))
print(has_33([1,3,1,3]))

def paper_doll(text):
    result = ''
    for char in text:
        result += char * 3
    return result

print(paper_doll('hello'))
print(paper_doll('Mississippi'))

def blackJack(a,b,c,):
    if sum((a,b,c,)) <= 21:
        return sum((a,b,c,))
    elif sum((a,b,c,)) <=31 and 11 in (a,b,c,):
        return sum((a,b,c)) - 10
    else:
        return 'BUST'

print(blackJack(5,6,7))
print(blackJack(9,9,9))
print(blackJack(9,9,11))

