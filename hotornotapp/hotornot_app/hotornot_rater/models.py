from django.db import models

class User(models.Model):
	username = models.CharField(max_length=200)
	password = models.CharField(max_length=200)

	def __str__(self):
		return self.username

class Images(models.Model):
	city = models.CharField(max_length=200)
	country = models.CharField(max_length=200)
	#imageUploaded = models.ImageField()
	isHot = models.IntegerField()
	isNot = models.IntegerField()

	def __str__(self):
		return self.id