from django.contrib import admin

from mysite.rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
	list_display = ('title','category','url','slug')

admin.site.register(Category)

#Custom admin page admin.ModelAdmin is a class representation of a model in the admin interface. Must register model with ModelAdmin object.
#if you want the standard output then no need for a ModelAdmin object
admin.site.register(Page,PageAdmin)




# Register your models here.
