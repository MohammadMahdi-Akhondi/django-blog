from django import template
from django.db.models import Count
from datetime import datetime, timedelta

from ..models import Category, Article

register = template.Library()

@register.inclusion_tag('blog/partials/sidebar.html')
def sidebar():
    return {
        "articles" : Article.objects.filter(status = "p").order_by("-publish")[:3],
        "categories" : Category.objects.filter(status = True)
    }

@register.inclusion_tag('blog/partials/popular_articles.html')
def popular_articles():
    last_month = datetime.today() - timedelta(days = 30)
    return {
        "popular_articles" : Article.objects.published().filter(articlehit__created__gte = last_month).annotate(count = Count('hits')).order_by('-count', '-publish')
    }