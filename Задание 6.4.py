'''4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать
текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.'''

class Car:
	def __init__(self, speed, color, name, is_police):
		self.speed = speed
		self.color = color
		self.name = name
		self.is_police = is_police

	def go(self):
		print('Машина {} поехала'.format(self.name))

	def stop(self):
		print('Машина {} остановилась'.format(self.name))

	def turn(self, direction):
		self.direction = direction
		print('Машина повернула ', self.direction)

	def show_speed(self):
		print('Текущая скорость ', self.speed)

class TownCar(Car):
	def show_speed(self):
		if self.speed > 60 :
			print('Превышение скорости!')
		else :
			print('Текущая скорость ', self.speed)

class WorkCar(Car):
	def show_speed(self):
		if self.speed > 40 :
			print('Превышение скорости!')
		else :
			print('Текущая скорость ', self.speed)

class SportCar(Car):
	pass
	
class PoliceCar(Car):
	pass

workcar = WorkCar(120, 'white', 'Toyota Camry', False)
workcar.show_speed()