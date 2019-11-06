"""urls"""
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .matches.viewsets import MatchViewSet
from .players.viewsets import PlayerViewSet
from .views import SchemaView

router = DefaultRouter()
router.register(r'players', PlayerViewSet)
router.register(r'matches', MatchViewSet)

urlpatterns = [
    path('', SchemaView.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include(router.urls)),
    path('redoc', SchemaView.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
