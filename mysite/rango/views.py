from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.i

from mysite.rango.models import Category

def index(request):
	category_list = Category.objects.order_by('-likes')[:5]
	context_dict = {'boldmessage': "crunchy cookie!",'categories':category_list}
	#rango/index is set by the template dir so Django finds finds it through the settings file"
	return render(request, 'rango/index.html',context=context_dict)

def about(request):
	#Single quote inside double quote to say it is text uftiy use double quote it will fail
	#html1 = "<html><body>'Rango says this here is the about page!' <a href='/rango/'>Index</a></body></html>"
	return render(request,'rango/about.html',)

