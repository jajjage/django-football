"""views"""
from django.db.models import Count

from rest_framework import generics

from players.models import Player
from matches.models import Match
from . import serializers


class TopscorerList(generics.ListAPIView):
    """Topscorer list"""
    queryset = Player.objects.all() \
        .annotate(num_goals=Count('goals')) \
        .order_by("-num_goals")
    serializer_class = serializers.TopscorerSerializer


class PlayerDetail(generics.RetrieveAPIView):
    """Topscorer list"""
    queryset = Player.objects.all()
    serializer_class = serializers.PlayerSerializer


class MatchList(generics.ListAPIView):
    """Topscorer list"""
    queryset = Match.objects.all().order_by("date")
    serializer_class = serializers.MatchSerializer
