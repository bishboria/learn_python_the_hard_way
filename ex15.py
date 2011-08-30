from sys import argv

script = argv

filename = raw_input("type in the name of your file: ")
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

file_again = raw_input("Type in the name of your file AGAIN: ")
txt_again = open(file_again)

print txt_again.read()
