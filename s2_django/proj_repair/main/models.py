from django.db import models

class tech_db(models.Model):
  inv_num = models.CharField(max_length = 32, verbose_name="Инв. номер")
  type_t = models.ForeignKey('type_t_db', on_delete=models.PROTECT, null=True, blank=True, verbose_name="Наименование")
  terr_otd = models.CharField(max_length = 32, verbose_name="Отдел")
  defect = models.TextField(verbose_name="Неисправность")
  work_done = models.TextField(blank=True, verbose_name="Проделаная работа")
#  date_accept = models.DateTimeField(auto_now_add = True, verbose_name="Дата приемки")
  date_accept = models.DateTimeField(verbose_name="Дата приемки")
  date_issue = models.DateTimeField(null=True, blank=True, verbose_name="Дата выдачи")

  # для описания обекта в админке
  class Meta:
    verbose_name = "Тенику"
    verbose_name_plural = "Теника"
    ordering = ['-date_accept']

class type_t_db(models.Model):
  title = models.CharField(max_length = 32, db_index=True, verbose_name="Наименование")

  class Meta:
    verbose_name = "Наименование"
    verbose_name_plural = "Наименование"
    ordering = ['title']
