from django.contrib import admin

# импорт таблиц из файла .models
from .models import news_db, category_db

# для отображения записей в админке нормальном виде а не как объекты
class news_db_admin(admin.ModelAdmin):
  list_display = ('id', 'category', 'title', 'created_at', 'is_published')
  list_display_links = ('id', 'title') # чтобы тыкать
  search_fields = ('title', 'content') # поиск по полям
  list_filter = ['category'] # фильтрация
  list_editable = ['is_published']

class category_db_admin(admin.ModelAdmin):
  list_display = ('id', 'title')
  list_display_links = ('id', 'title') # чтобы тыкать
  # search_fields = ('title') # поиск по полям


# регистрируем наши классы
admin.site.register(news_db, news_db_admin)
admin.site.register(category_db, category_db_admin)
