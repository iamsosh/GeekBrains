'''1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод init()), который должен принимать данные (список списков) для формирования матрицы.

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.'''

class Matrix:
	def __init__(self, matrix):
		self.matrix = matrix

	def __str__(self):
		return '\n'.join([' '.join(str(el) for el in row) for row in self.matrix])

	def __add__(self, other):
		result = '' # пустой str, чтобы матрица несъезжала
		if len(self.matrix) == len(other.matrix):
			for row_1, row_2 in zip(self.matrix, other.matrix):
				if len(row_1) != len(row_2):
					return 'incorrect shape'
				else:
					sum_of_row = [a + b for a, b in zip(row_1, row_2)]
					result += ' '.join([str(i) for i in sum_of_row]) + '\n'
		else :
			return 'incorrect shape'
		return result

my_matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
my_matrix2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print(my_matrix1 + my_matrix2)