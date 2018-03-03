from django.conf.urls import url
from core import views
from django.conf.urls.static import static
from siteeject import settings

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^quemsomos$', views.quem_somos, name='quem_somos')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)