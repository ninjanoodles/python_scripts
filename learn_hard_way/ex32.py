the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'orange' , 'pears', 'apricots']
change = [1, 'pennies', 2 , 'dimes' , 3 , 'quarters']

# this first kind of for-loop goes the a list
for number in the_count:
    print "This is count %d" % number
    
# Same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit
    
# Also se wan through mixed list too
# Notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i
    
# we can also build list, first start with an empty one
elements = range (0, 11, 2)

# the use the range funftion to do 0 to 5 counts
#for i in range(0, 6, 2):
#    print "Adding %d to the list." % i
#    # append is a function that lists understand
#    elements.append(i)
    
# now we can can print them out too
for i in elements:
    print "Element was: % d" % i
      