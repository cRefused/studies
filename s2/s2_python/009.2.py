# Урок No9. Множества
# 
# Задание No2
# Вводятся два списка чисел, которые могут содержать до 100000 чисел
# каждый. Все числа каждого списка находятся на отдельной строке. Выведите,
# сколько чисел содержится одновременно как в первом списке, так и во
# втором.

maxN = 100000

n1 = set(map(int, input(f'[Список #1] Введите числа через пробел (не больше {maxN} штук): ').split()))
if (len(n1) > maxN):
  print(f'Надо не больше {maxN} штук')
  exit()
  
n2 = set(map(int, input(f'[Список #2] Введите числа через пробел (не больше {maxN} штук): ').split()))
if (len(n2) > maxN):
  print(f'Надо не больше {maxN} штук')
  exit()

#n3 = n1.intersection(n2)
n3 = n1 & n2

print(f'Совпадающих чисел: {len(n3)}')