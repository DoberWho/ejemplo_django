from django.db import models

# Create your models here.
class Customers(models.Model):
	username = models.EmailField(max_length=50, unique=False, blank=False) 
	password = models.CharField(max_length=50, unique=False, blank=False) 
	name = models.CharField(max_length=50, unique=False, blank=False) 
	lastname = models.CharField(max_length=50, unique=False, blank=False) 

	class Meta:
		ordering = ['username']
		db_table = 'clientes'
