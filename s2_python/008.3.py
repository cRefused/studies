# Урок No8. Списки
# 
# Задание No3
# На берегу реки стояли n рыбаков, все они хотели перебраться на другой берег.
# Одна лодка может выдержать не более m килограмм, при этом в лодку
# помещается не более 2 человек. Определите, какое минимальное число лодок
# нужно, чтобы перевезти на другой берег всех рыбаков В первую строку
# вводится число m (1 ≤ m ≤ 10e6) - максимальная масса, которую может
# выдержать одна лодка. Во вторую строку вводится число n (1 ≤ n ≤ 100) -
# количество рыбаков. В следующие N строк вводится по одному числу Ai (1 ≤ Ai
# ≤ m) - вес каждого путешественника. Программа должна вывести одно число -
# минимальное количество лодок, необходимое для переправки всех рыбаков
# на противоположный берег.

# грузоподъемность лодки
minCarrying = 1
maxCarrying = int(10e+6)
carrying = int(input(f'Введите грузоподъемность лодки ({minCarrying} ≤ m ≤ {maxCarrying}): '))
# максимальное количество людей в лодке
maxBodyWherry = 2

if (minCarrying > carrying) or (carrying > maxCarrying):
	print(f'Грузоподъемность лодки должна быть в пределах от {minCarrying} до {maxCarrying}')
	exit()

# количество кандидатов на перевозку
minBodies = 1
maxBodies = 100
bodies = int(input('Введите количество рыбаков (1 ≤ n ≤ 100): '))

if (minBodies > bodies) or (bodies > maxBodies):
	print(f'Количество рыбаков должно быть в пределах от {minBodies} до {maxBodies}')
	exit()

# список кандидатов в килограммах
massBody = []
# начальное количество отправленных лодок
countWherrys = 0

# заполняем список кандидатов
for i in range(bodies):
	m = int(input(f'Введите вес рыбака #{i+1}: '))
	if m > carrying:
		print('Этот слишком жирный, остается на берегу')
		continue
	elif m <= 0:
		print('Это фейковый рыбак, вычеркиваем')
		continue
	else:
		massBody.append(m)

# сортируем рыбаков
list.sort(massBody)

print()
print(f'Сортируем рыбаков по весу: {massBody}')
print('Рассаживаем по лодкам:')

# отправляем рыбаков
while massBody:
	iMassBody = (len(massBody) - 1)
	# рассаживаем рыбаков в лодки, компонуя жирных с дрыщами
	if len(massBody) > 1:
		# если оба влазят, отправляем
		if massBody[iMassBody] + massBody[0] <= carrying:
			print(massBody[iMassBody], massBody[0])
			massBody.pop(iMassBody)
			massBody.pop(0)
			countWherrys += 1
		# иначе отправляем жирного
		else:
			print(massBody[iMassBody])
			massBody.pop(iMassBody)
			countWherrys += 1
	# отправляем последнего, если остался
	else:
		print(massBody[iMassBody])
		massBody.pop(iMassBody)
		countWherrys += 1

print('-----------------------------------')
print(f'Количество лодок, необходимое для перевозки рыбаков (по {maxBodyWherry} в лодке и с грузоподьемностью {carrying}): {countWherrys}')