from django import forms
from .models import * 

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
 