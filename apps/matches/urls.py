"""Match urls"""
from django.urls import path

from .views import MatchListView

app_name = 'faqs'
urlpatterns = [
    path("", MatchListView.as_view(), name="list"),
]
