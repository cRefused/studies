# Урок No8. Списки
# 
# Задание No1
# В первой строке вводится число N. Далее в N строк вводится N чисел (1 ≤ N ≤
# 10000), по одному числу на строке. Все числа по модулю не превышают 10e5.
# Переверните массив чисел. Выведите N чисел - перевернутый массив.

# небольшая проверка на валидность
try:
	quantityQuery = int(input('Введите целое число: '))
except ValueError:
	print('Это не целое число')
	exit()

# массив чисел
arrN = []
# сумма введенных чисел по модулю
m = 0
# предел суммы
maxM = 10e+5

# запрашиваем ввод чисел, проверяем на соответствие условиям
for i in range(quantityQuery):
	try:
		n = int(input(f'Введите целое число #{i} (1 ≤ N ≤ 10000): '))
	except ValueError:
		print(f'Это не целое число')
		continue
	# плюсуем по модулю
	m += abs(n)
	# если сумма меньше, добавляем в список, иначе ругаемся и пропускаем это число
	if m <= maxM:
		arrN.append(n)
	else:
		print(f'Сумма чисел по модулю превышает {maxM}, пропускаем число [{n}]')
		m -= abs(n)
		continue
		
print(f'Введенные числа в обратном порядке: {list(reversed(arrN))}')