"""serializers"""
from rest_framework import serializers

from matches.models import Match
from players.models import Player

class MatchSerializer(serializers.ModelSerializer):
    """Serializer for matches."""
    match_goals = serializers.SerializerMethodField()
    player_goals = serializers.SerializerMethodField()
    class Meta:
        model = Match
        fields = ['date', 'score', 'title', 'match_goals', 'player_goals', 'uuid']

    @staticmethod
    def get_match_goals(obj):
        """Returns all goals scored during the match."""
        return obj.goals.count()

    def get_player_goals(self, obj):
        """Returns all goals scored by player during the match.
        If NOT used as nested serializer: returns None.
        """
        if isinstance(self.root.instance, Player):
            return obj.goals.filter(player=self.root.instance).count()
        return None
