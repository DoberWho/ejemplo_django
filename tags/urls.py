from django.urls import path

from . import views

# CRUD
urlpatterns = [
	path('create', views.create, name='tags_create'),
    path('read',   views.read,   name='tags_read'),
    path('update', views.update, name='tags_update'),
    path('delete', views.delete, name='tags_delete'),
]