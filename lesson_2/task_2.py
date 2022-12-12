def facto(n):
	answ = 1
	for num in range(1, n+1):
		answ *=num
	print(answ)


facto(int(input('Input integer positive number:')))
