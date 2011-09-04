i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num

# Extra Credit
numbers = []
def print_append_loop(count, increment):
    i = 0
    while i < count:
        print "At the top i is %d" % i
        numbers.append(i)

        i += increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

print_append_loop(5, 2)

def print_append_loop_2(count, increment):
    numbers = []
    for i in range(0, count, increment):
        print "At the top i is %d" % i
        numbers.append(i)

        i += 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

print_append_loop_2(8, 3)
# You don't need to add the manual increment in the code
# And it produces the same list in numbers as it's running...
# Even though i through the loop is different
