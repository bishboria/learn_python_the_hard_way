print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

# Extra Credit: 6'2" has escapes around the quotes as %r prints these
# characters out. %s doesn't, but then the user may not pass you what
# you expect.

print "What is your postcode?",
postcode = raw_input()
print "What is your 16 digit credit card number?",
credit_card_number = raw_input()

message_to_user = "So, your postcode is %r and your credit card number is %r" % (postcode, credit_card_number)
print message_to_user + ", thank you kindly!"

name = raw_input("What is your name? ")
dob = raw_input("When were you born %s? " % name)
