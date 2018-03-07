# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-28 01:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('link', models.CharField(max_length=500, verbose_name='Link')),
                ('image', models.ImageField(upload_to='home/imagens/parceiros', verbose_name='Imagem')),
            ],
            options={
                'verbose_name_plural': 'Parceiros',
                'verbose_name': 'Parceiro',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SlideShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('order', models.IntegerField(verbose_name='Ordem de apresentação do slide')),
                ('advertising', models.TextField(max_length=200, verbose_name='Anúncio')),
                ('description', models.TextField(max_length=500, verbose_name='Descrição')),
                ('imageGeral', models.ImageField(upload_to='home/imagens/slide', verbose_name='Imagem')),
            ],
            options={
                'verbose_name_plural': 'Slides',
                'verbose_name': 'Slide',
                'ordering': ['order'],
            },
        ),
    ]