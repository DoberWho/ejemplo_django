from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from .forms import *
import ujson

# Create your views here.
@csrf_exempt
def create(request): 
	# Crear una Categoria
	form = NameForm(data=request.POST) 
	if (form.is_valid()):
		cat = Category()
		cat.name = form.cleaned_data['name']
		cat.save() 
		return HttpResponse(cat)
	else:
		res = form.errors 
		return HttpResponse(res) 
	

def read(request): 
	# Listar todas las categorias 
	items = Category.objects.all()
	ar = []
	for item in items:
		ar.append( str(item) )
	return HttpResponse(ar)

@csrf_exempt
def update(request): 
	# Editar una Categoria
	items = []
	return HttpResponse(items)

@csrf_exempt
def delete(request): 
	# Borrar una Categoria 
	form = IDForm(data=request.POST) 
	if (form.is_valid()):
		id = form.cleaned_data['id']
		cat = Category.objects.filter(id=id)
		if None is cat:
			return HttpResponse("ID No Encontrado")
		else:
			strCat = str(cat)
			cat.delete()  
			return HttpResponse(strCat)
	else:
		res = form.errors 
		return HttpResponse(res) 
		