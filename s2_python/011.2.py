# Урок No11. Функции
#
# Задание No2
# В Урок No10. Задание No1 вы создавали словарь с информацией о питомце.
# Теперь нам нужна "настоящая" база данных для ветеринарной клиники.
# Подробный требуемый функционал будет ниже. Пока что справка:
# ● Создайте функцию create
# ● Создайте функцию read
# ● Создайте функцию update
# ● Создайте функцию delete
# ● Используйте словарь pets, который будет предоставлен ниже, либо
# создайте свой аналогичный
# Функция create:
# Данная функция будет создавать новую запись с информацией о питомце и
# добавлять эту информацию в наш словарь pets
# Функция read
# Данная функция будет отображать информацию о запрашиваемом питомце в
# виде:
# Это желторотый питон по кличке "Каа". Возраст питомца: 19 лет. Имя владельца:
# Саша
# Функция update
# Данная функция будет обновлять информацию об указанном питомце
# Функция delete
# Данная функция будет удалять запись о существующем питомце
# Структруа результирующего словаря pets будет как и в Урок No10. Задание No1,
# но с небольшим видоизменением:
# Словарь pets
# pets = {
# 1:
# {
# "Мухтар": {
# "Вид питомца": "Собака",
# "Возраст питомца": 9,
# "Имя владельца": "Павел"
# },
# },
# 2:
# {
# "Каа": {
# "Вид питомца": "желторотый питон",
# "Возраст питомца": 19,
# "Имя владельца": "Саша"
# },
# },
# # и так далее
# }
# Здесь, 1 и 2 - это идентификаторы наших питомцев. Это уникальные ключи, по
# которым мы сможем обращаться к нашим записям в "базе данных"
# Суть будущей программы будет заключаться в следующем:
# ● Программа будет работать с помощью цикла while с условием command
# != 'stop', то есть до тех пор, пока на предложение ввести команду,
# пользователь не введёт слово stop
# ● Перед взаимодействием с "базой данных" запрашивается одна из
# команд в качестве пользовательского ввода. Пусть это будет
# переменная command
# ● Функция create должна добавлять новую информацию таким образом,
# чтобы идентификатор увеличивался на единицу. Чтобы у вас была
# возможность получать последний ключ в словаре воспользуйтесь
# импортом модуля collections. В начале вашей программы пропишите
# строчку: import collection, а в функции create в первых строках пропишите
# следующий код:
# def create():
# last = collections.deque(pets, maxlen=1)[0]
# last в данном случае и будет число последнего ключа (или в нашей
# логике - идентификатора записи). Именно его и необходимо будет
# увеличивать на единицу при добавлении следующей записи.
# Как вам уже известно - суть функций заключается в том, чтобы использовать
# один и тот же код в нескольких местах. В данной задаче вам предстоит
# получать информацию о питомце несколько раз. Чтобы не повторяться в коде,
# вам нужно создать такие функции
# getPet(ID):
# def getPet(ID):
# # функция, с помощью которой вы получите информацию о питомце в виде
# словаря
# # сделайте проверку, если питомца с таким ID нету в нашей "базе данных"
# # верните в этом случае False
# # а если питомец всё же есть в "базе данных" - верните информацию о нём
# # выглядеть это может примерно так:
# return pets[ID] if ID in pets.keys() else False
# getSuffix(age):
# def getSuffix(age):
# # функция, с помощью которой можно получить суффикс
# # 'год', 'года', 'лет'
# # реализацию этой функции вам предстоит придумать самостоятельно
# # функция будет возвращать соответствующую строку
# return
# getPetsList():
# def getPetsList():
# # Эта функция будет создана для удобства отображения всего списка питомцев
# # Информацию по каждому питомцу можно вывести с помощью цикла for
# Обратите внимание, если ID не существует в словаре с питомцами - будет
# возникать ошибка. Вам можно от неё избавиться, если правильно составить
# проверочное условие. Здесь не потребуется использовать такие конструкции,
# как try, except, чтобы обработать возникшую ошибку

from collections import deque

# база питомцев изначально не пустая
pets = {
1:{'Мухтар':{'vid':'собака','age':9,'name':'Иван'}},
2:{'Фрося':{'vid':'свинья','age':1,'name':'Иван'}}
}

# сообщение, если нет такого ID
msgPetNotExist = 'Питомец с таким ID не зарегистрирован'

# ф-ция добавления записи о питомце
def addPet():
  if len(pets) == 0:
    id = 1
  else:
    id = (deque(pets, maxlen=1)[0]) + 1
  print('Добавление записи о питомце')
  pName = input('Имя питомца: ')
  vid = input('Вид питомца: ')
  age = int(input('Возраст питомца: '))
  name = input('Имя владельца: ')
  pets[id] = {pName:{'vid':vid,'age':age,'name':name}}

  print('Запись добавлена:')
  getPetsList(id)

# ф-ция просмотра записи о питомце/ах
def readPet():
  id = int(input('Введите ID питомца (0 чтобы отобразить всех): '))
  getPetsList(id)

# ф-ция обновления записи о питомце
def updatePet():
  print('Редактирование записи о питомце')
  id = int(input('Введите ID питомца: '))
  if getPet(id):
    pName = input('Имя питомца: ')
    vid = input('Вид питомца: ')
    age = int(input('Возраст питомца: '))
    name = input('Имя владельца: ')
    pets[id] = {pName:{'vid':vid,'age':age,'name':name}}
    print('Информация о питомце обновлена:')
    getPetsList(id)
  else:
    print(msgPetNotExist)
    
# ф-ция удаления записи о питомце
def deletePet():
  print('Удаление записи о питомце')
  id = int(input('Введите ID питомца: '))
  if getPet(id):
    pets.pop(id)
    print(f'ID {id}: Информация о питомце удалена')
  else:
    print(msgPetNotExist)


# ф-ция проверки id
def getPet(id):
  return pets[id] if id in pets.keys() else False
  
# запрашиваем информацию о всех питомцах или об одном
def getPetsList(id):
  if id == 0:
    for p in pets:
      getPetsInfo(p)
  elif getPet(id):
    getPetsInfo(id)
  else:
    print(msgPetNotExist)

# получение информации о питомце и вывод на экран      
def getPetsInfo(id):
  for sp in pets[id]:
    s = getSuffix(pets[id][sp]['age'])
    print(f"ID {id}: Это {pets[id][sp]['vid']} по кличке \"{sp}\". Возраст питомца: {pets[id][sp]['age']} {s}. Имя владельца: {pets[id][sp]['name']}")

# ф-ция склонения года
def getSuffix(age):
# сверка по последней цифре
  petAgeY = int(str(age)[-1])
# костыль для диапазона 10-20
  petAgeY10 = int(str(age)[(len(str(age))-2)::])
  if (10 <= age <= 20) or (10 <= petAgeY10 <= 20):
    year = 'лет'
  elif petAgeY == 1:
    year = 'год'
  elif 2 <= petAgeY <= 4:
    year = 'года'
  else:
    year = 'лет'
  return year

# старт
def start():
  cmd = ''
  print()
  print('\n--------------------------------')
  print('     БАЗА ДАННЫХ ПИТОМЦЕВ   ')
  print('--------------------------------\n')
  while cmd != 'q':
    cmd = input('Введите команду ((a)dd | (r)ead | (u)pdate | (d)elete | (q)uit): ')
    if cmd == 'a':
      addPet()
    elif cmd == 'r':
      readPet()
    elif cmd == 'u':
      updatePet()
    elif cmd == 'd':
      deletePet()

start()


