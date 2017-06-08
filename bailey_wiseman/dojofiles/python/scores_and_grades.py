# Assignment: Scores and Grades
# Write a function that generates ten scores between 60 and 100. 
# Each time a score is generated, your function should display what the grade is for a particular score. Here is the grade table:

# Score: 60 - 69; Grade - D Score: 70 - 79; Grade - C Score: 80 - 89; Grade - B Score: 90 - 100; Grade - A

import random
roll = random.randrange(60, 101)

def scores():
	if roll > 59 and roll < 70:
		print('Score:...', roll, 'Your Grade is D')
	elif roll > 69 and roll < 80:
		print('Score:...', roll, 'Your Grade is C')
	elif roll > 79 and roll < 90:
		print('Score:...', roll, 'Your Grade is B')
	elif roll > 89 and roll < 101:
		print('Score:...', roll, 'Your Grade is A')
scores()
