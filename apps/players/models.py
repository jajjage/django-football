"""models"""
import uuid as uuid_lib

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from django_extensions.db.models import TimeStampedModel

UserModel = get_user_model()


class Player(TimeStampedModel):
    """Player"""

    name = models.CharField(
        verbose_name=_("name"),
        max_length=60)
    user = models.OneToOneField(
        UserModel,
        on_delete=models.SET_NULL,
        verbose_name=_("user"),
        blank=True,
        null=True)
    uuid = models.UUIDField( # Used by the API
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False)

    @property
    def total_goals(self):
        """return number of scored goals"""
        return self.goals.all().count()

    def __str__(self):
        return self.name
