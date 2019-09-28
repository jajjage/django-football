from rest_framework import serializers
from players.models import Player
from matches.models import Match
from goals.models import Goal

class TopscorerSerializer(serializers.ModelSerializer):
    goals_count = serializers.ReadOnlyField()
    
    class Meta:
        model = Player
        fields = [
            'name',
            'goals_count',
        ]


class MatchSerializer(serializers.ModelSerializer):
    """Serializer for matches."""
    goals = serializers.SerializerMethodField()

    class Meta:
        """meta"""
        model = Match
        fields = ['date', 'score', 'title', 'goals']

    def get_goals(self, obj):
        """
        Returns all goals scored in the match.
        If used as nested serializer: filters by player in root serializer.
        """
        # if used as nested serializer, filter by player in root serializer.
        if self is not self.root:  
            return obj.goals.filter(player=self.root.instance).count()
        return obj.goals.count()


class PlayerSerializer(serializers.ModelSerializer):
    """Serializer for players"""
    matches = MatchSerializer(many=True, read_only=True)

    class Meta:
        model = Player
        fields = [
            'name',
            'total_goals',
            'matches',
        ]
