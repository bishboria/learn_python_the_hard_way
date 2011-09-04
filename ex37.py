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
