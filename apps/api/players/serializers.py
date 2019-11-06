"""serializers"""
from rest_framework import serializers
from players.models import Player

from ..matches.serializers import MatchSerializer


class PlayerSerializer(serializers.ModelSerializer):
    """Serializer for players"""
    matches = MatchSerializer(many=True, read_only=True)

    class Meta:
        model = Player
        fields = [
            'uuid',
            'name',
            'total_goals',
            'matches',
        ]
