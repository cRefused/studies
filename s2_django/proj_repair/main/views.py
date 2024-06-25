from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# импорт таблиц бд из файла .models
from .models import tech_db

def get_index(request):
  context = {
    'title': "Журнал ремонта",
    'tech_db_all': tech_db.objects.all()
  }
  return render(request, 'index.html', context)

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
