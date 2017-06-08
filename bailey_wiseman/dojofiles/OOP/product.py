class product(object):
	def __init__(self, price, item, weight, brand, cost, status='For Sale'):
		self.price = price
		self.item = item
		self.weight = weight
		self.brand = brand
		self.cost = cost
		self.status = status

	def display(self):
		print 'Price:...', self.price
		print 'Item:...', self.item
		print 'Weight:...', self.weight
		print 'Brand:...', self.brand
		print 'Cost:...', self.cost
		print 'Status:...', self.status
		print ''

		return self

	def sell(self):
		self.status = 'Sold'

		return self

	def tax(self):
		self.price = self.price * 1.08
		print 'Price after tax:...', self.price
		return self

	def itemreturn(self, refund):
		if refund == 'defective':
			self.status = 'defective'
			self.price = 0
		elif refund == 'like_new':
			self.status = 'For Sale'
		elif refund == 'used':
			self.status = 'used'
			self.price = self.price * 0.8

		return self

product1 = product(200, 'Kayak', '85lbs', 'Alqui', 200)
product2 = product(20, 'Teapot', '5lbs', 'Sern', 20)
product3 = product(2000, 'Office Chair', '15lbs', 'Office Mate', 2000)
product4 = product(60, 'SunRoof', '30lbs', 'Shade Masters', 60)
product5 = product(180, 'Monitor', '12lbs', 'Hoffs', 180)

product1.tax().sell().display()
product2.itemreturn('defective').display()
product3.tax().sell().display()
product4.itemreturn('like_new').display()
product5.itemreturn('used').display()
