# Урок No9. Множества
# 
# Задание No3
# Во входную строку водится последовательность чисел через пробел. Для
# каждого числа выведите слово ”YES” (в отдельной строке), если это число
# ранее встречалось в последовательности или ”NO”, если не встречалось.

a = set()

while True:
  try:
    i = int(input('Введите число (для завершения введите 0): '))
  except ValueError:
    print('Надо ввести целое число')
    continue

  if i == 0:
    a.add(i)
    print(f'Введенные числа: {a}')
    exit()
  if i in a:
    print('YES')
  else:
    print('NO')
    a.add(i)