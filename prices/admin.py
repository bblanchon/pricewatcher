from django.contrib import admin
from prices.models import Shop, Product, Reference, Price

class ReferenceInline(admin.StackedInline):
	model = Reference

class ProductAdmin(admin.ModelAdmin):
	inlines = [ReferenceInline]

class ReferenceAdmin(admin.ModelAdmin):
	list_display = ('product', 'name', 'shop')
	
admin.site.register(Shop)
admin.site.register(Product, ProductAdmin)
admin.site.register(Reference, ReferenceAdmin)