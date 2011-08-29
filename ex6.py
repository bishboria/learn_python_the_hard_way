x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) # 2 Strings in a string

print x
print y

print "I said: %r." % x # String in a string
print "I also said: '%s'." % y # String in a string

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e # + concatenates strings

# There are only 4 strings in strings as x takes an integer
# and "hilarious" is a boolean
