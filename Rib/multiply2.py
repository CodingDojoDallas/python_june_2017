# Multiply:
# Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) 
# and returns a list where each value has been multiplied by 5. The function should multiply each value in the 
# list by the second argument. For example, let's say:

# a = [2,4,10,16]

# Then:

# b = multiply(a, 5)
# print b

# Should print [10, 20, 50, 80 ].

def multiply(list):
	new_list = []
	for i in list:
		new_list += [i*5]
		if  i >= len(list):
			print new_list

multiply([1,2,3,4])