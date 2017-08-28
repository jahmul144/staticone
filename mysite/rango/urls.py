from django.conf.urls import url

from mysite.rango  import views

urlpatterns = [
	url(r'^$', views.index, name='indexrango'),
	url(r'^about/', views.about, name='indexrangoabout'),
	url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category,name='show_category'),
]
