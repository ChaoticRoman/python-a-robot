# This is a comment, it serves for human reader of this file only


## Python has statements
print("Hello world!")
a = "Python is cool"
b, c = 10, 10.0
d = b**2
is_it_fine = True
is_it_not_fine = not is_it_fine  # Python is case-sensitive, e.g.
                                 # using IS_IT_FINE would be error


## Python has if, else, for and while as any other language
if 1 < 2 and 42 and "abc":  # most types can be directly used as a boolean
    print(a)
else:
    pass  # pass does nothing

variable = "abc" or nonsense  # python uses lazy evaluation, i.e.
                              # when "abc" is True, nonsense isn't evaluated

for i in range(3):
    print(i, end=" ")  # no new line in the end

print()  # new line here

collector, new_text = "", True
while new_text:
    new_text = input(
        "Give me some text and press enter (empty string terminates this):"
    )
    collector += new_text

if collector == "Python is great":
    print("You wrote:", collector)
elif collector:  # non-empty string is True
    print("You wrote:", collector)
else:
    print("You wrote nothing")


## for and while loops have else clause in Python!

# for: else clause is exectued after iteration over all items

for i in range(0):
    break  # break terminates the loop
else:
    print('This is reached.')

for i in range(0):
    continue  # continue skip rest of the current 
else:
    print('This is reached too.')

for i in range(1):
    break
else:
    print('This is not reached, guess why!')

# while: else is executed when condition becomes false
text = ""
while not text:
    text = "abc"
else:
    print('This is reached as well.')

while True:
    break
else:
    print('This is not reached, guess why!')


## Python has lot of nice built-in data types:

# integers and floating point numbers
i = -42
f1, f2 = 42.0, 4.2e1

import math

# https://docs.python.org/3/library/math.html#math.isclose
print(math.isclose(f1, f2))

print(type(math.nan), type(math.inf), type(-math.inf))
print(1 / math.inf)

# strings with lot of build-in function and slices too
a = "Python is hard!".replace("hard", "easy")
print(a)
print(a[:6] + a[-1])  # slices are nice,
                      # you can have range or single character
                      # negative slice counts from the end
x = "abcdef"
print(x, "reversed is", x[::-1])  # you can also specify step, negative step goes backward

print("Surprise:", x[:-1:-1])  # however it can be confusing sometimes
# Explanation: https://stackoverflow.com/a/41430981

print("Hello!".find("!"))  #  strings have useful functions, see "pydoc3 str" or help(str)

print("Nice formatting, look: {}, {}, {:.2f}".format("abc", 20, 20.55555))

print("Old formatting works too: %s, %d, %.2f" % ("abc", 20, 20.55555))

# Lists are very useful when dealing with lot of stuff
empty_list = []
some_list = [1, 2, 3, 'abc']  # you can mix different data types in single list
                              # however it is usually bad idea

print(len(some_list))  # length of list is common operation

some_list = some_list[:-1]  # you can use slices too, here we get [1, 2, 3]
print(some_list)

some_list.append(-3)  # adding elements
some_list += [0]  # ok too, but less efficient
print(some_list)

print("Sorted:", sorted(some_list))  # this returns a new sorted list and prints it
print("Original:", some_list)  # but original is unchanged
some_list.sort()  # this is in-place sorting
print("After in-place sort:", some_list)

# there are lot of nice functions for any type, for overview just skim
# pydoc3 list
# pydoc3 str
# ...

# tuples are immutable objects
tup = 1, 2
print("Some tuple:", tup)
print("Second item:", tup[1])

a, b = tup  # this notation is often useful
a, b = b, a  # switching content of two variables
print(a, b)

# Dictionaries are often very useful for key -> value mappings
d = dict()
d['a'] = 'A'
d['b'] = 'B'

other_dict = {0: 10, 10: 20}

for key in other_dict:  # you can iterate over keys in dictionary
    print(key, "->", other_dict[key])

# There is special noneType with only one value
none_at_all = None

if not none_at_all:
    print("None is evaluated as false")

# there are boolean types
t, f = True, False
print("Any:", any([t, f]))  # any is useful substitute for chained "or"
print("All:", all([t, f]))  # all is for chained "and"

# and there are lot other data types:
# complex, set, frozenset, bytes, Ellipsis, methods, classes, functions, modules, etc...
# data types are implemented as classes so you can simply make your own

## there were already presented some built-in functions
# you can print list of all of them by
print(dir(__builtins__))


## You can define your own functions of course

def f():
    """This function prints something and return nothing."""  # this is called docstring
    print('Function has been called')                         # and it is good practice to use it

f()  # calls function
a = f()  # calls function and save its return value
print(a)  # Guess, what is here!

# functions can get arguments and return values
def sum_it(a, b):
    """Sums two numbers and return result"""
    return a + b

print("1 + 1 =", sum_it(1, 1))


# you can specify arbitrary number of arguments, notice we are redefining sum_it above
def sum_it(*args):
    """Sums numbers and return result."""
    result = 0
    for num in args:
        result += num
    return result

print("1 + 2 + 3 =", sum_it(1, 2, 3))

