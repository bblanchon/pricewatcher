from django.contrib import admin
from prices.models import Shop, Product, Reference, Price

class ReferenceInline(admin.StackedInline):
	model = Reference

class ProductAdmin(admin.ModelAdmin):
	inlines = [ReferenceInline]

class PriceInline(admin.TabularInline):
	model = Price

class ReferenceAdmin(admin.ModelAdmin):
	inlines = [PriceInline]
	
admin.site.register(Shop)
admin.site.register(Product, ProductAdmin)
admin.site.register(Reference, ReferenceAdmin)