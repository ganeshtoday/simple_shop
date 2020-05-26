from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Box
from shopping_cart.models import Order, OrderItem

def box_list(request):
	# display a list of books
	queryset = Box.objects.all()
	context = {
		'queryset': queryset
	}
	return render(request, "box_list.html", context)

@login_required
def box_detail(request, slug):
	# display a box product detail page
	box = get_object_or_404(Box, slug=slug)
	box_is_in_cart = False
	
	try:
		order_qs = Order.objects.filter(user=request.user)
		if order_qs.exists():
			order = order_qs[0]
			order_item_qs = OrderItem.objects.filter(box=box)
			if order_item_qs.exists():
				order_item = order_item_qs[0]
				if order_item in order.items.all():
					box_is_in_cart = True
	except:
		box_is_in_cart = False

	context = {
		'box': box,
		'in_cart': box_is_in_cart
	}
	return render(request, "box_detail.html", context)