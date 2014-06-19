from django.db import models

class Shop(models.Model):
	name = models.CharField(max_length=32)
	url_regex = models.CharField(max_length=128)
	css_select = models.CharField(max_length=128)
	def __unicode__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=32)
	def __unicode__(self):
		return self.name

class Reference(models.Model):
	name = models.CharField(max_length=32)
	product = models.ForeignKey(Product)
	shop = models.ForeignKey(Shop)
	url = models.URLField()
	def __unicode__(self):
		return self.url

class Price(models.Model):
	start_time = models.DateTimeField(auto_now_add=True)
	end_time = models.DateTimeField(auto_now=True)
	price = models.DecimalField(max_digits=8, decimal_places=2)
	reference = models.ForeignKey(Reference)