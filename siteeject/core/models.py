from django.db import models
from django.utils import timezone

class Campos(models.Model):
	title = models.CharField('Título', max_length=100)
	descricao = models.CharField('Descrição', max_length=800)
	create_date = models.DateField('Criado em', default=timezone.now())

	def __str__(self):
		return self.title


class QuemSomos(Campos):

	class Meta:
		verbose_name_plural = 'Quem Somos'


class Portifolio(Campos):
	categoria = models.CharField('Categoria', max_length=100)
	
	class Meta:
		verbose_name_plural = 'Portfólio'


class Depoimentos(Campos):
	nome = models.CharField('Nome', max_length=100)
	empresa = models.CharField('Empresa', max_length=100)