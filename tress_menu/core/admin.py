from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from core.models import MenuItem


@admin.register(MenuItem)
class MenuItemMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20
