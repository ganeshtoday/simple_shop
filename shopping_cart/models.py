from django.db import models
from django.conf import settings
from boxes.models import Box

class OrderItem(models.Model):
	box = models.ForeignKey(Box, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)

	def __str__(self):
		return self.box.name


class Order(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,
							 on_delete=models.CASCADE)

	is_ordered = models.BooleanField(default=False)
	items = models.ManyToManyField(OrderItem)
	ref_code = models.CharField(max_length=50,null=True)
	payment_intent_id = models.CharField(max_length=100,null=True)

	def __str__(self):
		return self.ref_code

	def get_total(self):
		sum = 0.0
		for item in self.items.all():
			sum += item.box.price * item.quantity
		return sum


class Payment(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,
							 on_delete=models.CASCADE)
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	total_amount = models.FloatField(null=True)
	date_paid = models.DateTimeField(auto_now_add=True)
	stripe_charge_id = models.CharField(max_length=100)

	def __str__(self):
		return self.stripe_charge_id