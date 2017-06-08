# Create a function called odd_even that counts from 1 to 2000. 
# As your loop executes have your program print the number of that 
# iteration and specify whether it's an odd or even number.

def odd_even(size):
	for x in range(1, size):
		if x %2 != 0:
			print "The number is {}.  This is an odd number.".format(x)
		else:
			print "The number is {}.  This is an even number.".format(x)
odd_even(2000)