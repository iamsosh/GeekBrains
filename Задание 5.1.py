''' 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.'''
my_list = ['hello,', 'world!', '', 'broccoli', 'is', 'healthy', 'food']
my_file = open('test.txt', 'w')
for i in my_list :
	if i != '':
		my_file.writelines(i + '\n')
	else :
		break
my_file.close()