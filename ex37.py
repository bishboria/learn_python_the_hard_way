# KEYWORDS

# and
print 1 == 1 and 2 == 2

# del
a = [1, 2, 3]
del a
# referencing a now causes a NameError. a now deleted.

# from & import
from sys import exit

# not
print not False

# while
i = 0
while i < 2:
    print i
    i += 1

# with & as
with open("ex37.py") as f:
    print f.read()

# if, elif, else
if False:
    print "won't get here"
elif True:
    print "in the elif"
else:
    print "not possible either"

# global & def
def test():
    global some_value
    some_value = "Not in the original scope"
test()
print some_value
del some_value

# or
print False or True

# assert
def test(arg):
    # assert arg == "a value" # Will stop the code from running
    print arg
test("a value")
test("b value")

# pass
if 1 == 1:
    print "do something"
else:
    pass # don't need to do anything

# yield & for
def enum(seq):
    n = 0
    for i in seq:
        yield n, i
        n += 1
print list(enum(['a', 'b', 'c', 'd', 'e']))

# break
for i in range(0, 5):
    if i == 3:
        break
    else:
        print i

# try & except
try:
    a = [1, 2, 3]
    del a
    a
except:
    print "oops, that didn't work"

# class & return
class Thing:
    def __init__(self, a, b):
        self.y = a
        self.z = b
    def meth_1(self):
        return "method_1 %d" % self.y
    def meth_2(self):
        return "method_2 %d" % self.z
a = Thing(1, 2)
print a.meth_1()
print a.meth_2()

# exec
exec 'print "Hello world!"'

# in
for i in [3, 8, 3, 2, 4]:
    print i

# raise & finally
try:
    raise NameError
except:
    print "raised a NameError deliberately"
finally:
    print "Here's a finally block"

# continue
for i in [1, 2, 3, 4, 5]:
    if i == 2:
        print "got a 2 continue"
        continue
    else:
        print i

# is checks identity
a = "thing"
b = "thing"
if a is b:
    print "they are equal"

# lambda
def add(n):
    return lambda m: m + n
add_to_10 = add(10)
print add_to_10(0)
print add_to_10(10)
print add_to_10(1)


# DATATYPES

print True

print False

if None:
    print "None is true..."
else:
    print "None is false"

if [] is None:
    print "empty list is None."
elif [] is not None:
    print "empty list is not None."

print "This is a string"
print 'And so is this'

print 5

print 4.2

print [1, 2, 4]


# String Escape Sequences

print "\\"
print "\'"
print "\""
print "\\a before\aafter"
print "\\b before\bafter"
print "\\f before\fafter"
print "\\n before\nafter"
print "\\r before\rafter"
print "\\t before\tafter"
print "\\v before\vafter"


# String Formats

print "%d" % 2
print "%i" % 1.1
print "%o" % 9 # octal
print "%u" % 12345678
print "%x" % 10
print "%X" % 10
print "%e" % 100
print "%E" % 100
print "%f" % 100
print "%F" % 100
print "%g" % 123
print "%G" % 123
print "%c" % 'b'
print "%r" % "a"
print "%s" % "a"


# Operators

print 1 + 1
print 2 - 1
print 2 * 3
print 2 ** 3
print 2.0 / 3.0
print 2 // 3
print 2 % 3
print 1 < 2
print 2 > 1
print 2 <= 2
print 2 >= 2
print 2.0 == 2.0
print 1.1 != 1.0
print 1.1 <> 1.0
print (1, 2, 3) # tuples
print 1, 2, 3
print [1, 2, 3] # list
print {"one":1, "two":2} # dictionaries
print dict(one=1, two=2)
print dict(zip(("one", "two"), (1, 2)))

# @ is used in decorators
# but decorators in python are more like macros
# they allow you to modify functions
def security_log_in_out(trans):
    def inner(*args, **kwargs):
        print "log in"
        trans(*args, **kwargs)
        print "log out"
    return inner

@security_log_in_out
def deposit(money):
    print "adding %r to account" % money

deposit(100)


print [1, 2, 3] # , usage
print (1, 2, 3)
print 1, 2, 3

print [1, 2, 3][0:1] # : usage
print {"key":"value"}

a = [1, 2] # . usage
a.append(3)
print a

print "hello"; print "there" # ; usage
if 1 < 2: print "1"; print "is less than"; print "2"

i = 0
i += 1
print i

i = 0
i -= 1
print i

i = 1
i *= 3
print i

i = 7.0
i /= 3.0
print i

i = 7.0
i //= 3.0
print i

i = 7
i %= 3
print i

i = 2
i **= 3
print i