# instead of this, you can also unpack list (or tuple)
print("1 + 2 + 3 =", sum_it(*[1, 2, 3]))

# you can have keywords arguments too
def multiply(a, b, cast_to_float=None):
    if cast_to_float:
        return float(a * b)
    else:
        return a * b

print(
    multiply(1, 1),
    multiply(1, 1, True),
    multiply(1, 1, cast_to_float=True),
)

# and you can have arbitrary arguments, both positional and keywords
def print_number_of_args(*args, **kwargs):
    p, k = len(args), len(kwargs)
    print("Positional arguments count:", p)
    print("Keyword arguments count:", k)  # kwargs is dictionary
    print("Total args count:", p + k)

print_number_of_args(1, 2, 3, a=1, b=2)

# scope of functions
x = 5
def print_x():
    print(x)  # you can access value in outer scope for read
print_x()

def write_x():
    x = 6  # but you can't just overwrite it
write_x()
print_x()  # damn, five again

def write_x():
    global x  # but you can specify that you mean global variable and it works
    x = 6
write_x()
print_x()  # finally six

print("For nested functions:")
def nested():
    x = 0
    def write_x():  # we are NOT redefining write_x above, it is proteced by local scope
        nonlocal x  # x is nonlocal variables = one scope above, but not global
        x = 42
    write_x()  # calls write_x in this scope
    print(x)   # print x in this scope
    print_x()  # calls print_x in global scope, print x in global scope too

nested()

print('Closures:')
x = 5
def f():
    x = 45
    def g():
        print(x)
    print(g.__closure__)
    print(g.__closure__[0].cell_contents)
    return g

a = f()
a()
x = 10
a()

print('Decorators:')
def decorate(f):
    print('We just decorated some function')
    return f

@decorate
def hi():
    print('Hi!')

print(hi())

print('Parametric decorators:')
def get_decorator(count, decor_above, decor_below):
    def decorator(f):
        print(count * decor_above)
        result = f()
        print(count * decor_below)
        def return_result():
            return result
        return return_result
    return decorator

@get_decorator(16, 'v', '^')
def hello():
    print('Hello!')
    return 42

a = hello()
print(a)
# Context managers are useful when you would like to have some set up and tear down functions

# reading files old way
f = open('basics.py')
text = f.read()
f.close()  # it is fine, but people often forget to close the file

# with context manager
with open('basics.py') as f:
    text = f.read()

print('First line:', text.split('\n')[0])  # print first line

# there are lot of use cases as you will see further

# you can define your own context managers using __enter__
# and __exit__ magic methods, see further


## List comprehension
squares = [x**2 for x in range(10)]
print(squares)

evens = [x for x in range(10) if x % 2 == 0]
print(evens)


## Generators: iterator that "returns" one element at time
# save memory, can't use indices, slices, len and similar
def gen():
    """This is a function that returns generator"""
    for i in range(10):
        yield i**2  # just use yield instead of return

g = gen()
for i in g:
    print(i, end=" ")
print()
print('Now g is empty:')
for i in g:
    print(i, end=" ")

# we can have even infinite generators
def get_squares_generator():
    i = 0
    while True:
        yield i**2
        i += 1

print(get_squares_generator)

g = get_squares_generator()  # g is a generator
print(g)

print(next(g), next(g), next(g))

# it is nice when you need e.g. process really big file line by line
def process_big_file_line_by_line(filename):
    with open(filename) as f:
        for line in f:
            print(line, end='')  # some processing, here we just print

process_big_file_line_by_line('README.md')

def process_big_file_by_chunks(filename, chunk_size=64):
    def generator():
        with open(filename, 'rb') as f:
            while True:
                data = f.read(chunk_size)
                if not data:
                    break
                yield data

    for chunk in generator():
        print(chunk)  # some processing, here we just print

process_big_file_by_chunks('README.md')

# there is something similar to list comprehension, using round brackets will result in generator
squares = (i**2 for i in range(3))
print(squares)  # doesn't work :(

for i in squares:  # this does :)
    print(i)

for i in squares:  # prints nothing, iterator is exhausted :/
    print(i)

print(list((i for i in range(3))))  # this works, but why you used generator in first place then?


## exceptions:
try:
    1/0
except:  # bad practice, catches all, can hide errors
    print('Something is wrong')

try:
    1/0
except ZeroDivisionError:
    print('No zero division, please :(')

try:
    try:
        raise RuntimeError('Boom!')
    except RuntimeError:
        print('Something went wrong, just saying...')
        raise
except Exception as e:
    print('Something happened above, see:')
    print(e)
    print('Recovering...')

print('\nGood:\n')

try:
    pass
except:
    print('Not going here, because everything is fine.')
else:
    print('Nothing wrong happened!')
finally:
    print('This is always executed, no matter what.')

print('\nBad:\n')

try:
    assert 'War' is 'Peace'
except Exception as e:
    print(type(e), e.args, e)
else:
    print('Not going here, it is bad...')
finally:
    print('This is always executed, no matter what.')


print('Magic:', [item for item in dir() if item.startswith('__')])
