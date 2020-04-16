''' 5. Создать (программно) текстовый файл,
записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.'''
with open('numbers_sum.txt', 'w') as my_file:
    numbers = input('Введите числа через пробел: ')
    my_file.write('Введены числа ' + numbers + '\n')
	numbers = map(int, numbers.split())
	numbers_sum = sum(numbers)
	my_file.write('Сумма чисел равна ' + str(numbers_sum))
	print('Сумма введенных чисел ', numbers_sum)
# Задание сделал, вроде как и в разборе задач.
# Но выдает ошибку 
# TabError: inconsistent use of tabs and spaces in indentation (line 4)
# долго крутил, но всеравно не получилось избавиться от проблемы