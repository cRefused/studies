from django.shortcuts import render
#from django.http import HttpResponse

# импорт таблиц бд из файла .models
from .models import news_db, category_db

def index(request):
  category_all = category_db.objects.all()

  context = {
    'title': "Список новостей",
    'news_all': news_db.objects.all(),
    'category_all': category_all
  }
  return render(request, 'news/index.html', context)

def get_category(reguest, cid):
  news_category = news_db.objects.filter(category_id = cid)
  category_all = category_db.objects.all()
  category_cur = category_db.objects.get(pk = cid) # pk - primary key
  context = {
    'news_category': news_category,
    'category_all': category_all,
    'category_cur': category_cur,
  }
  return render(reguest, 'news/category.html', context)

