'''2. Создать текстовый файл (не программно), сохранить в нем несколько строк, 
выполнить подсчет количества строк, количества слов в каждой строке.'''
with open('test.txt') as my_file:
	count_lines = my_file.readlines()
	print('Количество строк равно %d' % len(count_lines))
	for ordinal_number, count_words in enumerate(count_lines, start = 1):
		print('В строке {} находится {} слов'.format(ordinal_number, len(count_words.split(' '))))