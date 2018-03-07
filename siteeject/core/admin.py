from django.contrib import admin
from .models import QuemSomos, Portifolio, Depoimentos, Parceiros
from siteeject.forms import Correio

class Newsletter(admin.ModelAdmin):
	form = Correio()
	fieldsets = (
		('Nome', {'fields': 'nome'}),
		('Email', {'fields': 'email'}),
		('Empresa', {'fields': 'empresa'}),
	)

admin.site.register(QuemSomos)
admin.site.register(Portifolio)
admin.site.register(Depoimentos)
admin.site.register(Parceiros)
admin.site.register(Correio, Newsletter)
