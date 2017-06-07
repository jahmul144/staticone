from django.conf.urls import url

from mysite.polls  import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
