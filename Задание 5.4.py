'''. Создать (не программно) текстовый файл со следующим содержимым:

One — 1

Two — 2

Three — 3

Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл. '''
with open('numbers.txt') as my_file :
	numbers = my_file.readlines()
with open('new_numbers.txt', 'w') as my_file:
	for row in numbers:
		if '1' in row:
			row = row.replace('one','один')
		elif '2' in row:
			row = row.replace('two', 'два')
		elif '3' in row:
			row = row.replace('three', 'три')
		elif '4' in row:
			row = row.replace('four', 'четыре')
		my_file.write(row)