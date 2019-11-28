"""urls"""
from django.urls import path, include

from rest_framework.routers import SimpleRouter

from .matches.viewsets import MatchViewSet
from .players.viewsets import PlayerViewSet

router = SimpleRouter()
router.register(r'players', PlayerViewSet)
router.register(r'matches', MatchViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
