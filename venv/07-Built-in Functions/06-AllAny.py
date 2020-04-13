"""
all() and any() are built-in functions in Python that allow us to conveniently
check for boolean matching in an iterable.

all() will return True if all elements in an iterable are True.

any() will return True if any of the elements in the iterable are True.

"""

lst = [True, True, False, True]

print(all(lst))
print(any(lst))