# Урок No6. Циклы while и for

# Задание No2
# Вводится натуральное число X. Подсчитайте количество натуральных
# делителей числа X (включая 1 и само число). x ≤ 2e9 (2 миллиарда)

# счетчик натуральных делителей
cntNumberX = 0
# список делителей
listNumberX = []
# Число должно быть <= заданого
maxLimit = int(2e+9)

# просим ввести число с небольшой проверкой на валидность
try:
	numberX = int(input(f'Введите натуральное число, ≤ {maxLimit}: '))
except ValueError:
	print('Это не натуральное число')
	exit()
	
if numberX <= 0:
	print('Это не натуральное число')
	exit()
elif numberX > maxLimit:
	print(f'Число больше {maxLimit}')
	exit()
	
# проходимся по диапазону
for i in range(1, numberX + 1):
	# неплохо бы выводить хоть какой-то прогресс
	p = (i*100//numberX)
	print(f'Считаем... {p}% ', end='\r', flush=True)
	# собсна считаем
	if numberX % i == 0:
		cntNumberX += 1
		listNumberX.append(str(i))

print('Количество натуральных делителей числа %s по заданым условиям: %s' %(numberX, cntNumberX))
print(f"Список натуральных делителей: {' '.join(listNumberX)}")
