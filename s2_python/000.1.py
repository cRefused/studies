# -*- coding: utf-8 -*-
# Есть строка со словами через пробел
# Задача: разбить строку по пробелам, 
# слова добавить в массив
# а еще (в качестве бонуса, почему бы и нет) 
# уберем всякие запятые с точками.
#
# тоже самое на си:
# https://github.com/cRefused/c_test/blob/main/split_string.c

# эти символы будем убирать
other_spr = ".,!@#$^&*/\\\%{}[]()-"

# фраза, которую надо разбить на слова
myString = "Функция#  (strtok),  [выделяет],,,  **очередную.- {часть} /- /строки, на которую указывает  аргумент str";

# убираем символы из other_spr
for c in other_spr:
  myString = myString.replace(c, '')

# разбиваем по пробелам
myString = myString.split()

# выводим результат
for i in range(0, len(myString)):
  print('[%-2s][%s]' %(i, myString[i]))
  
print()

