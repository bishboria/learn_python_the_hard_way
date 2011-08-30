from sys import argv

script, filename = argv

txt = open(filename)

bytes_to_read = 15
print "Here's the first %d characters of the file %r:" % (bytes_to_read, filename)
print txt.read(15)

txt_again = open(filename)

print "Here's the first line of the file %r:" % filename
print txt_again.readline()
