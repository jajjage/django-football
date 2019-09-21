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
    opponent_goals = models.PositiveIntegerField(
        verbose_name=_("opponent goals"),
        null=True)

    class Meta:
        "meta"
        verbose_name = _("Match")
        verbose_name_plural = _("Matches")

    def __str__(self):
        """str"""
        if self.home:
            return f"DES 1 - {self.opponent} ({self.score})"
        return f"{self.opponent} - DES 1 ({self.score})"

    @property
    def score(self):
        """str"""
        team_goals = self.goals.count()
        if self.opponent_goals:
            if self.home:
                return f"{team_goals} - {self.opponent_goals}"
            return f"{self.opponent_goals} - {team_goals}"
        return _("no score yet")
