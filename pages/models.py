from django.db import models

class Team(models.Model):

	#photo, 
	#first_name, 
	#last_name, designal 
	#icon, facebook, 
	#twitter_link,
	#google_plus_link
	#created_date

	first_name = models.CharField(
		max_length = 255,
		verbose_name = 'Имя'
	)
	last_name = models.CharField(
		max_length=255,
		verbose_name='Фамилия',
	)
	designation = models.CharField(
		max_length=255,
		verbose_name='Профессия'
	)
	photo = models.ImageField(
		upload_to='photos/%Y/%m/%d/',

	)
	facebook_link = models.URLField(
		max_length=100,

	)
	twitter_link = models.URLField(max_length=100)
	google_plus_link = models.URLField(max_length=100)
	created_date = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return f'{self.first_name} {self.last_name}'

	class Meta:

		verbose_name_plural = 'Команда'

