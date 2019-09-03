from django.db import models
from django.utils.translation import gettext_lazy as _

from django_extensions.db.models import TimeStampedModel

class Match(TimeStampedModel):
    """Match"""

    opponent = models.CharField(
        verbose_name=_("opponent"),
        max_length=60)
    date = models.DateField(
        verbose_name=_("date"))
    home = models.BooleanField(
        verbose_name=_("home"))
    
    def __str__(self):
        """str"""
        if self.home:
            return f"DES 1 - {self.opponent}"
        return f"{self.opponent} - DES 1"
