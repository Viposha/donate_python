import math

radius = None
while not radius:
	try:
		radius = float(input('Enter radius'))
		if radius <= 0:
			print('Radius must be a positive number. And not zero')
			radius = None
	except ValueError:
		print('Enter only digits')

area = math.pi * radius ** 2
print(f'The area of circle is {round(area, 2)}')