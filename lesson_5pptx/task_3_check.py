x = int(input('Enter a number:'))


def sign_number():
	global x

	def neg_number():
		print('Number is negative')
	if x > 0:
		print(f'Number is positive')
	elif x == 0:
		print(f'Number is 0')
	else:
		neg_number()

sign_number()