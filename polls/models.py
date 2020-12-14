from django.db import models
import ujson
import arrow

# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('Cuando Publicarlo')
	denunciado = models.BooleanField(default=False)

	def getJson(self):
		if None is self:
			return {}

		ctx = {}
		ctx['id'] = self.id
		ctx['question_text'] = self.question_text
		ctx['pub_date'] = arrow.get(self.pub_date , 'YYYYMMDDHHmm')

		return ctx

	def __str__(self):
		ctx = self.getJson()
		return ujson.dumps(ctx)

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def getJson(self):
		if None is self:
			return {}

		ctx = {}
		ctx['id'] = self.id
		ctx['choice_text'] = self.choice_text
		ctx['question'] = self.question.getJson() 

		return ctx


	def __str__(self):
		ctx = self.getJson()
		return ujson.dumps(ctx)


class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline