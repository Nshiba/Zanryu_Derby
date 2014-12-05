from django.shortcuts import render_to_response
from django.template import loader,RequestContext
from django.http import HttpResponse
from mysite.zanryu.models import Person, Log

# Create your views here.
def index(request):
    person_list = Person.objects.all().order_by('-student_id')[:2]

    return render_to_response('zanryu/index.html', {'person_list':person_list}, context_instance=RequestContext(request))

def insert(request):
    if request.method == 'POST':
        i_student_id = request.POST['student_id']
        i_name = request.POST['name']
        i_now = request.POST['now']
        i_date = request.POST['date']

        insert_person = Person(student_id = i_student_id, name = i_name, now_entry_exit = i_now)
        insert_log = Log(student_id = i_student_id, entry_exit = i_now, dump_date = i_date)

        insert_person.save()
        insert_log.save()
    else:
        return render_to_response('zanryu/nodata.html')
