# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

class SlideShowAdmin(admin.ModelAdmin):
	list_display = ['title','order','advertising','description']
	search_fields = ['title']
	list_filter = ['title']

	#prepopulated_fields = { 'slug':('title',)}

admin.site.register(SlideShow, SlideShowAdmin)

class PartnerAdmin(admin.ModelAdmin):
	list_display = ['name','link','image']
	search_fields = ['name']
	list_filter = ['name']

admin.site.register(Partner, PartnerAdmin)

