from django.db.models import Count, F
from django import template
from news.models import Category
from django.core.cache import cache

register = template.Library()

@register.simple_tag(name = 'get_list_categories')
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('news/list_categories.html')
def show_categories(arg1 = 'Hello', arg2 = 'world'):
    #Еще один вариант кэширования(API низкого уровня для кэширования)
    # categories = cache.get('categories')
    # if not categories:
    #     categories =  Category.objects.annotate(cnt = Count('news', filter=F('news__is_published'))).filter(cnt__gt=0)
    #     cache.set('categories', categories, 30) #ВАЖНО! При разкомментировании удалить нижестоящюю переменную categories!
    categories =  Category.objects.annotate(cnt = Count('news', filter=F('news__is_published'))).filter(cnt__gt=0)
    return {"categories": categories, "arg1": arg1, "arg2": arg2}