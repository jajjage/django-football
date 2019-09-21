"""Match urls"""
from django.urls import path

from .views import TopscorersView

app_name = 'goals'

urlpatterns = [
    path("", TopscorersView.as_view(), name="topscorers"),
]
