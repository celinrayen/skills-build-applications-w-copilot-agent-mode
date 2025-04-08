# views.py for octofit_tracker
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserView(APIView):
    def get(self, request):
        return Response({"message": "User endpoint"}, status=status.HTTP_200_OK)

class TeamView(APIView):
    def get(self, request):
        return Response({"message": "Team endpoint"}, status=status.HTTP_200_OK)

class ActivityView(APIView):
    def get(self, request):
        return Response({"message": "Activity endpoint"}, status=status.HTTP_200_OK)

class LeaderboardView(APIView):
    def get(self, request):
        return Response({"message": "Leaderboard endpoint"}, status=status.HTTP_200_OK)

class WorkoutView(APIView):
    def get(self, request):
        return Response({"message": "Workout endpoint"}, status=status.HTTP_200_OK)
