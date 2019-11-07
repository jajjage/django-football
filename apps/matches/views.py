"""views"""
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Match


class MatchListView(LoginRequiredMixin, ListView):
    """View for listing matches"""
    model = Match

class MatchDetailView(DetailView):
    """view for listing matches"""
    model = Match

    def get_context_data(self, **kwargs):
        """Insert the single object into the context dict."""
        context = {}
        if self.object:
            context['goals'] = self.object.goals.all().select_related("player")
        return super().get_context_data(**context)
