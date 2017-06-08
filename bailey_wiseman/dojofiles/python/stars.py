# Assignment: Stars
# Write the following functions.

# Part I
# Create a function called draw_stars() that takes a list of numbers and prints out *.

def stars(mylist):
	for i in mylist:
		chain = ''
		for x in range(0, i):
			chain += '*'
		print (chain)
stars([4, 6, 1, 3, 5, 7, 25])


# Part II
# Modify the function above. Allow a list containing integers and strings to be passed to the draw_stars() function. 
# When a string is passed, instead of displaying *, display the first letter of the string according to the example below. 
# You may use the .lower() string method for this part.

def first(mylist):
	for i in mylist:
		if type(i) == int:
			chain = ''
			for x in range(0, i):
				chain += '*'
			print (chain)
		elif type(i) == str:
			mystr = ''
			for z in i:
				mystr += i[0]
			print (mystr)
first([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])
