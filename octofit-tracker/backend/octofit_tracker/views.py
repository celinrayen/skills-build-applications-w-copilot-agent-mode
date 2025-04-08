# views.py for octofit_tracker
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserView(APIView):
    def get(self, request):
        return Response({"url": "https://organic-goldfish-5vwx7qvw694fv4q-8000.app.github.dev/api/users/"}, status=status.HTTP_200_OK)

class TeamView(APIView):
    def get(self, request):
        return Response({"url": "https://organic-goldfish-5vwx7qvw694fv4q-8000.app.github.dev/api/teams/"}, status=status.HTTP_200_OK)

class ActivityView(APIView):
    def get(self, request):
        return Response({"url": "https://organic-goldfish-5vwx7qvw694fv4q-8000.app.github.dev/api/activity/"}, status=status.HTTP_200_OK)

class LeaderboardView(APIView):
    def get(self, request):
        return Response({"url": "https://organic-goldfish-5vwx7qvw694fv4q-8000.app.github.dev/api/leaderboard/"}, status=status.HTTP_200_OK)

class WorkoutView(APIView):
    def get(self, request):
        return Response({"url": "https://organic-goldfish-5vwx7qvw694fv4q-8000.app.github.dev/api/workouts/"}, status=status.HTTP_200_OK)
