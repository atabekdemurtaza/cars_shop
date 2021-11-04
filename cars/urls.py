from django.urls import path 
from .views import cars 
from .views import car_detail

urlpatterns = [
	
	path('', cars, name='cars'),
	path('<int:id>', car_detail, name='car_detail'),

]
