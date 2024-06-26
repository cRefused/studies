from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

# импорт таблиц бд из файла .models
from .models import tech_db, equipment_name_db, otdel_db

def get_index(request):
  context = {
    'title': "Журнал ремонта",
    'tech_db_all': tech_db.objects.all()
  }
  return render(request, 'index.html', context)

# просмотр/редактирование карточки
@csrf_exempt
def get_rcard(request):
  if(request.POST):
    if('fn' in request.POST and request.POST['fn'] == 'open_rcard'):
      rcard_id = request.POST['rcard_id']
      cur_rcard = tech_db.objects.get(pk = rcard_id)
      context = {
        'cur_rcard': cur_rcard,
      }
      return render(request, 'edit_rcard.html', context)
    elif('fn' in request.POST and request.POST['fn'] == 'write_rcard'):

      rcard_id = request.POST['rcard_id']
      defect = request.POST['defect']
      work_done = request.POST['work_done']

      cur_rcard = tech_db.objects.get(pk = rcard_id)
      cur_rcard.defect = defect
      cur_rcard.work_done = work_done
      cur_rcard.save()

      context = {
        'rcard_id': rcard_id,
        'defect': defect,
        'work_done': work_done,
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
    if('fn' in request.POST and request.POST['fn'] == 'open_rcard'):
      cur_date = datetime.now
      equipment_name = equipment_name_db.objects.all().order_by('title')
      otdel_all = otdel_db.objects.all().order_by('name')
      context = {
        'cur_date': cur_date,
        'equipment_name': equipment_name,
        'otdel_all': otdel_all,
      }
      return render(request, 'new_rcard.html', context)
    elif('fn' in request.POST and request.POST['fn'] == 'write_rcard'):
      inv_num = request.POST['inv_num']
      equipment_id = request.POST['equipment_id']
      otdel_id = request.POST['otdel']
      defect = request.POST['defect']
      date_accept = request.POST['date_accept']
      tmp = list(date_accept.split('-'))

      date_accept_dmy = f"{tmp[2]}.{tmp[1]}.{tmp[0]}"
      equipment_name = equipment_name_db.objects.get(pk = equipment_id)
      otdel = otdel_db.objects.get(pk = otdel_id)

      tech_db.objects.create(
        inv_num = inv_num,
        equipment_name_id = equipment_id,
        otdel_id = otdel_id,
        defect = defect,
        date_accept = date_accept,
      )
      rcard_new_id = tech_db.objects.all().order_by('-pk')[0].id

      context = {
        'rcard_new_id': rcard_new_id,
        'inv_num': inv_num,
        'equipment_name': equipment_name.title,
        'otdel': otdel.name,
        'defect': defect,
        'date_accept': date_accept_dmy,
      }
      return render(request, 'past_rcard_to_tbody.html', context)
  else:
    msg = '<div class="main-frame">ERROR</div>'
    return HttpResponse(msg)
  msg = 'Nothing'
  return HttpResponse(msg)
