# Write a program that compares two lists and prints a message depending on if the inputs are identical or not.

# Your program should be able to accept and compare two lists: list_one and list_two. If both lists are identical 
# print "The lists are the same". If they are not identical print "The lists are not the same." Try the following test 
# cases for lists one and two:



def compare(list1,list2):
	if len(list1) != len(list2):
		print 'The lists are not the same.'
		return False
	for i in range(len(list1)):
		if list1[i] != list2[i]:
			print 'The lists are not the same'
			return False
	print 'The lists are the same'

list1 = [1,4,6,7,5,34]
list2 = [2,4,5,7,7,75]
compare(list1,list2)