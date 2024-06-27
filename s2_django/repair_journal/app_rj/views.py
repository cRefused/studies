from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

# импорт таблиц бд из файла .models
from .models import tech_db, equipment_name_db, otdel_db

def get_index(request):
  href_font = dict()
  tech_db_all = tech_db.objects.all()

  for i in tech_db_all:
    if (i.work_done != '' and i.date_issue != None):
      i.href_font = 'font_normal'
    else:
      i.href_font = 'font_red'

  context = {
    'title': "Журнал ремонта",
    'tech_db_all': tech_db_all,
  }
  return render(request, 'main/index.html', context)

# просмотр/редактирование карточки
@csrf_exempt
def get_rcard(request):
  rcard_ro = 0
  if(request.POST):
    # просмотр
    if('fn' in request.POST and request.POST['fn'] == 'open_rcard'):
      rcard_id = request.POST['rcard_id']
      cur_rcard = tech_db.objects.get(pk = rcard_id)
      # если эти поля заполнены, карточка только на чтение
      if (cur_rcard.work_done != ''
        and cur_rcard.date_issue != None):
          rcard_ro = 1

      context = {
        'rcard_ro': rcard_ro,
        'cur_rcard': cur_rcard,
        'cur_date': datetime.now,
      }
      return render(request, 'main/edit_rcard.html', context)
    # редактирование
    elif('fn' in request.POST and request.POST['fn'] == 'write_rcard'):
      rcard_id = request.POST['rcard_id']
      work_done = request.POST['work_done']
      date_issue = request.POST['date_issue']

      # если стоит галка "еще не выдано"
      if date_issue == '0':
        date_issue = None
        date_issue_dmy = None
        href_font = 'font_red'
      else:
        tmp = list(date_issue.split('-'))
        date_issue_dmy = f"{tmp[2]}.{tmp[1]}.{tmp[0]}"
        href_font = 'font_normal'

      # заносим в бд
      cur_rcard = tech_db.objects.get(pk = rcard_id)
      cur_rcard.work_done = work_done
      cur_rcard.date_issue = date_issue
      cur_rcard.save()

      # отдаем ответ фронту
      context = {
        'rcard_id': rcard_id,
        'work_done': work_done,
        'date_issue': date_issue_dmy,
        'href_font': href_font,
      }
      return JsonResponse(context)
  else:
    msg = '<div class="main-frame">ERROR</div>'
    return HttpResponse(msg)
  msg = 'Nothing'
  return HttpResponse(msg)

# добавление новой карточки
@csrf_exempt
def new_rcard(request):
  if(request.POST):
    # открыли форму новой карточки
    if('fn' in request.POST and request.POST['fn'] == 'open_rcard'):
      # текущая дата
      cur_date = datetime.now
      # список наименований
      equipment_name = equipment_name_db.objects.all().order_by('title')
      # список отделов
      otdel_all = otdel_db.objects.all().order_by('name')
      context = {
        'cur_date': cur_date,
        'equipment_name': equipment_name,
        'otdel_all': otdel_all,
      }
      return render(request, 'main/new_rcard.html', context)
    # добавление записи
    elif('fn' in request.POST and request.POST['fn'] == 'write_rcard'):
      inv_num = request.POST['inv_num']
      equipment_id = request.POST['equipment_id']
      otdel_id = request.POST['otdel']
      defect = request.POST['defect']
      date_accept = request.POST['date_accept']
      tmp = list(date_accept.split('-'))

      # добавляем запись в бд
      query = tech_db(
        inv_num = inv_num,
        equipment_name_id = equipment_id,
        otdel_id = otdel_id,
        defect = defect,
        date_accept = date_accept,
      )
      query.save()

      # получаем последний id
      #rcard_new_id = tech_db.objects.all().order_by('-pk')[0].id
      rcard_new_id = query.id

      # для вставки в html тег
      date_accept_dmy = f"{tmp[2]}.{tmp[1]}.{tmp[0]}"
      equipment_name = equipment_name_db.objects.get(pk = equipment_id)
      otdel = otdel_db.objects.get(pk = otdel_id)

      # отдаем ответ фронту
      context = {
        'rcard_new_id': rcard_new_id,
        'inv_num': inv_num,
        'equipment_name': equipment_name.title,
        'otdel': otdel.name,
        'defect': defect,
        'date_accept': date_accept_dmy,
      }
      return render(request, 'main/past_rcard_to_tbody.html', context)
  else:
    msg = '<div class="main-frame">ERROR</div>'
    return HttpResponse(msg)
  msg = 'Nothing'
  return HttpResponse(msg)
