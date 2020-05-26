from django.conf import settings
from django.db import models
from django.shortcuts import redirect, reverse

class Manufacturer(models.Model):
	name = models.CharField(max_length=30)
	slug = models.SlugField()

	def __str__(self):
		return self.name

class Box(models.Model):
	SIZE_CHOICES = (
		('small', 'Small'),
		('medium', 'Medium'),
		('large', 'Large'),
	)

	COLOR_CHOICES = (
		('white', 'White'),
		('brown', 'Brown'),
		('grey', 'Grey'),
	)

	manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=300, null=True)
	size = models.CharField(max_length=10, choices=SIZE_CHOICES, default='small')
	color = models.CharField(max_length=10, choices=COLOR_CHOICES, default='white')
	slug = models.SlugField()
	image = models.ImageField()
	price = models.FloatField()

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("boxes:box-detail", kwargs={
			'slug': self.slug
		})