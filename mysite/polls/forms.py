from django import forms

from mysite.polls.models import Stores

class StoreForm(forms.ModelForm):
	model = Stores
	fields = ('downtown_store','store_name','store_address','store_state',)




