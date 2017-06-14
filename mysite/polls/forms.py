from django import forms
from django.forms import ModelForm
from mysite.polls.models import Stores

class StoreForm(ModelForm):
	class Meta:
		model = Stores
		fields = ['name','address','city','state']




