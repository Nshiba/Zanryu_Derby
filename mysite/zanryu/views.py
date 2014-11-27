from django.shortcuts import render_to_response
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render_to_response('zanryu/index.html')
