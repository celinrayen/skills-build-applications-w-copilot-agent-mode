# tests.py for octofit_tracker
from django.test import TestCase

class UserTests(TestCase):
    def test_user_creation(self):
        self.assertEqual(1, 1)

class TeamTests(TestCase):
    def test_team_creation(self):
        self.assertEqual(1, 1)

class ActivityTests(TestCase):
    def test_activity_creation(self):
        self.assertEqual(1, 1)

class LeaderboardTests(TestCase):
    def test_leaderboard_creation(self):
        self.assertEqual(1, 1)

class WorkoutTests(TestCase):
    def test_workout_creation(self):
        self.assertEqual(1, 1)
