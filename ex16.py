from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

new_line = "\n"
output = "%s%s%s%s%s%s" % (
    line1,
    new_line,
    line2,
    new_line,
    line3,
    new_line
)
target.write(output)

print "And finally, we close it."
target.close()

print "Oh, open the file back up! Let's see what you wrote:"
target = open(filename)
print target.read()
target.close()

# Extra Credit 4: 'w' was passed as an extra parameter as this signifies
# that you want to file to be written to.
