products = {}
answ = 'yes'
print('Add first product')

while answ == 'yes':
	item = input('Enter product:')
	price = int(input('Enter price:'))
	products[f'{item}'] = price
	answ = input('Do you want add another product?').lower()
print(products)