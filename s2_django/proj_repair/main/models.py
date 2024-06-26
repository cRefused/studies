from django.db import models

class tech_db(models.Model):
  inv_num = models.CharField(max_length = 32, verbose_name="Инв. номер")
  equipment_name = models.ForeignKey('equipment_name_db', on_delete=models.PROTECT, null=True, blank=True, verbose_name="Наименование")
  otdel = models.ForeignKey('otdel_db', on_delete=models.PROTECT, null=True, blank=True, verbose_name="Отдел")
  defect = models.TextField(verbose_name="Неисправность")
  work_done = models.TextField(blank=True, verbose_name="Проделаная работа")
  date_accept = models.DateField(verbose_name="Дата приемки")
  date_issue = models.DateField(null=True, blank=True, verbose_name="Дата выдачи")

  # для описания обекта в админке
  class Meta:
    verbose_name = "Тенику"
    verbose_name_plural = "Теника"
    ordering = ['-id','-date_accept']

class equipment_name_db(models.Model):
  title = models.CharField(max_length = 32, db_index=True, verbose_name="Наименование")

  class Meta:
    verbose_name = "Наименование"
    verbose_name_plural = "Наименование"
    ordering = ['title']

class otdel_db(models.Model):
  name = models.CharField(max_length = 32, db_index=True, verbose_name="Отделы")

  class Meta:
    verbose_name = "Отдел"
    verbose_name_plural = "Отделы"
    ordering = ['name']
