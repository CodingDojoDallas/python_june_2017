def table():
	count = 0
	x = 1
	while count < 13:
		if count < 2:
			x = 1
			count += 1
			print (x * 1, x * 2, x * 3, x * 4, x * 5, x * 6, x * 7, x * 8, x * 9, x * 10, x * 11, x * 12)
		elif count > 1:
			x += 1
			count += 1
			print (x * 1, x * 2, x * 3, x * 4, x * 5, x * 6, x * 7, x * 8, x * 9, x * 10, x * 11, x * 12)

table()