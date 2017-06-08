class Call(object):
	def __init__(self, callid, name, phone, time, purpose):
		self.callid = callid
		self.name = name
		self.phone = phone
		self.time = time
		self.purpose = purpose

	def display(self):
		print 'Caller-ID :', self.callid
		print 'Name :', self.name
		print 'Phone# :', self.phone
		print 'Call-time :', self.timeCall
		print 'Purpose :', self.purpose
		print ''
		return self

	def __str__(self):
		return "Callid: {}, Name: {}, Phone: {}, Time: {}, Purpose: {}".format(
			self.callid,
			self.name,
			self.phone,
			self.time,
			self.purpose
		)

class Center(object):
	def __init__(self):
		self.data = []
		self.queue = 0

	def add_call(self, callid, name, phone, time, purpose):
		print 'added call...'
		call = Call(callid, name, phone, time, purpose)
		self.data.append(call)
		return self

	def remove_call(self):
		self.data.pop(0)
		print 'removed call...'
		return self

	def info(self):
		for call in center.data:
			self.queue += 1
			print 'queue:', self.queue
		return self

center = Center()
center.add_call(1, 'joe', '214-667-4567', 1330, 'finance')
center.add_call(2, 'mary-ann', '214-869-1300', 1332, 'tech support')
center.add_call(3, 'alex', '543-443-7492', 1332, 'finance')
center.add_call(4, 'sin', '324-437-4531', 1335, 'n/a')
center.add_call(5, 'chris', '622-096-2544', 1336, 'tech support')

center.info().remove_call().info()
for call in center.data:
	print call

