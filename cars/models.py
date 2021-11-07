from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
import uuid 

class Car(models.Model):

	state_choice = (

		('Tas', 'Tashkent'),
        ('Sam', 'Samarkand'),
        ('Karakalpakstan', 'Karakalpakstan'),
        ('Urg', 'Urgench'),
        ('Fer', 'Fergana'),
        ('And', 'Andijan'),
        ('Nam', 'Namangan'),
        ('Gul', 'Gulistan'),
        ('Jiz', 'Jizzax'),
        ('Qar', 'Qarshi'),
        ('Ter', 'Termez'),
        ('Bux', 'Buxara'),
        ('Nav', 'Navoi'),
	)

	features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

	door_choices = (

		('2', '2'),
		('3', '3'),
		('4', '4'),
		('5', '5'),
		('6', '6'),

	)


	year_choice = []
	for i in range(2000, (datetime.now().year + 1)):
		year_choice.append((i, i))

	car_title = models.CharField(max_length=255, verbose_name='Название')
	state = models.CharField(choices=state_choice, max_length=100, verbose_name='Штат')
	city = models.CharField(max_length=100, verbose_name='Город')
	color = models.CharField(max_length=100, verbose_name='Цвет')
	model = models.CharField(max_length=100, verbose_name='Марка')
	year  = models.IntegerField(('year'), choices=year_choice)
	condition = models.CharField(max_length=100, verbose_name='Состояние')
	price = models.IntegerField(verbose_name='Цена')
	description = RichTextField()
	car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Загружать первое фото', blank=True)
	car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Загружать второе фото', blank=True)
	car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Загружать третье фото', blank=True)
	car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Загружать четвертое фото', blank=True)
	car_photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Загружать пятое фото', blank=True)
	features = MultiSelectField(choices=features_choices, verbose_name='Особенности')
	body_style = models.CharField(max_length=100, verbose_name='Тип кузова')
	engine = models.CharField(max_length=100, verbose_name='Мотор')
	transmission = models.CharField(max_length=100, verbose_name='Трансмиссия')
	interior = models.CharField(max_length=100, verbose_name='Интерьер')
	miles = models.IntegerField(verbose_name='Миль')
	doors = models.CharField(choices=door_choices, max_length=10, verbose_name='Двери')
	passengers = models.IntegerField(verbose_name='Пассажиры')
	vin_no = models.CharField(max_length=100, verbose_name='Вин нет')
	milage = models.IntegerField(verbose_name='Пробег')
	fuel_type = models.CharField(max_length=50, verbose_name='Тип топливо')
	no_of_owners = models.CharField(max_length=100, verbose_name='Владелец')
	is_featured = models.BooleanField(max_length=100, verbose_name='Представлен', default=False )
	created_date = models.DateTimeField(default=datetime.now, blank=True, verbose_name='Дата выпуска')
    

	def __str__(self):

		return self.car_title

	class Meta:

		verbose_name_plural = 'Машины'



