# Assignment: Making Dictionaries
# Create a function that takes in two lists and creates a single dictionary where the first list contains keys and the second values. Assume the lists will be of equal length.

# Your first function will take in two lists containing some strings. Here are two example lists:

# name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
# favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
# Copy
# Here's some help starting your function.

# def make_dict(arr1, arr2):
#   new_dict = {}
#   # your code here
#   return new_dict

def mydict(list1, list2):
	new_dict = zip(list1, list2)
	print dict(new_dict)
mydict(["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"], ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"])