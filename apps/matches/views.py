from django.shortcuts import render

from core.views import BaseView

from .models import Match


class MatchListView(BaseView):
    """view for listing matches"""
    template_name = "matches/list.html"

    def get_context(self):
        """context"""
        return {
            "matches": Match.objects.all(),
        }
