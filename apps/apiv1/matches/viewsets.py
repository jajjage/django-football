"""views"""
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from matches.models import Match
from .serializers import MatchSerializer


class MatchViewSet(viewsets.ReadOnlyModelViewSet):
    """Retrieve match list or detail"""
    queryset = Match.objects.all().order_by("date")
    serializer_class = MatchSerializer
    lookup_field = "uuid"
    permission_classes = [IsAuthenticatedOrReadOnly]
