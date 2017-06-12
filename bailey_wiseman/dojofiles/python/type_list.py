# Assignment: Type List
# Write a program that takes a list and prints a message for each element in the list, 
# based on that element's data type.

# Your program input will always be a list. For each item in the list, test its data type. If the item is a string, 
# concatenate it onto a new string. If it is a number, add it to a running sum. At the end of your program print the string, the number and an analysis of what the array contains. If it contains only one type, print that type, otherwise, print 'mixed'.

# Here are a couple of test cases. Think of some of your own, too. What kind of unexpected input could you get?

# #input
# l = ['magical unicorns',19,'hello',98.98,'world']
# #output
# "The array you entered is of mixed type"
# "String: magical unicorns hello world"
# "Sum: 117.98"
# Copy
# # input
# l = [2,3,1,7,4,12]
# #output
# "The array you entered is of integer type"
# "Sum: 29"
# Copy
# # input
# l = ['magical','unicorns']
# #output
# "The array you entered is of string type"
# "String: magical unicorns"


def typelist(mylist):
	stronly = True
	intonly = True
	Mixed = False
	mysum = 0
	mystr = ''
	for i in mylist:
		if type(i) == int:
			mysum += i
			print ('integer:..', i)
			stronly = False
		elif type(i) == str:
			mystr += i
			print ('string:..', i)
			intonly = False
	if stronly == True:
		print ('This is a string list!...')
		print ('mystr:..', mystr)
		print (mylist)
	elif intonly == True:
		print ('this is an integer list!...')
		print ('mysum:..', mysum)
		print (mylist)
	else:
		print ('Its a mixed list!...')
		print ('mysum:..', mysum, 'mystr:..', mystr)
		print (mylist)
typelist(['magical unicorns',19,'hello',98.98,'world'])