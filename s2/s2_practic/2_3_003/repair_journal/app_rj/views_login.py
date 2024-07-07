from django.shortcuts import render
#from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

# импорт таблиц бд из файла .models
from .models_login import login_db

def get_login(request):
  title = 'Авторизация'
  context = {'title': title}
  return render(request, 'app_rj/login.html', context)

def fn_login(request):
  if(request.POST):
    if('fn' in request.POST and request.POST['fn'] == 'login'):
      username = request.POST['username']
      password = request.POST['password']
  return 0
