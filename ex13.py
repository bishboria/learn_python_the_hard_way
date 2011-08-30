from sys import argv

print argv
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is", second
print "Your third variable is", third

# Extra Credit: passing the scrip less parameters gives a ValueError.
# the LHS on line 3 is expecting 4 things, but argv doesn't have 4.

# Giving more arguments also gives a ValueError. That's just daft...

fourth_input = raw_input("Tell me something else: ")
print argv + [fourth_input]
