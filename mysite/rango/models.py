from django.db import models

# Create your models here.

class Page(models.Model):
        category = models.ForeignKey('rango.Category')
        title = models.CharField(max_length=128)
        views = models.IntegerField(default=0)

        def __str__(self):
                return self.title

# Create your models here.
