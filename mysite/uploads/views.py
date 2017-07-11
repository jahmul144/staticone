from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from mysite.uploads.models import Document
from mysite.uploads.forms import DocumentForm
# Create your views here. 
def model_upload(request):
	if request.method == 'POST':
	form = DocumentForm(request.POST, request.FILES)
	if form.is_valid():
		form.save(commit=True)
		return HttpResponseRedirect(reverse('uploadindex'))
	else:
		print(form.errors)
        	#form = DocumentForm()
	return render(request, 'uploads/index.html', {'form': form})
