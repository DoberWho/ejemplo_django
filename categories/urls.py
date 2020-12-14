from django.urls import path

from . import views

# CRUD
urlpatterns = [
	path('create', views.create, name='category_create'),
    path('read',   views.read,   name='category_read'),
    path('update', views.update, name='category_update'),
    path('delete', views.delete, name='category_delete'),
]