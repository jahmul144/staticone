from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.i

from mysite.rango.models import Category,Page
from mysite.rango.forms import CategoryForm

def index(request):
	category_list = Category.objects.order_by('-likes')[:5]
	page_list = Page.objects.order_by('-views')[:5]
	
	context_dict = {'boldmessage': "crunchy cookie!",'categories':category_list,'pages':page_list}
	#rango/index is set by the template dir so Django finds finds it through the settings file"
	return render(request, 'rango/index.html',context=context_dict)

def about(request):
	#Single quote inside double quote to say it is text uftiy use double quote it will fail
	#html1 = "<html><body>'Rango says this here is the about page!' <a href='/rango/'>Index</a></body></html>"
	return render(request,'rango/about.html',)


def show_category(request,category_name_slug):
	context_dict = {}
	try:
		category = Category.objects.get(slug=category_name_slug)
		
		pages = Page.objects.filter(category=category)
		#Add new item to dictionary with key value pair aDict = {} aDict{'key'] = value pattern
		context_dict['pages'] = pages
		context_dict['category'] = category

	except:
		context_dict['category'] = None
		context_dict['pages'] = None


	return render(request, 'rango/category.html',context=context_dict)


def add_category(request):
	'''A HTTP POST?'''
	form = CategoryForm()
	if request.method == 'POST':
		form = CategoryForm

		'''Have we been provided with a valid form?'''
		if form.is_valid():
			'''save the new category to the database.'''
			form.save(commit=True)
			'''Now the category is saved we can now redirect to index page'''
			return index(request)
		else:
			print(form.errors)
	
	''' will handle the bad form, new form, or no for supplied cases, render the form with error messages if any'''
	return render(request, 'rango/add_category.html', {'form':form})

