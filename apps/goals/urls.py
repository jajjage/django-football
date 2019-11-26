"""urls"""
from django.urls import path

from .views import TopscorersListView

app_name = 'goals'

urlpatterns = [
    path("", TopscorersListView.as_view(), name="topscorers"),
]
