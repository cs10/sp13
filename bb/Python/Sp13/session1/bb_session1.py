##! /usr/bin/env python3#! /usr/bin/env python3

# CS10 Beyond Blocks Session 1
# Python 3
# May 2, 2013 by Michael Ball
# CC-BY-NC-SA 3.0 Unported License
# hahahahaha blah blah blah

import math
from fib import fib
from fib import i_fib as iterfib

# TODO:
"""
    Multiline comments
    Strings
Functions
    Simple stuff
    Math
Types
Importing
Doctests?
nature of a script.
Map-Filter-Reduce
Lists/Tuples/Dicts/Sets
"""

# This is a simple comment!
# Comments are GOOD!

def fact(n):
    """
    Return the factorial (n!) of the input n.
    This is a special comment called a doctest which will be explored later.
    >>> fact(0)
    1
    >>> fact(5)
    120
    >>> fact(2)
    2
    fact(-100) #factorial isn't defined here, but our function is!
    1
    """
    if n < 1:
        return 1
    else:
        return n * fact(n - 1)

def do_nothing(x):
    # this function will never do anything
    if False:
        return x

def count_down(x):
    while (x > 0):
        print(x)
        x -= 1

def count_recur(x):
    print(x)
    if (x > 0):
        x -= 1
        count_recur(x - 1)

def count_another_way(x):
    for i in range(x, 0, -1):
        print(i)

print("Hello! Welcome to Beyond Blocks Session 1!\n")
print("Today, we're going to learn about Python!\tYay!\n\n")

print("Did you know that factorial(5) is {0}?!".format(fact(5)))

name = "Michael" # note the quotes

print("Oh, by the way, my name is ", name, ".\n")
name += " Ball"
print("Actually, my full name is ", name, ".\n")
print("Let's count down from 10!")
count_down(10)
print("Wow!\n Let's do it again!")
count_recur(10)
print("But let's see it a 3rd way!")
count_another_way(10)

