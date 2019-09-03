"""admin"""

from wagtail.contrib.modeladmin.options import (ModelAdmin, modeladmin_register)

from .models import Match


class MatchAdmin(ModelAdmin):
    """BaseAdmin for NamedAtrributes"""
    model = Match
    menu_icon = 'snippet'
    menu_order = 1000
    list_display = [
        "__str__",
        "date",
    ]
modeladmin_register(MatchAdmin)
