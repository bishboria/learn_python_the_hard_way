from sys import argv

open(argv[2], 'w').write( open(argv[1]).read() )

# if you just use import ex17mod then you call like this: ex17mod.testmod()
from ex17mod import testmod
print "About to run a test module function"
testmod()
