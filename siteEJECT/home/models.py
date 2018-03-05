# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

############ Models para o Slide ###########

class SlideShow(models.Model):
	title = models.CharField('Título', max_length=100)
	order = models.IntegerField('Ordem de apresentação do slide', unique=True)
	advertising = models.TextField('Anúncio', max_length=200)
	description = models.TextField('Descrição', max_length=500)

	imageGeral = models.ImageField(upload_to='home/imagens/slide', verbose_name='Imagem')

	
	class Meta:
		verbose_name = 'Slide'
		verbose_name_plural = 'Slides'
		ordering = ['order']

	def __str__(self):
		return self.title


class Partner(models.Model):
	name = models.CharField('Nome', max_length=50)
	link = models.URLField('Link', max_length=500)
	image = models.ImageField(upload_to='home/imagens/parceiros', verbose_name='Imagem')
	# slug = models.SlugField('Atalho', max_length=400, blank='True')
	
	class Meta:
		verbose_name = 'Parceiro'
		verbose_name_plural = 'Parceiros'
		ordering = ['name']

	def __str__(self):
		return self.name

	# def get_absolute_url(self):
	# 	return reverse('perfil', kwargs={'slug':self.slug})


# class Information(models.Model):
# 	adress = models.CharField('Localização', max_length=200)
# 	phone = models.CharField('Celular', max_length=15)
# 	telephone = models.CharField('Telefone Fixo', max_length=20)
# 	whatsapp= models.CharField('WhatsApp', help_text="Colocar todos os números juntos. Exemplo: 5584988990055", max_length=20)
# 	instagran = models.CharField('Link do Instagran', max_length=100)
# 	facebook = models.CharField('Link do Facebook', max_length=100)
# 	schedule = models.CharField('Horário de atendimento', max_length=100)

	
# 	class Meta:
# 		verbose_name = 'Informação'
# 		verbose_name_plural = 'Informações'
# 		ordering = ['adress']

# 	def __str__(self):
# 		return self.adress



# class Business(models.Model):
# 	operates = models.CharField('Área de Atuação', max_length=50)
# 	slug = models.SlugField('Atalho', max_length=400, blank='True')
# 	description = models.TextField('Descrição', max_length=200)
# 	image = models.ImageField(upload_to='home/imagens/atuacao', verbose_name='Imagem')

# 	text = RichTextField('Texto')

# 	class Meta:
# 		verbose_name = 'Área de Atuação'
# 		verbose_name_plural = 'Áreas de Atuações'
# 		ordering = ['operates']

# 	def __str__(self):
# 		return self.operates

# 	def get_absolute_url(self):
# 		return reverse('area:detalhe', kwargs={'slug':self.slug})
