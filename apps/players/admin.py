"""admin"""

from wagtail.contrib.modeladmin.options import (ModelAdmin, modeladmin_register)

from .models import Player


class MatchAdmin(ModelAdmin):
    """BaseAdmin for NamedAtrributes"""
    model = Player
    menu_icon = 'snippet'
    menu_order = 1000
    list_display = [
        "__str__",
    ]

modeladmin_register(MatchAdmin)
