from django.db import models
from django.urls import reverse
from sizeapp import views
# Create your models here.
class Images(models.Model):
	name = models.CharField(max_length=32, blank=True)
	image = models.ImageField(upload_to='uploads', blank=True)

	def __str__(self):
		return self.name