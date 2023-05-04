from django import template
from cms.models import Menu

register = template.Library()


@register.inclusion_tag('home.html', takes_context=True)
def show_top_menu(context):
    menu_items = Menu.objects.all()
    return {
        "menu_items": menu_items,
    }
