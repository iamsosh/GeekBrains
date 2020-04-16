''' 3. Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.'''
with open('salaries.txt') as my_file :
	salaries = []
	lines = my_file.readlines()
	for i in lines :
		surname, salary = i.split(' ')
		salaries.append(int(salary))
		if int(salary) < 20000 :
			print(i, end = '')
	middle_salary = sum(salaries) / len(salaries)
	print('Средняя зарплата равна %d' % middle_salary)