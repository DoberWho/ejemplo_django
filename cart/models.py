from django.db import models
from products.models import Product
from customers.models import Customers

class Carrito(models.Model):
	customer = models.ForeignKey(Customers, on_delete=models.CASCADE, blank=True)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	amount = models.PositiveIntegerField(default=1)

	class Meta:
		ordering = ['product']
		db_table = 'cart'
		