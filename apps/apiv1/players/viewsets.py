"""views"""
from django.db.models import Count

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets

from players.models import Player
from . import serializers


class PlayerViewSet(viewsets.ReadOnlyModelViewSet):
    """Retrieve player list or detail"""
    queryset = Player.objects.all() \
        .prefetch_related("matches") \
        .annotate(num_goals=Count('goals')) \
        .order_by("-num_goals")
    serializer_class = serializers.PlayerSerializer
    lookup_field = "uuid"
    permission_classes = [IsAuthenticatedOrReadOnly]
