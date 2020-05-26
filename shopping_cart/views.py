from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from boxes.models import Box
from .models import Order, OrderItem, Payment
import stripe
import random
import string

import logging
logger = logging.getLogger("mylogger")	

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_ref_code():
	return ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))

@login_required
def add_to_cart(request, box_slug):
	box = get_object_or_404(Box, slug=box_slug)
	try:
		quantity = int(request.GET['quantity'])
	except:
		quantity = 1

	order_item, created = OrderItem.objects.get_or_create(box=box, defaults={'quantity': quantity})
	order, created = Order.objects.get_or_create(user=request.user, is_ordered=False)
	order.ref_code = create_ref_code()
	order.items.add(order_item)
	order.save()
	return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

@login_required
def remove_from_cart(request, box_slug):
	box = get_object_or_404(Box, slug=box_slug)
	order_item = get_object_or_404(OrderItem, box=box)
	order = get_object_or_404(Order, user=request.user)
	order.items.remove(order_item)
	order.save()
	order_item.delete()
	return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

@login_required
def order_view(request):
	try:
		order = get_object_or_404(Order, user=request.user, is_ordered=False)
	except:
		order = None	
	context = {
		'order': order
	}
	return render(request, "order_summary.html", context)


@login_required
def checkout(request):
	order = get_object_or_404(Order, user=request.user, is_ordered=False)
	
	if request.method == "GET":

		# Create a Stripe PaymentIntent
		intent = stripe.PaymentIntent.create(
  			amount=int(order.get_total() * 100),
 			currency='usd',
  			metadata={'integration_check': 'accept_a_payment'},
		)

		context = {
			'order': order,
			'stripe_client_secret': intent.client_secret,
			'stripe_publish_key': settings.STRIPE_PUBLISH_KEY
		}
		return render(request, "checkout.html", context)

	if request.method == "POST":
		intent_id = request.POST.get('paymentIntent')

		# Create a payment object and link to the order
		payment = Payment.objects.create(user=request.user, 
						order=order,
						total_amount=order.get_total(),
						stripe_charge_id=intent_id)

		# Complete the order
		order.is_ordered = True
		order.save()

		context = {
			'order': order
		}

		# Redirect to success page
		return render(request, "order_confirm.html", context)


@login_required
def confirm_order(request):
	order = get_object_or_404(Order, user=request.user)
	context = {
		'order': order
	}
	return render(request, "order_confirm.html", context)


@login_required
def order_history(request):
	payments = Payment.objects.filter(user=request.user)
	context = {
		'payments': payments
	}
	return render(request, "order_history.html", context)