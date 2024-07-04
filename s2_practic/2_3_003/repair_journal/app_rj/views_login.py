from django.shortcuts import render
#from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

# импорт таблиц бд из файла .models
# from .models import tech_db, equipment_name_db, otdel_db

def get_login(request):
  title = 'Авторизация'
  context = {'title': title}
  return render(request, 'app_rj/login.html', context)
