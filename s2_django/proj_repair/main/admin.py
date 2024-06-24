from django.contrib import admin

# импорт таблиц из файла .models
from .models import tech_db, type_t_db

# для отображения записей в админке нормальном виде а не как объекты
class tech_db_admin(admin.ModelAdmin):
  list_display = ('id', 'inv_num', 'type_t', 'terr_otd', 'defect', 'work_done', 'date_accept', 'date_issue')
  list_display_links = ('id', 'inv_num') # чтобы тыкать
  search_fields = ('inv_num', 'terr_otd') # поиск по полям

class type_t_db_admin(admin.ModelAdmin):
  list_display = ('id', 'title')

# регистрируем наши классы
admin.site.register(tech_db, tech_db_admin)
admin.site.register(type_t_db, type_t_db_admin)
