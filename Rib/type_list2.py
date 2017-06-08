# Assignment: Type List
# Write a program that takes a list and prints a message
# for each element in the list, based on that element's 
# ta type.

# Your program input will always be a list. For each item in the list, test its data type. If the item is a string, 
# concatenate it onto a new string. If it is a number, add it to a running sum. At the end of your program print 
# the string, the number and an analysis of what the array contains. If it contains only one type, print that type, 
# otherwise, print 'mixed'.

# Here are a couple of test cases. Think of some of your own, too. What kind of unexpected input could you get?


def whatisit(list):
	string = ''
	sum = 0


	for item in list:
		if type(item) is int or type(item) is float:
			sum +=  item
		elif type(item) is str:
			string += ''+ item

	if len(string) > 0 and sum > 0:
		print 'The array you entered is of mixed type'
		print string
		print sum

	elif len(string) == 0 and sum > 0:
		print 'The array you entered is of integer type'
		print sum

	elif len(string) > 0 and sum == 0:
		print 'The array you entered is of string type'
		print string

whatisit(['magical unicorns',19,'hello',98.98,'world'])
whatisit ([2,3,1,7,4,12])
whatisit (['magical','unicorns'])


