# First and Last
# Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"]. 
# Now create a new list containing only the first and last values in the original list. Your code should work for any list.

x = ["hello",2,54,-2,7,12,98,"world"]
i=0
print x[0]

print 'The first value for the array is : ', x[0]
print 'The last value for the array is : ', x[len(x)-1]

#Creating a new list containing only the first and last values in the original list. Your code should work for any list.
print 'New List is: ', [x[0], x[-1]]



