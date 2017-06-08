class mathdojo(object):
	def __init__(self, mysum=0):
		self.mysum = mysum


	def add(self, *args):
		for i in args:
			if type(i) == int:
				self.mysum += i
		return self

	def subtract(self, *args):
		for i in args:
			if type(i) == int:
				self.mysum -= i
		return self
	def result(self):
		print 'SUM...', self.mysum
		return self

md = mathdojo()
md.add(2).add(2, 5).subtract(3, 2).result()