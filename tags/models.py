from django.db import models
import ujson

# Create your models here.
class Tag(models.Model):
	name = models.CharField(max_length=50, unique=False, blank=False)  

	class Meta:
		ordering = ['name']
		db_table = 'tag'

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