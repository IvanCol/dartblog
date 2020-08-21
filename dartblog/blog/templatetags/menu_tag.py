from django import template

from blog.models import Category

register = template.Library()


@register.inclusion_tag('blog/tags/menu.html')
def show_menu(menu_class='menu'):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'menu_class': menu_class,
    }
    return context
