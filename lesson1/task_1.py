while True:
	try:
		answ = int(input('Input a number:'))
		if answ > 0:
			print(f'Your\'s number is {answ}. And it\'s positiv')
			break
		elif answ < 0:
			print(f'Your\'s number is {answ}. And it\'s negativ')
			break
		else:
			print(f'Your\'s number is {answ}. And it\'s zero')
			break
	except ValueError as error:
		print("It's not a number. Try one more time")