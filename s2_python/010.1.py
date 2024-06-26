# Урок No10. Словари
# 
# Задание No1
# Ранее вы выполняли задание связанное с ветеринарной клиникой. В той
# задаче вам предстояло вывести информацию о питомце на экран. Сейчас вам
# необходимо создать словарь pets = {}
# Примерный вид будет следующим:
# pets = {
# "Имя питомца": {
# 'Вид питомца': # придумайте каким образом сюда внести информацию,
# 'Возраст питомца': # придумайте каким образом сюда внести информацию,
# 'Имя владельца': # придумайте каким образом сюда внести информацию
# }
# }
# У вас должен получиться словарь, с ещё одним словарём внутри. То есть, есть
# словарь pets. Он в себе хранит ещё один словарь, который обозначается
# именем питомца. Имя питомца также нужно каким-то образом вносить туда.
# Задача не будет считаться выполненной, если вы заходите сразу внести
# информацию, не прибегая в функции input()
# Например:
# pets = {
# "Мухтар": {
# "Вид питомца": "Собака",
# "Возраст питомца": 9,
# "Имя владельца": "Павел"
# }
# }
# Так должен будет выглядеть результируюший словарь, но первоначальный
# его вид - пустой. Его необходимо заполнить пользовательским вводом через
# консоль с помощью функции input(), а не вписать значения уже в самом коде.
# Возраст питомца должен быть типа int Всё остальное - строки
# Так как возраст питомца указывается типом int. Необходимо, в соответствии с
# указанным возрастом выводит год, года или лет. Например:
# Его возраст: 24 года
# Его возраст: 21 год
# Его возраст: 19 лет
# И теперь осталось только получить всю информацию о питомце в виде
# строки, как из задания по Урок No3. Ввод-вывод и базовые переменные. Задание
# No1, но с небольшими изменениями. Для получения информации необходимо
# воспользоваться методами словаря keys() и values():
# Это желторотый питон по кличке "Каа". Возраст питомца: 19 лет. Имя владельца:
# Саша

pets = {}
year = ''

petName = input('Имя питомца: ')
petVid = input('Вид питомца: ')

petAge = int(input('Возраст питомца: '))

petOwner = input('Имя владельца: ')

pets[petName] = {'petVid':petVid, 'petAge':petAge, 'petOwner':petOwner}

# для склонения года/лет...
petAgeY = int(str(petAge)[-1])
petAgeY10 = int(str(petAge)[(len(str(petAge))-2)::])
if (10 <= petAge <= 20) or (10 <= petAgeY10 <= 20):
  year = 'лет'
elif petAgeY == 1:
  year = 'год'
elif 2 <= petAgeY <= 4:
  year = 'года'
else:
  year = 'лет'

print(f"Это {pets[petName]['petVid']} по кличке \"{petName}\". Возраст питомца: {pets[petName]['petAge']} {year}. Имя владельца: {pets[petName]['petOwner']}")


