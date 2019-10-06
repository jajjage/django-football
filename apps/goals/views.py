"""views"""
from django.db.models import Count

from core.views import BaseView
from players.models import Player


class TopscorersView(BaseView):
    """view for listing matches"""
    template_name = "goals/topscorers.html"

    def get_context(self):
        """context"""
        return {
            "players": Player.objects.all()
                       .annotate(num_goals=Count('goals'))
                       .order_by("-num_goals")
        }
