
from django.conf.urls import url

from mysite.uploads  import views

urlpatterns = [
    url(r'^$', views.model_upload, name='uploadindex'),
]
