from django.db import models

class news_db(models.Model):
  title = models.CharField(max_length = 150, verbose_name="Заголовок")
  content = models.TextField(blank = True, verbose_name="Контент")
  created_at = models.DateTimeField(auto_now_add = True, verbose_name="Создано")
  updated_at = models.DateTimeField(auto_now = True, verbose_name="Обновлено")
  photo = models.ImageField(upload_to = 'media/%Y/%m/%d', null=True, blank=True, verbose_name="Фото")
  is_published = models.BooleanField(default = True, verbose_name="Опубликовано")
  category = models.ForeignKey('category_db', on_delete=models.PROTECT, null=True, blank=True, verbose_name="Категория")

  # для описания обекта в админке
  class Meta:
    verbose_name = "БД Новостей"
    verbose_name_plural = "БД Новостей"
    ordering = ['-created_at']

class category_db(models.Model):
  title = models.CharField(max_length = 150, db_index=True, verbose_name="Категория")

  # для описания обекта в админке
  class Meta:
    verbose_name = "Категория"
    verbose_name_plural = "Категориии"
    ordering = ['-id']
