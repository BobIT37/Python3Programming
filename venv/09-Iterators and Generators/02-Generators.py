"""
Generators allow us to generate as we go along, instead of holding everything in memory.

Generator functions allow us to write a function that can send back a value and then later resume
to pick up where it left off. This type of function is a generator in Python, allowing us to generate
a sequence of values over time.

The main difference in syntax will be the use of a yield statement.

In most aspects, a generator function will appear very similar to a normal function.
The main difference is when a generator function is compiled they become an object
that supports an iteration protocol. That means when they are called in your code
they don't actually return a value and then exit. Instead, generator functions will
automatically suspend and resume their execution and state around the last point of value generation.

The main advantage here is that instead of having to compute an entire series of values up front,
the generator computes one value and then suspends its activity awaiting the next instruction.
This feature is known as state suspension.

"""

#Generator function for the cube of numbers (Power of 3)

def gencubes(n):
    for num in range(n):
        yield num**3

for x in gencubes(10):
    print(x)

def genfibon(n):
   a = 1
   b = 2
   for i in range(n):
       yield a
       a,b = b, a+b # 1 1 2 3 5 8 13....

for num in genfibon(10):
    print(num)

def fibon(n):
    a = 1
    b = 1
    output = []

    for i in range(n):
        output.append(a)
        a,b = b, a+b
    return output

print(fibon(10))

# next() iter()

def simple_gen():
    for x in range(3):
        yield x

g = simple_gen()

print(next(g))
print(next(g))
print(next(g))


s = 'hello'
for let in s:
    print(let)

#print(next(s))

s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
