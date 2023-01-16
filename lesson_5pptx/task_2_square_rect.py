def rect_square(a:int, b:int) -> int:
	if a <= 0 or b <= 0:
		print('This is invalid data')
	else:
		print(f'Square of rectangle is {a * b}')


rect_square(5, 7)