from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
import ujson

# Create your views here.
def create(request): 
	# Crear una Categoria
	items = []

	form = CategoryForm(request.POST)
	

	return HttpResponse(items)

def read(request): 
	# Listar todas las categorias
	items = Category.objects.all()
	return HttpResponse(items) 

def update(request): 
	# Editar una Categoria
	items = []
	return HttpResponse(items)

def delete(request): 
	# Borrar una Categoria
	items = []
	return HttpResponse(items)