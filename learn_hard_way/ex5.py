name = 'Zed A. Shaw'
age = 35 # not a lie
height_inch = 74 # inches
weight_lbs = 180 #lbs
height_cm = height_inch * 2.5 
weight_kg = weight_lbs / 2.2
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %f inches tall." % height_inch
print "He's %f pounds heavy." % weight_lbs
print "He's %f centimeters tall." % height_cm
print "He's %f kilograms heavy." % weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# This line is tricky, Try to get it exactly right

print "If I add %d, %d, and %d I get %d." % (age, height_inch, weight_lbs, age + height_inch + weight_lbs)
