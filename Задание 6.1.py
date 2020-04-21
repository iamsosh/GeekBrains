'''Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
и метод running (запуск). Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
 третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только
 в указанном порядке (красный, желтый, зеленый).
 Проверить работу примера, создав экземпляр и вызвав описанный метод.'''
import time

class TrafficLight:
	def __running(color):
		if color == 'red':
			print("now it's red, lasting 7 seconds")
			time.sleep(7)
			print("now it's yellow, lasting 2 seconds")
			time.sleep(2)
			print("now it's green, lasting 10 seconds")
			time.sleep(10)
		elif color == 'yellow':
			print("now it's yellow, lasting 2 seconds")
			time.sleep(2)
			print("now it's green, lasting 10 seconds")
			time.sleep(10)
			print("now it's yellow, lasting 2 seconds")
			time.sleep(2)
			print("now it's red, lasting 7 seconds")
			time.sleep(7)
		elif color == 'green':
			print("now it's green, lasting 10 seconds")
			time.sleep(10)
			print("now it's yellow, lasting 2 seconds")
			time.sleep(2)
			print("now it's red, lasting 7 seconds")
			time.sleep(7)
		else :
			print('Wrong color!')

light = TrafficLight
color = str(input('Enter color: '))
light._TrafficLight__running(color)