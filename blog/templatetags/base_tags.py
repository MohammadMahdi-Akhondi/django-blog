from django import template
from ..models import Category, Article

register = template.Library()

@register.inclusion_tag('blog/partials/sidebar.html')
def sidebar():
    return {
        "articles" : Article.objects.filter(status = "p").order_by("-publish")[:3],
        "categories" : Category.objects.filter(status = True)
    }