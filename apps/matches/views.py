"""views"""
from django.views.generic.detail import DetailView

from core.views import BaseView

from .models import Match


class MatchListView(BaseView):
    """view for listing matches"""
    template_name = "matches/matches_list.html"

    def get_context(self):
        """context"""
        return {
            "matches": Match.objects.all(),
        }


class MatchDetailView(DetailView):
    """view for listing matches"""
    template_name = "matches/matches_detail.html"
    model = Match

    def get_context_data(self, **kwargs):
        """Insert the single object into the context dict."""
        context = {}
        if self.object:
            context['goals'] = self.object.goals.all().select_related("player")
        return super().get_context_data(**context)
