# Урок No5. Логические и условные операторы

# Задание No2
# Дано слово из маленьких латинских букв. Сколько там согласных и гласных
# букв? Гласными называют буквы «a», «e», «i», «o», «u».
# Для решения задачи создайте переменную и в неё положите слово с
# помощью input()
# А также определите количество каждой из этих гласных букв Если какой-то из
# перечисленных букв нет - Выведите False

strWord = input('Введите слово из маленьких латинских букв: ')

# список гласных
listLetterG = ['a', 'o', 'e', 'i', 'u', 'y']

# сюда будем вносить совпадения по гласным и согласным
strWordG = {}
strWordNotG = {}

# количество гласных и согласных
cntStrWordG = 0
cntStrWordNotG = 0

# ищем совпадения и заполняем списки гласных и согласных
for k in strWord:
  if k in listLetterG:
    if not k in strWordG:
      strWordG[k] = []
    strWordG[k].append(k)
  else:
    if not k in strWordNotG:
      strWordNotG[k] = []
    strWordNotG[k].append(k)

# считаем количество гласных, если гласной нет, то проставляем False
for i in listLetterG:
  if i in strWordG:
    strWordG[i] = len(strWordG[i])
    cntStrWordG += strWordG[i]
  else:
    strWordG[i] = False

# считаем количество согласных
for i in strWordNotG:
  cntStrWordNotG += len(strWordNotG[i])


print('Количество гласных букв: %s' %(cntStrWordG))
print('Количество согласных букв: %s' %(cntStrWordNotG))
print('Количество совпадений по гласным: %s' %(strWordG))



