# Assignment: Find Characters
# Write a program that takes a list of strings and a string containing a single character, 
# and prints a new list 
# of all the strings containing that character.

def command_F(string_list,char_kb):
	new_list = []
	for i in string_list:
		if char_kb in i:
			new_list.append(i)
	print 'This is the new list: '
	print new_list

words = ['hello','world','my_name', 'is', 'Anna']
char = 'o'

command_F(words,char)

	