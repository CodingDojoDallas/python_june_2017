# Assignment: Compare Arrays
# Write a program that compares two lists and prints a message depending on if the inputs are identical or not.

# Your program should be able to accept and compare two lists: list_one and list_two. If both lists are identical print "The lists are the same". If they are not identical print "The lists are not the same." Try the following test cases for lists one and two:

# list_one = [1,2,5,6,2]
# list_two = [1,2,5,6,2]
# Copy
# list_one = [1,2,5,6,5]
# list_two = [1,2,5,6,5,3]
# Copy
# list_one = [1,2,5,6,5,16]
# list_two = [1,2,5,6,5]
# Copy
# list_one = ['celery','carrots','bread','milk']
# list_two = ['celery','carrots','bread','cream']

def clone(mylist_1, mylist_2):
	if (type(mylist_1) == list and type(mylist_2) == list):
		print ('Both Are List!...')
		print(mylist_1)
		print(mylist_2)
		if (len(mylist_1) == len(mylist_2)):
			print ('Length is Same!...')
			print(mylist_1)
			print(mylist_2)
			for x,y in zip(mylist_1, mylist_2):
				if x != y:
					print ('ERROR: List values differ!...')
					print(mylist_1)
					print(mylist_2)
					return False
			print ('List are identical!...')
			print(mylist_1)
			print(mylist_2)
		else:
			print ('ERROR: Lengths differ!...')
			print(mylist_1)
			print(mylist_2)
			return False
	else:
		print ('ERROR: One or Both are not list!...')
		print(mylist_1)
		print(mylist_2)
		return False
clone()