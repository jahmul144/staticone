from django import template
from mysite.rango.models import Category

register = template.Library()

@register.inclusion_tag('/mysite/rango/cats.html')
def get_category_list(cat=None):
	return {'cats': Category.objects.all(),'act_Cat':cat}


