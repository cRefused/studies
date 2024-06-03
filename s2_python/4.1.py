# Урок No4. float, int и арифметические операции

# Задание No1
# Пользователь вводит стороны прямоугольника, выведите его площадь и
# периметр. На вход программе могут подаваться как целые числа, так и
# вещественные

try:
	arrSides = list(map(int, input('введите стороны прямоугольника, разделенные пробелом: ').split()))
except ValueError:
	print('Некорректные данные')
	exit()

if len(arrSides) != 2:
	print('Надо ввести 2 числа')
	exit()

rectangleArea = arrSides[0] * arrSides[1]
perimeterArea = (arrSides[0] + arrSides[1]) * 2

print('Площадь прямоугольника со сторонами %sx%s: %s' %(arrSides[0], arrSides[1], rectangleArea))
print('Периметр прямоугольника со сторонами %sx%s: %s' %(arrSides[0], arrSides[1], perimeterArea))
