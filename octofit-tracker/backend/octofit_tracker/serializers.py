from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout


class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    def get_id(self, obj):
        return str(obj._id)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']


class TeamSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    def get_id(self, obj):
        return str(obj._id)

    class Meta:
        model = Team
        fields = ['id', 'name', 'members']


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    def get_id(self, obj):
        return str(obj._id)

    class Meta:
        model = Activity
        fields = ['id', 'username', 'activity_type', 'duration', 'date']


class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    def get_id(self, obj):
        return str(obj._id)

    class Meta:
        model = Leaderboard
        fields = ['id', 'username', 'score']


class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    def get_id(self, obj):
        return str(obj._id)

    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'duration']
