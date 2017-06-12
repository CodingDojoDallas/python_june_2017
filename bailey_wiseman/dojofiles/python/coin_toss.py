import random

def start(myrange):
	tails = 0
	heads = 0
	total = heads + tails
	for i in myrange:
		flip = random.randrange(1, 3)
		if flip == 1:
			tails += 1
			total = heads + tails
			print('Attempt #', total, 'out of', len(myrange), 'Throwing coin... It is Tails!...', 'Got', heads, 'Head(s) so far and', tails, 'Tail(s) so far!')
		elif flip == 2:
			heads += 1
			total = heads + tails
			print('Attempt #', total, 'out of', len(myrange), 'Throwing coin... It is Heads!...', 'Got', heads, 'Head(s) so far and', tails, 'Tail(s) so far!')
start(range(0, 5000))