# Assignment: Filter by Type
# Write a program that, given some value, tests that value for its type. Here's what you should do for each type:

# Integer
# If the integer is greater than or equal to 100, print "That's a big number!" If the integer is less than 100, 
# print "That's a small number"


# question = 'Please enter an integer from 1 to 100 '
# print ('Please an integer from 1 to 100,')


# a = int(raw_input(question))

# if a <= 100=True

# if True :
#     print 'Thats a small number!'
# elif:	
# 	print 'Thats a big number!'
# else:
# 	print ("That wasnt a number between 1 and 100.  Please try again."

def whatisit(test):
    if type(test) is int:
        if (test) <= 100:
            print "Small Number"
        else:
            print "Big Number!"
    elif type(test) is str:
        if len(test) <= 100:
            print "Short Sentence"
        else:
            print "Long Sentence"
    elif type(test) is list:
        if len(test) <=10:
            print "Short List"
        else:
            print "Big List!"
        
whatisit([1,2,43,556,4,5,6,3,2,3,67,8,"sdflk"])