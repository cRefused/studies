# Урок No11. Функции# # Задание No1# ● Создайте функцию, которая принимает в качестве параметра -# натуральное целое число.# ● Данная функция находит факториал полученного числа# Например, факториал числа 3 это число 6.# ● Теперь создайте список факториалов чисел от получившегося ранее# факториала 6, до 1.# В итоге, на вход программа получает например число 3, возвращает число 6# (факториал числа 3) и вам нужно сделать список из факториалов числа 6 в# убывающем порядке. Находим факториал числа 6 - это 720, затем от числа 5 -# это 120 и так далее вплоть до 1# То есть, результирующий список будет выглядеть в нашем примере так:# [720, 120, 24, 6, 2, 1]# # Лимит результата (ограничения для print)maxFactorials = 4300# сообщение, если результат большойmsgBigFactorial = 'Результат слишком большой (%s%s значений)'# стартуемdef fnStart():	try:		n = int(input('Введите натуральное целое число: '))	except:		print('Некорректные данные')		return False	if n <= 0:		print('Некорректные данные')		return False	# отдаем число считалке факториалов	fnGenFactorial(n)# функция получения списка факториаловdef fnGenFactorial(n):	# список факториалов	listFactorials = []	# считаем начальный факториал	factorial = n	for i in range(1, n):		factorial = factorial * i	# если результат большой, нет смысла ждать, 	# все равно в print() не влезет	if factorial > maxFactorials:		# на случай, если даже сюда не влазит		overBig = 10**(maxFactorials - 1)		if factorial > overBig:			print(msgBigFactorial %('свыше ', overBig))		else:			print(msgBigFactorial %('', factorial))		return False	# считаем факториалы по убывающей от начального и заносим в список	for n2 in range(factorial, 0, -1):		factorial2 = n2		for i2 in range(1, n2):			factorial2 = factorial2 * i2		listFactorials.append(factorial2)	print(listFactorials)fnStart()