from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^sitesresponsivos$', views.sites_responsivos, name='sites_responsivos'),
	url(r'^sistemasweb$', views.sistemas_web, name='sistemas_web'),
	url(r'^hospedagem$', views.hospedagem, name='hospedagem'),
]