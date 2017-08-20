from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=126,unique=True)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	
	def __str__(self):
		return self.name
	
	class Meta:
		verbose_name_plural = "Categories"

class Page(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=128)
	url = models.URLField(default="www.python.org")
	views = models.IntegerField(default=0)

	def __str__(self):
		return self.title


# Create your models here.


