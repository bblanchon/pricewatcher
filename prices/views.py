from django.shortcuts import render, get_object_or_404
from prices.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
	products = []
	for p in Product.objects.all():
		references = []
		for r in p.reference_set.all():
			price = r.price_set.order_by("-end_time").first()
			if price != None:
				references.append({
					'name': r.name,
					'shop': r.shop.name,
					'price': price.price
					})
		products.append({
			'name': p.name,
			'references': references,
			'id': p.id
			})
	context = {'products': products}
	return render(request, 'prices/index.html', context)

@login_required
def product(request, pk):
	p = get_object_or_404(Product, pk=pk)

	references = []
	for r in p.reference_set.all():
		history = []
		for x in r.price_set.order_by("start_time"):
			history.append(
				{
					'time': x.start_time,
					'price': x.price
				})
			history.append(
				{
					'time': x.end_time,
					'price': x.price
				})
		references.append(
			{
				'name': r.name,
				'shop': r.shop.name,
				'history': history
			})
	product = {
	 'name': p.name,
	 'references': references
	}

	context = {'product': product}

	return render(request, 'prices/product.html', context)


