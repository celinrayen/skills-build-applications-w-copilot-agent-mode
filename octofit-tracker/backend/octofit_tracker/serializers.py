# serializers.py for octofit_tracker
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()

class TeamSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    members = UserSerializer(many=True)

class ActivitySerializer(serializers.Serializer):
    user = UserSerializer()
    type = serializers.CharField(max_length=50)
    duration = serializers.IntegerField()

class LeaderboardSerializer(serializers.Serializer):
    team = TeamSerializer()
    points = serializers.IntegerField()

class WorkoutSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
