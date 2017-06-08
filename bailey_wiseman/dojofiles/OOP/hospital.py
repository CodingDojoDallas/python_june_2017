class Patient(object):
	def __init__(self, p_id, name, allergies, bed=[]):
		self.p_id = p_id
		self.name = name
		self.allergies = allergies
		self.bed = bed
		self.patient_info = {'p_id': self.p_id, 'name': self.name, 'allergies': self.allergies, 'bed': self.bed,}

	def __str__(self):
		return "p_id: {}, Name: {}, allergies: {}, bed: {}".format(
			self.p_id,
			self.name,
			self.allergies,
			self.bed,
		)

class Hospital(object):
	def __init__(self, building, capacity):
		self.info = []
		self.building = building
		self.capacity = capacity
		self.myid = []

	def admit(self, p_id, name, allergies, bed):
		patient = Patient(p_id, name, allergies, bed)
		print 'admited patient {}, {}'.format(name, p_id)
		print ''
		self.info.append(patient)
		self.myid.append(p_id)
		return self

	def discharge(self, p_id):
		print self.myid
		if p_id == self.myid:
				self.info.pop(patient)
				self.myid.pop(p_id)
				print self.myid
				print ''
				print 'removed patient', self.info
				print ''
				self.capacity += 1
				return self

	def display(self):
		print 'Building: {}, Max Capacity: {}'.format(self.building, self.capacity)
		print ''
		for i in self.info:
			print 'patient info:', i
		return self

hospital = Hospital('st.johns', 5)

hospital.admit(2, 'jack', 'penicillin', [1])
hospital.admit(3, 'mike', 'asprin', [2])
hospital.admit(4, 'doug', 'penicillin', [3])
hospital.admit(5, 'louise', 'latex', [4])
hospital.admit(6, 'malley', 'penicillin, latex, oxiodants', [5])

hospital.display()

hospital.discharge(1)

hospital.display()