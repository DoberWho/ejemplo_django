from django.db import models
import ujson

from categories.models import Category
from tags.models import Tag

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=250, unique=False, blank=False)
	price = models.DecimalField(max_digits=7, decimal_places=2)
	stock = models.PositiveIntegerField(default=1)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False)
	tags = models.ManyToManyField(Tag)

	class Meta:
		ordering = ['name']
		db_table = 'product'

	def getJson(self):
		if None is self:
			return {}

		ctx = {}
		ctx['id'] = self.id
		ctx['name'] = self.name 
		ctx['price'] = self.price 
		ctx['stock'] = self.stock 
		ctx['category'] = self.category.getJson() 

		return ctx

	def __str__(self):
		return self.name
