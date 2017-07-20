from django.http import HttpResponse

# Create your views here.i

def index(request):
	html = "<html><body>'Rango says he there partner!' <a href='/rango/about/'>About</a>"
	return HttpResponse(html)

def about(request):
	html1 = "<html><body>'Rango says this here is the about page!' <a href='/rango/'>Index</a>"
	return HttpResponse(html1)

