"""models"""
import uuid as uuid_lib

from django.db import models
from django.utils.translation import gettext_lazy as _

from django_extensions.db.models import TimeStampedModel

from matches.models import Match
from players.models import Player


class Goal(TimeStampedModel):
    """Stores a goal scored in a match by a specific player."""
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
    uuid = models.UUIDField( # Used by the API
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False)

    def __str__(self):
        return _("Goal by {} during {}").format(self.player, self.match)

    class Meta:
        verbose_name = _("Goal")
        verbose_name_plural = _("Goals")
        ordering = ["-match"]
