from django.core.exceptions import ObjectDoesNotExist
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
		item = Tag()
		item.name = form.cleaned_data['name']
		item.save() 
		return HttpResponse(item)
	else:
		res = form.errors 
		return HttpResponse(res) 
	

def read(request): 
	# Listar todas las categorias 
	items = Tag.objects.all()
	ar = []
	for item in items:
		ar.append( str(item) )
	return HttpResponse(ar)

@csrf_exempt
def update(request): 
	# Editar una Categoria
	idForm = IDForm(data=request.POST) 
	nameForm = NameForm(data=request.POST)
	if (idForm.is_valid() and nameForm.is_valid() ):
		id = idForm.cleaned_data['id']
		name = nameForm.cleaned_data['name']
		try:
			obj = Tag.objects.get(id=id)
		except ObjectDoesNotExist as ex: 
			return HttpResponse("ID No Encontrado")
	
		try:
			obj = Tag.objects.get(name=name)
		except ObjectDoesNotExist as ex: 
			obj.name = name
			obj.save()
			return HttpResponse(obj)
		return HttpResponse("Ya Existe Esa Categoria")

	else:
		if (not idForm.is_valid()):
			return HttpResponse("FALTA ID")
		if (not nameForm.is_valid()):
			return HttpResponse("FALTA NAME")

	return HttpResponse("XXXX")

@csrf_exempt
def delete(request): 
	# Borrar una Categoria 
	form = IDForm(data=request.POST) 
	if (form.is_valid()):
		id = form.cleaned_data['id']
		obj = Tag.objects.filter(id=id)
		if None is obj:
			return HttpResponse("ID No Encontrado")
		else:
			strobj = str(obj)
			obj.delete()  
			return HttpResponse(strobj)
	else:
		res = form.errors 
		return HttpResponse(res) 
		