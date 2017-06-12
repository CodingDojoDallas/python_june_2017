# Assignment: Making and Reading from Dictionaries
# Create a dictionary containing some information about yourself. The keys should include name, age, country of birth, favorite language.

# Write a function that will print something like the following as it executes:

# My name is Anna
# My age is 101
# My country of birth is The United States
# My favorite language is Python



def basics():

	thisdict = {
	'name': 'bailey',
	'age': '21',
	'COB': 'U.S.A',
	'language': 'python'
	}
	for key,data in thisdict.items():
		print (key, data)
basics()