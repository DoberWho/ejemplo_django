from django import forms
from .models import *


class CategoryForm(forms.ModelForm):
	name = forms.CharField()
	class Meta:
		model = Category
		fields = ['name']

		error_messages = {
			'name': {
				'required': ('Please let us know what to call you!'),
				'max_length': ("This writer's name is too long."),
			},
		} 

	def clean_name(self):
		data = self.cleaned_data['name']
		print("DATA"+str(data))
		if None is data:
			return None 
		return data

class NameForm(forms.Form):
	name = forms.CharField(label='Your name', max_length=100)

	def clean_name(self):
		data = self.cleaned_data['name']
		if None is data:
			return None 
		if data.strip():
			return data.strip()
		return None # ''


class IDForm(forms.Form):
	id = forms.IntegerField()

	def clean_id(self):
		data = self.cleaned_data['id']
		if None is data:
			return None  
		return data