'''3. Реализовать базовый класс Worker (работник),
в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).'''

class Worker:
	def __init__(self, name, surname, position, income):
		self._name = name
		self._surname = surname
		self._position = position
		self._income_wage = income['wage']
		self._income_bonus = income['bonus']
class Position(Worker):
	def get_full_name(self):
		print(self._name, self._surname, self._position)

	def get_total_income(self):
		print(self._income_wage + self._income_bonus)

worker = Position('Иван', 'Петров', 'Строитель', {'wage': 125000, 'bonus': 50000})
worker.get_full_name()
worker.get_total_income()