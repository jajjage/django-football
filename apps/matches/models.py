"""models"""
from django.db import models
from django.utils.translation import gettext_lazy as _

from django_extensions.db.models import TimeStampedModel
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel

from players.models import Player


class Match(ClusterableModel, TimeStampedModel):
    """A match between two teams."""

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
    players = models.ManyToManyField(
        Player,
        related_name="matches",
        verbose_name=_("players"),
    )
    class Meta:
        verbose_name = _("Match")
        verbose_name_plural = _("Matches")

    def __str__(self):
        if self.home:
            return f"DES 1 - {self.opponent}"
        return f"{self.opponent} - DES 1"

    @property
    def title(self):
        """Returns title"""
        # TODO: remove
        return self.__str__()

    @property
    def team_goals(self):
        """Returns number of goals scored by own team."""
        return self.goals.count()

    @property
    def score(self):
        """Returns match score."""
        if self.opponent_goals:
            if self.home:
                return f"{self.team_goals} - {self.opponent_goals}"
            return f"{self.opponent_goals} - {self.team_goals}"
        return _("no score yet")

    panels = [
        FieldPanel("opponent"),
        FieldPanel("date"),
        FieldPanel("home"),
        FieldPanel("opponent_goals"),
        InlinePanel("goals", label=_("goals")),
        FieldPanel("players"),
    ]
