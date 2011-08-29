name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

# Extra Credit
print "This uses %%r: %r." % (age * height * weight)
# %r formats using repr() which returns a string that contains the printable
# version of an object. Handy for classes later

inches_centimetres_ratio = 2.54
pounds_kilos_ratio = 2.2
print "%s's height in centimetres is %.2f" % (name, height * inches_centimetres_ratio)
print "%s's weight in kilos is %.2f" % (name, weight / pounds_kilos_ratio)
