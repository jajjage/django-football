"""views"""
from rest_framework import generics

from matches.models import Match
from . import serializers


class MatchList(generics.ListAPIView):
    """Topscorer list"""
    queryset = Match.objects.all().order_by("date")
    serializer_class = serializers.MatchSerializer
