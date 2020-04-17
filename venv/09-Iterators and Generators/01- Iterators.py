"""
In this part of the Python tutorial, we work with iterators and generators.
Iterator is an object which allows a programmer to traverse through all the elements of a collection,
regardless of its specific implementation.

In Python, an iterator is an object which implements the iterator protocol.
The iterator protocol consists of two methods. The __iter__() method, which must return
the iterator object, and the next() method, which returns the next element from a sequence.

Iterators have several advantages:

Cleaner code
Iterators save resources

"""

list1 = [1,2,3,4,5]

#print(dir(list1))

iterator = iter(list1)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
#print(next(iterator))

list2 = [6,7,8,9,10]
for i in list2:
    print(i)

list3 = [11,12,13,14,15]

iterator = iter(list3)

while True:
    try:
        print(next(iterator))

    except StopIteration:
        break

#How to create your own iterator

class RemoteControl():
    def __init__(self, channellist):
        self.channellist = channellist
        self.index = -1

    def __iter__(self):
       return self
    def __next__(self):
        self.index += 1
        if(self.index < len(self.channellist)):
            return self.channellist[self.index]
        else:
            self.index = -1
            raise StopIteration

remotecontrol = RemoteControl(["CNN", "ABC", "NBATV", "Bloomberg", "Fox"])

iterator = iter(remotecontrol)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

