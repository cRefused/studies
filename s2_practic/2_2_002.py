# -*- coding: utf-8 -*-
# Кейс-задача № 2

from random import randint

if int(__import__('sys').version[0]) < 3:
  print('Необходима версия Python 3.0 и выше')
  exit()

run = 1 # флаг выполнения
cnt_attempts = 10 # кол-во попыток
grad_hint = 10 # градация подсказок

# диапазон
min_rnd = 1
max_rnd = 100

# сообщения
msg = ''
msg_cnt_attempts = ''
msg_error = ''

rnd_num = randint(min_rnd, max_rnd) # генерим число

while(run):
  user_num = input("Введите число от %d до %d (для выхода введите 0): " %(min_rnd, max_rnd))
  cnt_attempts -= 1

  msg_cnt_attempts = "\nОсталось попыток: %d\n---" %(cnt_attempts)
  msg_error = "Некорректные данные: [%s] %s" %(user_num, msg_cnt_attempts)

  try:
    user_num = int(user_num)
  except ValueError:
    print(msg_error)
    continue

  # если "0" - выходим
  # если не попали в диапазон, шо поделать...
  if(user_num == 0):
    run = 0
    continue
  elif(user_num < min_rnd or user_num > max_rnd ):
    print(msg_error)
    continue

  # Очень холодно / Холодно / Тепло
  if(user_num < rnd_num):
    if(user_num <= (rnd_num - grad_hint * 3)):
      msg = "Очень холодно, надо больше"
    elif(user_num <= (rnd_num - grad_hint * 2)):
      msg = "Холодно, надо больше"
    else:
      msg = "Тепло, надо больше"
  elif(user_num > rnd_num):
    if(user_num >= (rnd_num + grad_hint * 3)):
      msg = "Очень холодно, надо меньше"
    elif(user_num >= (rnd_num + grad_hint * 2)):
      msg = "Холодно, надо меньше"
    else:
      msg = "Тепло, надо меньше"
  elif(user_num == rnd_num):
      msg = "Угадали! Это число: %d!" %(rnd_num)
      msg_cnt_attempts = ''
      run = 0

  # если попытки закончились, заканчиваем игру
  if(cnt_attempts < 1 and run != 0):
    run = 0
    msg = "Вы исчерпали все попытки\nЗагаданое число было: %d" %(rnd_num)
    print(msg)
    continue
  else:
    print(msg, msg_cnt_attempts)



