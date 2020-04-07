#words = (input('Введите слова '))
#space = words.find(' ')
#j = 1
#l = len(words[:space])
#for i in words :
#	if l < 11 :
#		print(j, words[i:space])
#		words = words[space+1:]
#		space = words.find(' ')
#		i -= 1
#		l = len(words[:space])
#	else :
#		print(j, words[i:i+9])
#		j += 1
#		words = words[space+1:]
#		space = words.find(' ')
#		i -= 1
#		l = len(words[:space])
###############################
#Решение задачи далось очень трудно.
#Изначально пытался делать через слайсинг и искать пробелы между словами
#Но не получилось довести до ума, ошибка в значениях внутри []
words = (input('Введите слова '))
divided_words = words.split()
counting = 1
for i, j in enumerate (divided_words) :
    print(counting, j[:10])
    counting += 1