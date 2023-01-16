x = 'global'


def enc():
	x = 'enclosing'
	print(f'Enclosing x = {x} scope')

	def local():
		x = 'local'
		print(f'Local x = {x} scope')

	local()


enc()
print(f'Global x = {x} scope')
