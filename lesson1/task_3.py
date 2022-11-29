def is_valid_sides():
	while True:
		try:
			a = int(input('Input side a:'))
			b = int(input('Input side b:'))
			c = int(input('Input side c:'))
			if a > 0 and b > 0 and c > 0:
				break
			else:
				print('Sides can not be less then 0')
		except ValueError as error:
			print("It's not a number. Try one more time")

	return [a, b, c]


def is_valid_triangle():
	triangle = sorted(is_valid_sides())
	if triangle[2] < triangle[0] + triangle[1]:
		print(f'Triangle with sides {triangle[0]}, {triangle[1]}, {triangle[2]} is real')
	else:
		print('This is fake triangle')


if __name__ == '__main__':
	is_valid_triangle()
