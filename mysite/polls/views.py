from django.shortcuts import render
from django.http import HttpResponse

from mysite.polls.models import Stores
def index(request):
	downtown_store = Stores.objects.get(name="Corporate")
	store_name = downtown_store.name
	store_address = downtown_store.address
	store_state = downtown_store.state
	context = {'store_name':store_name, 'store_address':store_address, 'store_state':store_state}    	
	return render(request,'polls.index.html',context)


