"""admin"""

from wagtail.contrib.modeladmin.options import (ModelAdmin, modeladmin_register)

from .models import Goal


class GoalAdmin(ModelAdmin):
    """BaseAdmin for NamedAtrributes"""
    model = Goal
    menu_icon = 'snippet'
    menu_order = 1000
    list_display = [
        "__str__",
        "player",
        "match",
    ]
modeladmin_register(GoalAdmin)
