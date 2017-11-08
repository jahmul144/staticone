from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.

from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField(max_length=126,unique=True)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	slug = models.SlugField(default='',unique=True)	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

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

class UserProfile(models.Model):
	
	user = models.OneToOneField(User)
	
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)
	
	def __str__(self):
		return self.user.username

	 


# Create your models here.


