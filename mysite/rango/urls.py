from django.conf.urls import url

from mysite.rango  import views

urlpatterns = [
    url(r'^$', views.index, name='indexrango'),
]
