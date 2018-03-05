from django.shortcuts import render

def sites_responsivos(request):
	context = {}

	return render(request, 'sites-responsivos.html', context)