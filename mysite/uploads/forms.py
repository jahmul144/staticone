from django import forms
from mysite.uploads.models import Document

class DocumentForm(forms.ModelForm):
	class Meta:
		model = Document
		fields = ['description', 'document']
