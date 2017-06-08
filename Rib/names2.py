# Assignment: Names
# Write the following function.

# students =	[{'first_name':  'Michael', 'last_name' : 'Jordan'},
# 			{'first_name' : 'John', 'last_name' : 'Rosales'},
# 			{'first_name' : 'Mark', 'last_name' : 'Guillen'},
# 			{'first_name' : 'KB', 'last_name' : 'Tonel'}]

users = {
 'Students':	[
 				 	{'first_name':  'Michael', 'last_name' : 'Jordan'},
 				 	{'first_name' : 'John', 'last_name' : 'Rosales'},
 				 	{'first_name' : 'Mark', 'last_name' : 'Guillen'},
 				 	{'first_name' : 'KB', 'last_name' : 'Tonel'}
 				],

 'Instructors':	[
	 				{'first_name' : 'Michael', 'last_name' : 'Choi'},	
	 				{'first_name' : 'Martin', 'last_name' : 'Puryear'}
	 			]
 }

students = users['Students']
# print students
# print green['first_name'], green['last_name']

for student in students:
	print student['first_name'], student['last_name']

instructors = users['Instructors']

for instructor in instructors:
	print instructor['first_name'], instructor['last_name']

# 






# green = students[0]

# # print "green: " ,green['first_name']
# # print "green: " ,green['last_name']

# green2 = students[1]
# # print "green2: " ,green2
# # print "green2: " ,green2['first_name']
# # print "green2: " ,green2['last_name']

# green3 = students[2]
# # print "green3: " ,green3
# # print "green3: " ,green3['first_name']
# # print "green3: " ,green3['last_name']

# green4 = students[3]
# # print "green4: " ,green4
# # print "green4: " ,green4['first_name']
# # print "green4: " ,green4['last_name']

# for green in students:
# 	print "first_name: ",green['first_name'], "last_name: ", green['last_name']
# # ['first_name'],['last_name']



































# def output(students):

# 	for x in students:
# 		print x['first_name'], x['last_name']

# def all(users):
# 	for role in users:
# 		count = 0
# 		print role
# 		for people in users[role]:
# 			count += 1
# 			length = len(people['first_name']) + len(people['last_name'])
# 			print "{} - {}  {} - {}".format(count, people['first_name'], people['last_name'], length)

# output(students)
# all(users)










