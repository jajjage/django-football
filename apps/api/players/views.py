"""player views"""
from django.db.models import Count

from rest_framework import generics

from players.models import Player
from .serializers import PlayerSerializer


class TopscorerList(generics.ListAPIView):
    """Topscorer view for players."""
    queryset = Player.objects.all() \
        .annotate(num_goals=Count('goals')) \
        .order_by("-num_goals")
    serializer_class = PlayerSerializer


class PlayerDetail(generics.RetrieveAPIView):
    """Detail view for players."""
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
