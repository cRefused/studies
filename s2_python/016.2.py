# Урок No16. Классы и объекты
#
# Задание No2
#
# Создайте класс Черепашка, который хранит позиции x и y черепашки, а также
# s - количество клеточек, на которое она перемещается за ход
# у этого класс есть методы:
# ● go_up() - увеличивает y на s
# ● go_down() - уменьшает y на s
# ● go_left() - уменьшает x на s
# ● go_right() - увеличивает y на s
# ● evolve() - увеличивает s на 1
# ● degrade() - уменьшает s на 1 или выкидывает ошибку, когда s может
# стать ≤ 0
# ● count_moves(x2, y2) - возвращает минимальное количество действий, за
# которое черепашка сможет добраться до x2 y2 от текущей позиции

class turtle(object):
  x = 0
  y = 0
  s = 0

  def __init__(self, x, y, s):
    self.x = x
    self.y = y
    self.s = s

  def go_up(self, s): # увеличивает y на s
    self.y += s
    return self.y

  def go_down(self, s): # уменьшает y на s
    self.y -= s
    return self.y

  def go_left(self, s): # уменьшает x на s
    self.x -= s
    return self.x

  def go_right(self, s): # увеличивает x на s
    self.x += s
    return self.x

  def evolve(self): # увеличивает s на 1
    self.s += 1
    return self.s

  def degrade(self): # уменьшает s на 1 или выкидывает ошибку, когда s может стать ≤ 0
    if (self.s - 1) < 0:
      msg = f"Некуда ходить"
    else:
      self.s -= 1
      msg = self.s
    return msg

my_turtle = turtle(10, 20, 20)

print(my_turtle.go_up(1))
print(my_turtle.go_down(1))

print(my_turtle.go_left(1))
print(my_turtle.go_right(1))

print(my_turtle.evolve())

for i in range(my_turtle.s + 2):
  print(my_turtle.degrade())
