# Урок No16. Классы и объекты
#
# Задание No1
#
# Создайте класс Касса, который хранит текущее количество денег в кассе, у
# него есть методы:
# ● top_up(X) - пополнить на X
# ● count_1000() - выводит сколько целых тысяч осталось в кассе
# ● take_away(X) - забрать X из кассы, либо выкинуть ошибку, что не
# достаточно денег

class cashbox(object):
  cur_many = 2500

  def top_up(self, many):
    self.cur_many += many
    msg = f"Пополнение: +{many}"
    return msg

  def count_1000(self):
    cnt = self.cur_many // 1000
    msg = f"Осталось целых тысяч: {cnt}"
    return msg

  def take_away(self, many):
    if many > self.cur_many:
      msg = f"В кассе недостаточно денег"
    else:
      msg = f"Снятие: -{many}"
    return msg

shop = cashbox()

print(shop.count_1000())
