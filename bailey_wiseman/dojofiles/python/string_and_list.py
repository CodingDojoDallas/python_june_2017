# Use only the built-in methods and functions from the previous tabs to do the following exercises. You will find the following methods and functions useful:

# • .find()

# • .replace()

# • min()

# • max()

# • .sort()

# • len()



# Find and Replace
# In this string: words = "It's thanksgiving day. It's my birthday,too!"
 # print the position of the first instance of the word "day". Then create a new string where the word "day" is replaced with the word "month".

def findnreplace(mystr):
	day = 'day'
	month = 'month'
	findit = mystr.find(day)
	replc = mystr.replace(day, month)
	print(mystr, findit, replc)
findnreplace("It's thanksgiving day. It's my birthday,too!")


# Min and Max
# Print the min and max values in a list like this one: x = [2,54,-2,7,12,98]. Your code should work for any list.

def mymax(mylist):
	compare = mylist[0]
	for i in mylist:
		if compare < i:
			compare = i
	print (compare, "max", mylist)
mymax([2,54,-2,7,12,98])

def mymin(mylist):
	compare = mylist[0]
	for i in mylist:
		if compare > i:
			compare = i
	print (compare, "min", mylist)
mymin([2,54,-2,7,12,98])

# First and Last
# Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"].
 # Now create a new list containing only the first and last values in the original list. Your code should work for any list.

def fandl(mylist):
	first = mylist[0]
	last = mylist[-1]
	print ('first-value:', first, 'last-value:', last)
	print (mylist)
fandl(["hello",2,54,-2,7,12,98,"world"])

# New List
# Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. Sort your list first. Then, split your list in half.
 # Push the list created from the first half to position 0 of the list created from the second half.
 #  The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. Stick with it, this one is tough!

def newlist(mylist):
	mylist.sort()
	print (mylist)
	middle = len(mylist)/2
	print (middle)
	middle = int(middle)
	print (middle)
	left = mylist[0:5]
	print (left)
	right = mylist[5:]
	print (right)
	stitch = left + right
	print (stitch)
newlist([19,2,54,-2,7,12,98,32,10,-3,6])