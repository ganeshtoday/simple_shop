from django.urls import path
from .views import box_list, box_detail

app_name = 'boxes'

urlpatterns = [
	path('', box_list, name='box-list'),
	path('<slug>/', box_detail, name='box-detail')
]