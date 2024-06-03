# Урок No6. Циклы while и for

# Задание No1
# Сначала вводится число N, затем вводится ровно N целых чисел. Подсчитайте,
# сколько из них равны нулю, и выведите это количество.

try:
	numberN = int(input('Введите число запросов: '))
except ValueError:
	print('Надо ввести целое число')
	exit()

cntZero = 0

for i in range(numberN):
	try:
		k = int(input('Введите число #%s: ' %(i + 1)))
	except ValueError:
		print('Надо ввести целое число')
		exit()
	if k == 0:
		cntZero += 1
		
print('Количество чисел, равных нулю: %s' %(cntZero))
