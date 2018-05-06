# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

class Campo(models.Model):
	title = models.CharField('Título', max_length=100, blank=True)
	descricao = models.CharField('Descrição', max_length=800, blank=True)
	create_date = models.DateField('Criado em', default=timezone.now())

	def __str__(self):
		return self.title

class CampoImagem(Campo):
	imagem = models.ImageField('Selecione uma imagem', upload_to='core/images/', default='')
		

class QuemSomos(Campo):

	class Meta:
		verbose_name_plural = 'Quem Somos'


class VejaMais(models.Model):
	title = models.CharField('Título', max_length=100, blank=True)
	descricao = models.TextField('Descrição', blank=True)

	class Meta:
		verbose_name_plural = 'Quem Somos'


class Portifolio(CampoImagem):
	categorias = (
		('NA', 'Outros'),
		('SR', 'Sites Responsivos'),
		('SW', 'Sistemas Web')
	)
	categoria = models.CharField('Categoria', max_length=100, choices=categorias, default='NA')
	link = models.CharField('Link', max_length=100, default='')
	
	class Meta:
		verbose_name_plural = 'Portfólio'


class Depoimentos(CampoImagem):
	nome = models.CharField('Nome', max_length=100)
	empresa = models.CharField('Empresa', max_length=100)

	class Meta:
		verbose_name_plural = 'Depoimentos'

class Parceiros(CampoImagem):
	link = models.CharField('Link', max_length=100, default='')

	class Meta:
		verbose_name_plural = 'Parceiros'

class Correio(models.Model):
	nome = models.CharField('Nome', max_length=100)
	email = models.CharField('Email', max_length=100)
	empresa = models.CharField('Empresa', max_length=100)

	def __str__(self):
		return self.nome

	class Meta:
		verbose_name_plural = 'Correio'