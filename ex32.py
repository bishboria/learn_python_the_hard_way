the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also notice we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d do the list." % i
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print "Element was: %d" % i

# Extra Credit: alternative to block at line 22
new_elements = range(0, 6)
print new_elements

# other methods available to lists
els = range(0, 1000)
print 5 in els # check for inclusion
print range(0, 1000) == els # equality
print range(-5, 1001) >= els # compares each element lexicograpically
print els[14:17] # slices the list
print els[0:2]
print els[0] # accessing elements directly
print els[1]
print range(0, 5) * 2 # appends original list x-1 times onto itself
print range(0, 5).pop()
xs = range(0, 5)
xs.reverse()
print xs
xs = [6, 2, 3, 5, 1]
xs.sort()
print xs
xs = [1, 2, 3, 4, 5]
xs.remove(3)
print xs # value 3 is missing now
xs = [1, 2, 3]
xs.insert(1, 3)
print xs # value 3 is now where value 2 was
print xs.count(3) # how many 3's are in the list
print xs.index(3) # index of first occurence of 3
