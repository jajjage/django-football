"""serializers"""
from rest_framework import serializers
from players.models import Player
from matches.models import Match


class TopscorerSerializer(serializers.ModelSerializer):
    """Serializer for topscorers' list."""
    total_goals = serializers.ReadOnlyField()

    class Meta:
        """meta"""
        model = Player
        fields = [
            'pk',
            'name',
            'total_goals',
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
        """meta"""
        model = Player
        fields = [
            'name',
            'total_goals',
            'matches',
        ]
