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
    """Nested serializer for matches."""
    goals = serializers.SerializerMethodField()

    class Meta:
        """meta"""
        model = Match
        fields = ['date', 'score', 'title', 'goals']

    def get_goals(self, obj):
        """returns all goals scored by the player in the match"""
        return obj.goals.filter(player=self.root.instance).count()


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

