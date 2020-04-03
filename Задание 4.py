#Пользователь вводит целое положительное число.
#Найдите самую большую цифру в числе.
#Для решения используйте цикл while и арифметические операции.
chislo = (int(input('Введите целое число ')))
ostatok = 0
while ostatok > 1 :
	if ostatok == 0 :
		ostatok = chislo % 10
		maximum = ostatok
		chislo //= 10
	else :
		ostatok = chislo % 10
		if maximum < ostatok :
			maximum = ostatok
			chislo //= 10
		else :
			chislo //= 10
print(maximum)
