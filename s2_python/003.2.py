# Урок No3. Ввод-вывод и базовые переменные

# Задание No2
# А теперь мы с тобой напишем форму ввода ответа на тест по биологии для
# студентов. Он должен запрашивать по порядку этапы развития человека
# (проверим твое умение гуглить, что тоже очень важно для программиста. ) и в
# конце вывести все стадии, разделенные знаком =>, что будет означать
# постепенный переход от одного к другому. В следующих уроках мы дополним
# эту форму до полноценного теста, который будет проверять правильность
# ответов, а пока - начнем с малого. Напоминаем, что разделить эти данные
# тебе поможет команда sep внутри команды print, например, чтобы разделить
# переменные знаком + нужно ввести:
# print(a1, a2, a3, sep='+')
# Подсказка: последняя стадия развития - Homo sapiens sapiens.

headMsg = 'Введите стадии развития человека'

print(headMsg)
st1 = input('Первая стадия: ')
st2 = input('Вторая стадия: ')
st3 = input('Третья стадия: ')

print('Ваш ответ: ')
print(st1, st2, st3, sep=' => ')
