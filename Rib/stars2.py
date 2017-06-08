# Assignment: Stars
# Write the following functions.
# Part I
# Create a function called draw_stars() that takes a list of numbers and prints out *.

# For example:

# x = [4, 6, 1, 3, 5, 7, 25]
# Copy
# draw_stars(x)should print the following in when invoked:

# ****
# ******
# *
# ***
# *****
# *******
# *************************
def draw_stars(list):
	for i in range(len(list)):
		print "* " * list[i]


def draw_stars2(list):
	for i in range(len(list)):
		if type(list[i]) == int:
			print "*" * list[i] 
		elif type(list[i]) == str:
			print list[i][0].lower() * len(list[i])

test_list = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars2(test_list)

