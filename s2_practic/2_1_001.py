# -*- coding: utf-8 -*-
# Кейс-задача № 1

from math import factorial

if int(__import__('sys').version[0]) < 3:
  print('Необходима версия Python 3.0 и выше')
  exit()

run = 1
fl = 0

while(run):
  num = input("Введите положительное целое число (для выхода введите 0): ")

  try:
    num = int(num)
  except ValueError:
    print("Некорректные данные")
    continue

  if(num == 0):
    run = 0
    continue
  elif(num < 1):
    print("Некорректные данные")
    continue

  fl = factorial(num)
  print("Факториал числа %s = %s" %(num, fl))
