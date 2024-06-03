# Урок No5. Логические и условные операторы

# Задание No3
# Два инвестора - Майкл и Иван хотят вложиться в стартап. Фаундеры сказали,
# что минимальная сумма инвестиций - X долларов, больше инвестировать
# можно сколько угодно. У Майкла A долларов, у Ивана B долларов. Если оба
# могут вложиться - выведите 2, если только Майкл - Mike, если только Иван -
# Ivan, если не могут по отдельности, но вместе им хватает - 1, если никто - 0.

moneyStartup = 1000

try:
	moneyMike = int(input('Сколько денег у Майка?: '))
	moneyIvan = int(input('Сколько денег у Ивана?: '))
except ValueError:
	print('Деньги должны быть выражены целым числом')
	exit()

moneySum = moneyIvan + moneyMike
msg = ''

if moneyMike >= moneyStartup and moneyIvan >= moneyStartup:
	msg = 2
elif moneyMike >= moneyStartup:
	msg = 'Mike'
elif moneyIvan >= moneyStartup:
	msg = 'Ivan'
elif moneySum >= moneyStartup:
	msg = 1
else:
	msg = 0
	
print('Код состоятельности: %s' %(msg))

