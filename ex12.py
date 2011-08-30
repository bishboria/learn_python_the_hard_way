age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

# Extra Credit: both open & file are used in file I/O. open is the preferred
# way to do this though.

# Import and use os if you want to make your programs compatible with *nix and
# windows. But then you should limit yourself to only the functions available
# to all systems.

# sys gives you access to some of the functions available to the python
# interpreter, like argv, path, stdout, stdin, float_info, maxint, etc
