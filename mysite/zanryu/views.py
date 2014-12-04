from django.shortcuts import render_to_response
from django.template import loader,RequestContext
from django.http import HttpResponse
from mysite.zanryu.models import Person

# Create your views here.
def index(request):
    person_list = Person.objects.all().order_by('-student_id')[:2]

    return render_to_response('zanryu/index.html', {'person_list':person_list}, context_instance=RequestContext(request))
