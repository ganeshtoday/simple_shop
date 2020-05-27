from django.urls import path
from .views import add_to_cart, remove_from_cart, order_view, checkout, confirm_order, order_history, payment_complete

app_name = 'shopping_cart'

urlpatterns = [
	path('add-to-cart/<box_slug>/',
		add_to_cart,
		name='add-to-cart'),
	path('remove-from-cart/<box_slug>/',
		remove_from_cart,
		name='remove-from-cart'),
	path('order-summary/',
		order_view,
		name='order-summary'),
	path('checkout/',
		checkout,
		name='checkout'),
	path('payment-complete/',
		payment_complete,
		name='payment-complete'),
	path('confirm-order/',
		confirm_order,
		name='confirm-order'),
	path('order-history/',
		order_history,
		name='order-history'),
]