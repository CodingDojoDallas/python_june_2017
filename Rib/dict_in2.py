# Assignment: Dictionary in, tuples out
# Write a function that takes in a dictionary and returns a list of tuples where the first tuple item is the key
 # and the second is the value. Here's an example:

a_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}


def my_dict(a_dict):

	print "{}".format(dict.items(a_dict))

my_dict(a_dict)
		



