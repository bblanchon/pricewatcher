from django.shortcuts import render
from django.views import generic
from prices.models import Product

class IndexView(generic.ListView):
	template_name = 'prices/index.html'
	model = Product
