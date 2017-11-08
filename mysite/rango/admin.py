from django.contrib import admin

from mysite.rango.models import Category, Page, UserProfile

class PageAdmin(admin.ModelAdmin):
	list_display = ('title','category','url')

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}

admin.site.register(Category,CategoryAdmin)

#Custom admin page admin.ModelAdmin is a class representation of a model in the admin interface. Must register model with ModelAdmin object.
#if you want the standard output then no need for a ModelAdmin object
admin.site.register(Page,PageAdmin)

admin.site.register(UserProfile)




# Register your models here.
