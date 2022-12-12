import sqlite3

db = "Donate_box.db"


def db_create(db):

	""" Create table in Databese"""

	with sqlite3.connect(db) as conn:
		sql_create_table = """ 
							CREATE TABLE IF NOT EXISTS Donate(
							day integer PRIMARY KEY,
							money integer
							); """
		c = conn.cursor()
		c.execute(sql_create_table)


while input("Україна сьогодні перемогла?").lower() != 'так':
	db_create(db)
	with sqlite3.connect(db) as conn:
		money = [int(input('Скільки гривень сьогодні задонатиш?'))]
		sql = """ 
				INSERT INTO Donate(money)
				VALUES(?) """
		cur = conn.cursor()
		cur.execute(sql, money)
		conn.commit()

with sqlite3.connect(db) as conn:
	all_donates = 0
	sql = """SELECT money FROM Donate"""
	data = conn.execute(sql)
	for money in data:
		all_donates += money[0]
	print(f'За час війни ди зібрав {all_donates} гривень')
	sql_2 = """ DROP TABLE Donate"""
	conn.execute(sql_2)