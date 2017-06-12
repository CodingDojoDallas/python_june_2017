class car(object):
	def __init__(self, price, speed, fuel, mileage, tax=1.12):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		self.tax = tax
		if self.price > 10000:
			self.tax = (1.15)

	def display(self):
		print 'Price:...', self.price
		print 'Speed:...', self.speed, 'MPH' 
		print 'Fuel:...', self.fuel
		print 'Mileage:...', self.mileage, 'MPG'
		print 'Tax:...', self.tax
		print ''
		return self

car1 = car(8000, 40, 'empty', 25)
car2 = car(18000, 80, 'low', 17)
car3 = car(3000, 20, 'empty', 13)
car4 = car(28000, 120, 'full', 20)
car5 = car(9900, 50, 'low', 22)
car6 = car(14200, 55, 'empty', 15)

car1.display()
car2.display()
car3.display()
car4.display()
car5.display()
car6.display()