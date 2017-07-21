from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.i

def index(request):
	context_dict = {'boldmessage': "crunchy cookie!"}
	#rango/index is set by the template dir so Django finds finds it through the settings file"
	return render(request, 'rango/index.html',context=context_dict)

def about(request):
	#Single quote inside double quote to say it is text uftiy use double quote it will fail
	#html1 = "<html><body>'Rango says this here is the about page!' <a href='/rango/'>Index</a></body></html>"
	return render(request,'rango/about.html',)

