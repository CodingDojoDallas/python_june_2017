class animal(object):
	def __init__(self, name, health):
		self.name = name
		self.health = health

	def display(self):
		print 'Hit Points...', self.health
		print ''
		return self

	def walk(self):
		print 'Walking...'
		self.health -= 1
		return self

	def run(self):
		print 'Running...'
		self.health -= 5
		return self

animal1 = animal('adsd', 100)
animal1.walk().walk().walk().run().run().display()

class dog(animal):
	def __init__(self, name, health):
		super(dog, self).__init__(name, health)
		self.name = name
		self.health = health

	def pet(self):
		print 'Petting...'
		self.health += 5
		return self

dog1 = dog('spot', 150)
dog1.walk().walk().pet().run().display()

class dragon(animal):
	def __init__(self, name, health):
		super(dragon, self).__init__(name, health)

	def fly(self):
		print 'Flying...'
		self.health -= 10
		return self

dragon1 = dragon('ajis', 170)
dragon1.fly().fly().fly().display()

class bear(animal):
	def __init__(self, name, health):
		super(bear, self).__init__(name, health)

	def climb(self):
		print 'Climbing...'
		self.health -= 15
		return self

bear1 = bear('misha', 800)
bear1.walk().walk().walk().climb().climb().climb().climb().display()