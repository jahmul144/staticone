from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from mysite.polls.models import Stores
from mysite.polls.forms import StoreForm
def index(request):
	downtown_store = Stores.objects.get(name="Corporate")
	store_name = downtown_store.name
	store_address = downtown_store.address
	store_state = downtown_store.state
	if request.method == 'Post':
		form = StoreForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('index'))
	else:
		form = StoreForm() 
	
	context = {'store_name':store_name, 'store_address':store_address, 'store_state':store_state, 'form':form,} 
	    	
	return render(request,'polls/index.html',context)


