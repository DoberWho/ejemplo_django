from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request): 
	preguntas = Choice.objects.all() 
	return HttpResponse(preguntas)

def prueba(request):

	data = {}
 
	data['preguntas'] = Choice.objects.all() 

	return render(
        request,
        'choices_template.html',
        context=data,
    ) 
