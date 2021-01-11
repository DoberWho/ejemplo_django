from django.db import models
import ujson

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=250, unique=True, blank=False) 
	
	class Meta:
		db_table = 'categoria'

	def getJson(self):
		if None is self:
			return {}

		ctx = {}
		ctx['id'] = self.id
		ctx['name'] = self.name 

		return ctx

	def __str__(self):
		ctx = self.getJson()
		return ujson.dumps(ctx)

