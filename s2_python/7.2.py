# Урок No7. Строки

# Задание No2
# Дана строка, длина которой не превосходит 1000. Вам требуется
# преобразовать все идущие подряд пробелы в один. Выведите измененную
# строку.

# максимальная длина строки
maxLenStr = 1000

strRaw = input(f'Введите строку с одиночными, двойными и т.д. пробелами, не превышающую {maxLenStr} знаков: ')

# смотрим длину
strRange = len(strRaw)
# сюда будем заносить обработаные символы
strNew = []

# хоть какая-то проверка на валидность
if strRange > maxLenStr:
	print(f'Строка превышает {maxLenStr} знаков')
	exit()

# проходимся по строке, пропуская идущие подряд пробелы
for i in range(strRange):
	if (i+1 < strRange) and strRaw[i] == ' ' and strRaw[i+1] == ' ':
		continue
	else:
		strNew.append(strRaw[i])

strNewJ = ''.join(strNew)
print(f'Строка без лишних пробелов: {strNewJ}')

