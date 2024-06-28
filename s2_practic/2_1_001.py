# Кейс-задача № 1

from math import factorial

run = 1
fl = 0

while(run):
  num = input("Введите положительное целое число (для выхода введите 0): ")

  try:
    num = int(num)
  except:
    print("Некорректные данные")
    continue

  if(num == 0):
    run = 0
    continue
  elif(num < 1):
    print("Некорректные данные")
    continue

  fn = factorial(num)
  print(f"Факториал числа {num} = {fn}")
