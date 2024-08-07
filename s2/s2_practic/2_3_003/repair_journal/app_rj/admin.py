from django.contrib import admin

# импорт таблиц из файла .models
from .models import tech_db, equipment_name_db, otdel_db
from .models_login import login_db

# для отображения записей в админке нормальном виде а не как объекты
class tech_db_admin(admin.ModelAdmin):
  list_display = ('id', 'inv_num', 'equipment_name', 'otdel', 'defect', 'work_done', 'date_accept', 'date_issue')
  list_display_links = ('id', 'inv_num') # чтобы тыкать
  search_fields = ('inv_num', 'otdel') # поиск по полям

class equipment_name_db_admin(admin.ModelAdmin):
  list_display = ('id', 'title')

class otdel_db_admin(admin.ModelAdmin):
  list_display = ('id', 'name')

# LOGIN DB
class login_db_admin(admin.ModelAdmin):
  list_display = ('login', 'passwd',
    'rights', 'session', 'surname', 'first_name',
    'last_name', 'locked')


# регистрируем наши классы
admin.site.register(tech_db, tech_db_admin)
admin.site.register(equipment_name_db, equipment_name_db_admin)
admin.site.register(otdel_db, otdel_db_admin)
admin.site.register(login_db, login_db_admin)