# The awesome thing about python is that it just runs a script.
print(5/2) # some random math.
print(5//2)
print(5%2)
print(5**2)

def learn_pow(n):
    i = 0
    while (i < n):
        print(2**i)
        i += 1

def weird_identity(x):
    return (x//2*2 + x%2) # this is just a fun thing. It works for any numb.

print(weird_identity(4))

# This is weird!
print(print("Whoa...wat"))

# Scope and environments
x = 4
print("Let's learn powers of 2!")
print(x)
print("x")
learn_pow(x)
# didn't learn_pow modify the variable we put in?
# it might look like it did, but it didn't really.
# this is called "scoping"
x += 20
print("And some more! How high can you go?")
learn_pow(x)

print("Who likes pie? I can eat lots!")
print(math.pi)

# CS10 Beyond Blocks Session 1
# Python 3
# May 2, 2013 by Michael Ball
# CC-BY-NC-SA 3.0 Unported License
# hahahahaha blah blah blah

import math
from fib import fib
from fib import i_fib as iterfib

# TODO:
"""
    Multiline comments
    Strings
Functions
    Simple stuff
    Math
Types
Importing
Doctests?
nature of a script.
Map-Filter-Reduce
Lists/Tuples/Dicts/Sets
"""

# This is a simple comment!
# Comments are GOOD!

def fact(n):
    """
    Return the factorial (n!) of the input n.
    This is a special comment called a doctest which will be explored later.
    >>> fact(0)
    1
    >>> fact(5)
    120
    >>> fact(2)
    2
    fact(-100) #factorial isn't defined here, but our function is!
    1
    """
    if n < 1:
        return 1
    else:
        return n * fact(n - 1)

def do_nothing(x):
    # this function will never do anything
    if False:
        return x

def count_down(x):
    while (x > 0):
        print(x)
        x -= 1

def count_recur(x):
    print(x)
    if (x > 0):
        count_recur(x - 1)

def count_another_way(x):
    for i in range(x, 0, -1):
        print(i)

print("Hello! Welcome to Beyond Blocks Session 1!\n")
print("Today, we're going to learn about Python!\tYay!\n\n")

print("Did you know that factorial(5) is {0}?!".format(fact(5)))

name = "Michael" # note the quotes

print("Oh, by the way, my name is ", name, ".\n")
name += " Ball"
print("Actually, my full name is ", name, ".\n")
print("Let's count down from 10!")
count_down(10)
print("Wow!\n Let's do it again!")
count_recur(10)
print("But let's see it a 3rd way!")
count_another_way(10)

# The awesome thing about python is that it just runs a script.
print(5/2) # some random math.
print(5//2)
print(5%2)
print(5**2)

def learn_pow(n):
    i = 0
    while (i < n):
        print(2**i)
        i += 1

def weird_identity(x):
    return (x//2*2 + x%2) # this is just a fun thing. It works for any numb.

print(weird_identity(4))

# This is weird!
print(print("Whoa...wat"))

# Scope and environments
x = 4
print("Let's learn powers of 2!")
print(x)
print("x")
learn_pow(x)
# didn't learn_pow modify the variable we put in?
# it might look like it did, but it didn't really.
# this is called "scoping"
x += 20
print("And some more! How high can you go?")
learn_pow(x)

print("Who likes pie? I can eat lots!")
print(math.pi)! /usr/bin/env python3
#! /usr/bin/env python3

# CS10 Beyond Blocks Session 1
# Python 3
# May 2, 2013 by Michael Ball
# CC-BY-NC-SA 3.0 Unported License
# hahahahaha blah blah blah

import math
from fib import fib
from fib import i_fib as iterfib

# TODO:
"""
    Multiline comments
    Strings
Functions
    Simple stuff
    Math
Types
Importing
Doctests?
nature of a script.
Map-Filter-Reduce
Lists/Tuples/Dicts/Sets
"""

# This is a simple comment!
# Comments are GOOD!

def fact(n):
    """
    Return the factorial (n!) of the input n.
    This is a special comment called a doctest which will be explored later.
    >>> fact(0)
    1
    >>> fact(5)
    120
    >>> fact(2)
    2
    fact(-100) #factorial isn't defined here, but our function is!
    1
    """
    if n < 1:
        return 1
    else:
        return n * fact(n - 1)

def do_nothing(x):
    # this function will never do anything
    if False:
        return x

def count_down(x):
    while (x > 0):
        print(x)
        x -= 1

def count_recur(x):
    print(x)
    if (x > 0):
        count_recur(x - 1)

def count_another_way(x):
    for i in range(x, 0, -1):
        print(i)

print("Hello! Welcome to Beyond Blocks Session 1!\n")
print("Today, we're going to learn about Python!\tYay!\n\n")

print("Did you know that factorial(5) is {0}?!".format(fact(5)))

name = "Michael" # note the quotes

print("Oh, by the way, my name is ", name, ".\n")
name += " Ball"
print("Actually, my full name is ", name, ".\n")
print("Let's count down from 10!")
count_down(10)
print("Wow!\n Let's do it again!")
count_recur(10)
print("But let's see it a 3rd way!")
count_another_way(10)

# The awesome thing about python is that it just runs a script.
print(5/2) # some random math.
print(5//2)
print(5%2)
print(5**2)

def learn_pow(n):
    i = 0
    while (i < n):
        print(2**i)
        i += 1

def weird_identity(x):
    return (x//2*2 + x%2) # this is just a fun thing. It works for any numb.

print(weird_identity(4))

# This is weird!
print(print("Whoa...wat"))

# Scope and environments
x = 4
print("Let's learn powers of 2!")
print(x)
print("x")
learn_pow(x)
# didn't learn_pow modify the variable we put in?
# it might look like it did, but it didn't really.
# this is called "scoping"
x += 20
print("And some more! How high can you go?")
learn_pow(x)

print("Who likes pie? I can eat lots!")
print(math.pi)
# CS10 Beyond Blocks Session 1
# Python 3
# May 2, 2013 by Michael Ball
# CC-BY-NC-SA 3.0 Unported License
# hahahahaha blah blah blah

import math
from fib import fib
from fib import i_fib as iterfib

# TODO:
"""
    Multiline comments
    Strings
Functions
    Simple stuff
    Math
Types
Importing
Doctests?
nature of a script.
Map-Filter-Reduce
Lists/Tuples/Dicts/Sets
"""

# This is a simple comment!
# Comments are GOOD!

def fact(n):
    """
    Return the factorial (n!) of the input n.
    This is a special comment called a doctest which will be explored later.
    >>> fact(0)
    1
    >>> fact(5)
    120
    >>> fact(2)
    2
    fact(-100) #factorial isn't defined here, but our function is!
    1
    """
    if n < 1:
        return 1
    else:
        return n * fact(n - 1)

def do_nothing(x):
    # this function will never do anything
    if False:
        return x

def count_down(x):
    while (x > 0):
        print(x)
        x -= 1

def count_recur(x):
    print(x)
    if (x > 0):
        count_recur(x - 1)

def count_another_way(x):
    for i in range(x, 0, -1):
        print(i)

print("Hello! Welcome to Beyond Blocks Session 1!\n")
print("Today, we're going to learn about Python!\tYay!\n\n")

print("Did you know that factorial(5) is {0}?!".format(fact(5)))

name = "Michael" # note the quotes

print("Oh, by the way, my name is ", name, ".\n")
name += " Ball"
print("Actually, my full name is ", name, ".\n")
print("Let's count down from 10!")
count_down(10)
print("Wow!\n Let's do it again!")
count_recur(10)
print("But let's see it a 3rd way!")
count_another_way(10)

# The awesome thing about python is that it just runs a script.
print(5/2) # some random math.
print(5//2)
print(5%2)
print(5**2)

def learn_pow(n):
    i = 0
    while (i < n):
        print(2**i)
        i += 1

def weird_identity(x):
    return (x//2*2 + x%2) # this is just a fun thing. It works for any numb.

print(weird_identity(4))

# This is weird!
print(print("Whoa...wat"))

# Scope and environments
x = 4
print("Let's learn powers of 2!")
print(x)
print("x")
learn_pow(x)
# didn't learn_pow modify the variable we put in?
# it might look like it did, but it didn't really.
# this is called "scoping"
x += 20
print("And some more! How high can you go?")
learn_pow(x)

print("Who likes pie? I can eat lots!")
print(math.pi)