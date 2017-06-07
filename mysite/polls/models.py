from django.db import models

# Create your models here.

class Stores(models.Model):
	name  = models.CharField(max_length=200)
	address = models.CharField(max_length=30)
	city = models.CharField(max_length=30)
	state = models.CharField(max_length=2)
	def __str__(self):
		return "%s (%s,%s)" % (self.name, self.city, self.state)
	
