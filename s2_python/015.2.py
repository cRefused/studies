# Урок No15. ООП
#
# Задание No2
#
# Создайте класс Autobus, который наследуется от класса Transport.
# Дайте аргументу Autobus.seating_capacity() значение по умолчанию 50.
# Используйте переопределение метода.
# Используйте следующий код для родительского класса транспортного
# средства:
# class Transport:
#   def __init__(self, name, max_speed, mileage):
#     self.name = name
#     self.max_speed = max_speed
#     self.mileage = mileage
#   def seating_capacity(self, capacity):
#     return f"Вместимость одного автобуса {self.name} {capacity} пассажиров"
# Ожидаемый результат вывода:
# Вместимость одного автобуса Renaul Logan: 50 пассажиров

class transport(object):
  capacity = 50

  def __init__(self, name, max_speed, mileage):
    self.name = name
    self.max_speed = max_speed
    self.mileage = mileage

  def seating_capacity(self, capacity):
    return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"

autobus = transport("Liaz", 90, 10000)

print(autobus.seating_capacity(autobus.capacity))
