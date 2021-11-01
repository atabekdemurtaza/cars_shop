from django.db import models
from datetime import datetime

class Car(models.Model):

	state_choice = (

		('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),

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
	description = models.TextField(verbose_name='Описание')
	car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Загружать первое фото', blank=True)
	car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Загружать второе фото', blank=True)
	car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Загружать третье фото', blank=True)
	car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Загружать четвертое фото', blank=True)
	car_photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Загружать пятое фото', blank=True)
	features = models.CharField(choices=features_choices, max_length=100, verbose_name='Особенности')
	body_style = models.CharField(max_length=100, verbose_name='Тип кузова')
	engine = models.CharField(max_length=100, verbose_name='Мотор')
	transmission = models.CharField(max_length=100, verbose_name='Трансмиссия')
	interior = models.CharField(max_length=100, verbose_name='Интерьер')
	miles = models.IntegerField(verbose_name='Миль')
	doors = models.CharField(choices=door_choices, max_length=100, verbose_name='Двери')
	passengers = models.IntegerField(verbose_name='Пассажиры')
	vin_no = models.CharField(max_length=100, verbose_name='Вин нет')
	milage = models.IntegerField(verbose_name='Пробег')
	fuel_type = models.CharField(max_length=100, verbose_name='Тип топливо')
	no_of_owners = models.CharField(max_length=100, verbose_name='Владелец')
	is_featured = models.BooleanField(max_length=100, verbose_name='Представлен')
	created_date = models.DateTimeField(default=datetime.now, blank=True, verbose_name='Дата выпуска')

	def _str__(self):

		return self.car_title

	class Meta:

		verbose_name_plural = 'Машины'



