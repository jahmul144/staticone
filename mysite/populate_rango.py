import sys
sys.path.append("/home/ubuntu/virtenv/webstatic/staticone/")
print (sys.path)
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')
import django
django.setup()
from mysite.rango.models import Category,Page

def populate():
	python_pages = [{"title": "Official Python Tutorial", "url":"http://docs.python.org/2/tutorial/"},{"title":"How to Think like a Computer Scientist",
			"url":"http://www.greenteapress.com/thinkpython/"}]

	cats = {"Python": {"pages": python_pages}}


	for cat, cat_data in cats.items():
		print(cats.items())

populate()
