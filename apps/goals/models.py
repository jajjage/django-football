from django.db import models
from django.utils.translation import gettext_lazy as _

from django_extensions.db.models import TimeStampedModel

from matches.models import Match
from players.models import Player


class Goal(TimeStampedModel):
    """Goal"""

    match = models.ForeignKey(
        Match,
        on_delete=models.PROTECT,
        related_name="goals",
        verbose_name=_("match"))
    player = models.ForeignKey(
        Player,
        on_delete=models.PROTECT,
        related_name="goals",
        verbose_name=_("player"))

    def __str__(self):
        """str"""
        return _("Goal by {} during {}").format(self.player, self.match)

    class Meta:
        "meta"
        verbose_name = _("Goal")
        verbose_name_plural = _("Goals")
