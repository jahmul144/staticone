from django.http import HttpResponse

# Create your views here.i

def index(request):
	return HttpResponse("Rango says hey there partner!")

