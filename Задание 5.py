#Долго думал над решением. 
#Понял, что можно просто добавить любое число, отсортировать и просто перевернуть
#И получится правильный ответ
rating = [7, 5, 3, 3, 2]
new_element = (int(input('Введите новый элемент ')))
rating.append(new_element)
ordered_rating = sorted(rating)
print(ordered_rating[::-1])