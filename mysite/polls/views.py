from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from mysite.polls.models import Stores
from mysite.polls.forms import StoreForm
def index(request):
	downtown_store = Stores.objects.get(name="E2")
	store_name = downtown_store.name
	store_address = downtown_store.address
	store_state = downtown_store.state
	if request.method == 'Post':
		form = StoreForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return HttpResponseRedirect(reverse('index'))
	else:
		form = StoreForm() 
	
	context = {'store_name':store_name, 'store_address':store_address, 'store_state':store_state, 'form':form,} 
	    	
	return render(request,'polls/index.html',context)


