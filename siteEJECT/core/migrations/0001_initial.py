# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-27 18:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('descricao', models.CharField(max_length=800, verbose_name='Descrição')),
                ('create_date', models.DateField(default=datetime.datetime(2018, 2, 27, 18, 32, 49, 85549, tzinfo=utc), verbose_name='Criado em')),
            ],
        ),
        migrations.CreateModel(
            name='CampoImagem',
            fields=[
                ('campo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Campo')),
                ('imagem', models.ImageField(default='', upload_to='core/images/', verbose_name='Selecione uma imagem')),
            ],
            bases=('core.campo',),
        ),
        migrations.CreateModel(
            name='QuemSomos',
            fields=[
                ('campo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Campo')),
            ],
            options={
                'verbose_name_plural': 'Quem Somos',
            },
            bases=('core.campo',),
        ),
        migrations.CreateModel(
            name='Depoimentos',
            fields=[
                ('campoimagem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.CampoImagem')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('empresa', models.CharField(max_length=100, verbose_name='Empresa')),
            ],
            options={
                'verbose_name_plural': 'Depoimentos',
            },
            bases=('core.campoimagem',),
        ),
        migrations.CreateModel(
            name='Parceiros',
            fields=[
                ('campoimagem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.CampoImagem')),
            ],
            options={
                'verbose_name_plural': 'Parceiros',
            },
            bases=('core.campoimagem',),
        ),
        migrations.CreateModel(
            name='Portifolio',
            fields=[
                ('campoimagem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.CampoImagem')),
                ('categoria', models.CharField(choices=[('NA', 'Outros'), ('SR', 'Sites Responsivos'), ('SW', 'Sistemas Web')], default='NA', max_length=100, verbose_name='Categoria')),
            ],
            options={
                'verbose_name_plural': 'Portfólio',
            },
            bases=('core.campoimagem',),
        ),
    ]
