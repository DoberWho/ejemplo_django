from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='polls_indice'),
    path('prueba/', views.prueba, name='polls_prueba'),
]