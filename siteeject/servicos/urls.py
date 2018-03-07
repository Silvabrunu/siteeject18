from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^sitesresponsivos$', views.sites_responsivos, name='sites_responsivos')
]