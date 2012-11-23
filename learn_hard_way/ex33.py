def loop_test (num,inc):
    """ this function is a test of while loop""" 
    i = 0
    numbers = []

#    while i < num:
    for i in range (0,num,inc):
        print "At the top i is %d" % i 
        numbers.append(i)
    
        i = i + inc
        print "Number now: ", numbers
        print "At the bottom i is %d" % i
    
    print "The numbers: "

    for num in numbers:
        print num
        
loop_test (20,5)