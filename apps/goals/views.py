"""views"""
from django.db.models import Count
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from players.models import Player


class TopscorersListView(LoginRequiredMixin, ListView):
    """View for listing matches"""
    queryset = Player.objects.all() \
        .annotate(num_goals=Count('goals')) \
        .order_by("-num_goals")
