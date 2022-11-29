print('Вітаємо в найкращому уніаерситеті Києва')
name = input('Як тебе звати?')
education = input(f'{name}, яка в тебе освіта? Школа чи коледж?')
doc_name_school = ['Атестат', 'Додаток', ' Сертифікат ЗНО', 'ІНН', 'Паспорт', 'Прописка', 'Військовий квиток чи приписне']
doc_name_college = ['Диплом', 'Додаток', ' Сертифікат ЗНО', 'ІНН', 'Паспорт', 'Прописка', 'Військовий квиток чи приписне']
prupusne = None
mark = None
mark_zno = None
if education.lower() == 'школа':
	atestat = input('В тебе є атестат з собою? Відповідай так чи ні')
	dodatok = input('А додаток до нього?')
	if dodatok == 'так':
		mark = int(input(f'Так так. Подивимся. {name}, а який в тебе середній бал?'))
	zno = input('Сертифікат ЗНО?')
	if zno == 'так':
		mark_zno = int(input(f'{name}, а який в тебе бал з математики та фізики?'))
	inn = input('Індивідуальний податковий номер')
	passport = input('Паспорт?')
	propiska = input('Прописка')
	kvitok = input('Військовий квиток')
	if kvitok.lower() == 'ні':
		prupusne = input('А приписне?')
	docs = [atestat, dodatok, zno, inn, passport, propiska, kvitok]
	if prupusne == 'так':
		docs.pop()
	required_docs = []
	for i, doc in enumerate(docs):
		if doc == 'ні':
			required_docs.append(doc_name_school[i])
	if required_docs:
		print(f"Донеси будь ласка {', '.join(required_docs)}")
	else:
		if mark > 7 and mark_zno > 200:
			print(f'{name}, Ти проходиш до нашого університету поза конкурсом. Вітаю')
		elif mark < 7:
			print('Вашого середнього балу достатньо тільки для навчання на контракті')
		else:
			print('Ваші документи прийняті. Бажаємо успіху на іспиті')
else:
	diploma = input('В тебе диплом з собою?Відповідай так чи ні')
	dodatok = input('А додаток до нього?')
	mark = int(input(f'Так так. Подивимся. {name}, а який в тебе середній бал?'))
	zno = input('Сертифікат ЗНО?')
	inn = input('Індивідуальний податковий номер')
	passport = input('Паспорт?')
	propiska = input('Прописка')
	kvitok = input('Військовий квиток')
	if kvitok.lower() == 'ні':
		prupusne = input('А приписне?')
	docs = [diploma, dodatok, zno, inn, passport, propiska, kvitok]
	if prupusne == 'так':
		docs.pop()
	required_docs = []
	for i, doc in enumerate(docs):
		if doc == 'ні':
			required_docs.append(doc_name_college[i])
	if required_docs:
		print(f"Донеси будь ласка {', '.join(required_docs)}")
	else:
		if mark < 75:
			print('Вашого середнього балу достатньо тільки для навчання на контракті')
		else:
			print('Ваші документи прийняті. Бажаємо успіху на іспиті')

