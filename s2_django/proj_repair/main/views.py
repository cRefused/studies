from django.shortcuts import render
#from django.http import HttpResponse

# импорт таблиц бд из файла .models
from .models import tech_db

def get_index(request):
  context = {
    'title': "Журнал ремонта",
    'news_all': tech_db.objects.all()
  }
  return render(request, 'index.html', context)

def get_tech(request, tid):
  tech_cur = tech_db.objects.get(pk = tid)
  context = {
    'tech_cur': tech_cur,
  }
  return render(request, 'tech.html', context)
