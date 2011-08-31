from sys import argv
from os.path import exists

script, from_file, to_file = argv

# we could do these two on one line too, how?
input = open(from_file)
indata = input.read()
output = open(to_file, 'w')
output.write(indata)
output.close()
input.close()

# if you just use import ex17mod then you call like this: ex17mod.testmod()
from ex17mod import testmod
print "About to run a test module function"
testmod()
