# Урок No6. Циклы while и for

# Задание No3
# Вводятся целые числа A и B. Гарантируется, что A ≤ B. Выведите все четные
# числа на заданном отрезке через пробел.

# просим ввести числа с небольшой проверкой на валидность
try:
  a = int(input('Введите целое число A: '))
  b = int(input('Введите целое число B: '))
except ValueError:
  print('Это не целое число')
  exit()
  
if a > b:
  print('B должно быть больше или равно A')
  exit()

# список, который заполним подходящими числами
listEvenNumbers = []

# проверяем диапазон, добавляем нужное в список
for i in range(a, b + 1):
  if i % 2 == 0:
  	listEvenNumbers.append(str(i))

# строка чисел через пробел
strEvenNumbers = ' '.join(listEvenNumbers)

print(f'Четные числа на отрезке от {a} до {b}: {strEvenNumbers}')