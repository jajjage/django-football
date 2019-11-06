"""urls"""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import TopscorerList, PlayerDetail, MatchList


urlpatterns = [
    path("players/", TopscorerList.as_view(), name="topscorers"),
    path("players/<int:pk>", PlayerDetail.as_view(), name="player-detail"),
    path("matches/", MatchList.as_view(), name="matches"),

]

urlpatterns = format_suffix_patterns(urlpatterns)
