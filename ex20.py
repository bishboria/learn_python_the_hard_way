from sys import argv

script, input_file = argv

def print_all(f):
  print f.read()

# seek moves to a new file position and takes 1 or 2 parameters
# first param is the offset by which you want to move.
# The second (optional) parameter can have 1 of 3 different values:
#   0 (default): start from beginning of file. offset should be +ve
#   1: move from current position in file. offset can be +/-ve
#   2: move from end of file. offset -ve. some platforms allow +ve...
def rewind(f):
  f.seek(0)

def print_a_line(line_count, f):
  print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
