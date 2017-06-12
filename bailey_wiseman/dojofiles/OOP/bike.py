class bike(object):
	def __init__(self, price, max_speed, miles=0):
		self.price = price
		self.max_speed = max_speed
		self.miles = miles

	def display(self):
		print 'Price:...', self.price, 'Max_Speed:...', self.max_speed, 'Miles:...', self.miles
		return self

	def ride(self):
		print 'Riding...'
		self.miles += 10
		return self

	def reverse(self):
		if self.miles == 0:
			print 'Already at zero! Cannot reverse any further!...'
		else:
			print 'Reversing...'
			self.miles -= 5
		return self

instance1 = bike('200$', '30mph')
instance2 = bike('400$', '42mph')
instance3 = bike('900$', '51mph')
instance1.ride().ride().ride().reverse().display()
instance2.ride().ride().reverse().reverse().display()
instance3.reverse().reverse().reverse().display()