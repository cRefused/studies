# Урок No15. ООП
#
# Задание No1
#
# Есть родительский класс:
# class Transport:
#   def __init__(self, name, max_speed, mileage):
#     self.name = name
#     self.max_speed = max_speed
#     self.mileage = mileage
# Создайте объект Autobus, который унаследует все переменные и методы
# родительского класса Transport и выведете его.
# Ожидаемый результат вывода:
# Название автомобиля: Renaul Logan Скорость: 180 Пробег: 12

class transport:
  def __init__(self, name, max_speed, mileage):
    self.name = name
    self.max_speed = max_speed
    self.mileage = mileage

autobus = transport("Liaz", 90, 10000)

print("Название автомобиля: %s Скорость: %s Пробег: %s" %(autobus.name, autobus.max_speed, autobus.mileage,))
